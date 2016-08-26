# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 08:12:59 2016

@author: gwessels
"""

from zipfile import ZipFile
from config_file import Config_File
from ftplib import FTP
from import_data import import_ncep_text_file
import d3d_file_generation as d3d
import datetime as dt
import mdf


def main():
#    modify_mdf('/data/Projects/DDZMS/morning_sim/False_Bay9_operational.mdf','new_FB.mdf',dt.datetime(2000,1,1),dt.datetime(2014,1,1),dt.datetime(2014,1,2))
#    modify_mdw('/data/Projects/DDZMS/morning_sim/Oper.mdw','new_FB.mdw','False_Bay9_operational.mdf',dt.datetime(2000,1,1))
    generate_FalseBay_model()

def generate_FalseBay_model():    
    # * Requires a zipfile with the original model files.
    # * Simulation will run once a day
    
    original_model_zipfile = 'model.zip'
    new_model_dir = generate_foldername()
#    restart_file_dir = ''
    
    referencedate = dt.datetime(2000,1,1,0,0)
    
#    timestart  =    0.0
#    timestop   = 4320.0
    dt_min     =  180.0

#    This depends on when it will be run. If you run it at 20:00 on Monday to provide a 
#    forecast for Tuesday then you should adjust date_start.    
    date_start = dt.datetime(dt.datetime.now().year,dt.datetime.now().month,dt.datetime.now().day,0,0,0)
    date_end   = date_start + dt.timedelta(days=2)
    
##    Retrieve last run's details
#    df_config = Config_File('FB_config')
#    config = df_config.get_last()
    
#    Add current run's details.
    df_config = Config_File('FB_config')
#    Create runid
    runid = df_config.generate_runid('fb1')
    df_config.add_entry(new_model_dir,dt.datetime.now(),date_start,runid)
    df_config.write()

    # check if restart file exists in old run
    # copy restart file and map file to new directory

#    Extract original model file
    with ZipFile(original_model_zipfile) as model_zip:
        model_zip.extractall(new_model_dir)

    hdf_dict = get_ncep()
    
    d3d.generate_wavecon(runid, referencedate, date_start, date_end, dt_min, hdf_dict['Ocean_HDF'], hdf_dict['Atmos_HDF'])
    d3d.generate_wnd(runid, referencedate, date_start, date_end, dt_min, hdf_dict['Atmos_HDF'])
    
    modify_mdw(new_model_dir+'/'+'Oper.mdw',new_model_dir+'/'+new_model_dir+'.mdw','False_Bay9_operational.mdf',referencedate)
    modify_mdf(new_model_dir+'/False_Bay9_operational.mdf',new_model_dir+'/False_Bay9_operational.mdf',referencedate,date_start,date_end)
    

def modify_mdw(file_in,file_out,mdf,ref):
    # change mdf filename
    # change reference date --------- maybe not if it doesn't change between runs

    text = ''
    with open(file_in,'r') as f_in:
        for line in f_in:
            if line.split('=')[0].strip() == 'FlowFile':
                text = text + '   FlowFile  = ' + mdf + '\r\n'
            elif line.split('=')[0].strip() == 'ReferenceDate':
                text = text + '   ReferenceDate  = ' + ref.strftime('%Y-%m-%d') + '\r\n'
            else:
                text = text + line
                
    with open(file_out,'w') as f_out:
        f_out.write(text)

    
def modify_mdf(file_in,file_out,ref,start,end):
    inp, inp_order = mdf.read(file_in)
    inp['Itdate'] = ref.strftime('%Y-%m-%d')
    inp['Tstart'] = [d3d.minutes_from_refdate(start,ref)]
    inp['Tstop']  = [d3d.minutes_from_refdate(end,ref)]
    
    mdf.write(inp,file_out, selection=inp_order)

    
def get_ncep():
    
    log = []
    
    ncep = FTP('146.64.23.203')
    log.append(ncep.login('iposs','qwert'))
    log.append(ncep.cwd('ursula'))
    
    filename = generate_foldername()+'_SC1.ncep'
    
    log.append(ncep.retrbinary('RETR SC1.dat', open(filename,'w').write))
#    log.append(ncep.retrbinary('RETR NG.dat',  open(generate_foldername()+'_NG.ncep','w').write))
#    log.append(ncep.retrbinary('RETR FA.dat',  open(generate_foldername()+'_FA.ncep','w').write))
    
    hdf_dict = import_ncep_text_file(filename)
    
    return hdf_dict

#    generate wind and wave files from ncep


def generate_foldername():
    
#    runid = yyyymmdd_HHZ_FB 
    return dt.datetime.today().strftime("%Y%m%d_%HZ_FB")
        

        
if __name__ == '__main__':
    main()
