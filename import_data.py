# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 14:15:29 2016

@author: gwessels
"""

from ocean_hdf5 import Ocean_HDF5
import pandas as pd
#import numpy as np
#from netCDF4 import Dataset


def main():
    
#    dep_avg_cur_H = ['x_coord','y_coord','dep_avg_cur_u','dep_avg_cur_v','uvdams','z_coord','x_centre','y_centre']
#    
#    df = import_map2d('/data/Projects/OCIMS/python_scripts/data/exp_map2d.dat',headers=dep_avg_cur_H)

    header = read_header('/data/Projects/OCIMS/python_scripts/data/exp_map2d.dat')
    
    print 'time' in header
    print header
    
    
    
    
def import_map2d(filename,nan=-999,headers=['x_coord','y_coord','u','v','uvdams','z_coord','x_centre','y_centre']):
    
    df = pd.read_table(filename,skiprows=13,delim_whitespace=True,names=headers)
#    date = pd.re
#    amt_rows = len(df)
    
#    Remove rows that contain x_coord = 0
    df_nozero = df.loc[df['x_coord'] != 0]
    df_reind  = df_nozero.reset_index()
    df        = df_reind.drop('index',1)
    
    return df
    
    
def read_header(filename):
    
    header = []
    with open(filename,'r') as f:
        for line in f:
            if line.startswith('* '):
                header.append([x.strip() for x in line[2:].split(':',1)])
            if line[0] != '*':
                break

    if header[2][0] == 'time':
        header[2][1] = datetime.datetime.strptime(header[2][1],'%Y/%m/%d %H:%M:%S')
    
    return header
        
    
def import_map2d_dep_avg(filename):
    
    dep_avg_cur_H = ['grid_x','grid_y','current_u','current_v','uvdams','z_coord','x_centre','y_centre']
    df = import_map2d(filename, nan=-999, headers=dep_avg_cur_H)
    
    ohdf = Ocean_HDF5(filename)
    
    
        
        
        
        
#def write_map2d_netcdf4(filename, dataframe, time=[]):
#    """ dataframe is a pandas.core.frame.DataFrame or list (type) or a list of dataframes
#    """
#    timedependent = False    
#    
#    if type(dataframe) == list:
#        timedependent = True
#    
#    if timedependent:    
#        dimen = len(dataframe[0])
#    else:
#        dimen = len(dataframe)
#    
#    
#    
##    nrows = 87
##    ncols = 61
##    timesteps = 5
#    dep_avg_u = []
#    dep_avg_v = []
#    
#    for t in np.arange(0,timesteps):
#        dep_avg_u.append(np.abs(np.random.randn(nrows, ncols)*5)) # Random data
#        dep_avg_v.append(np.abs(np.random.randn(nrows, ncols)*5)) # Random data
#    
#    x = 100*np.arange(1, nrows + 1)
#    y = 100*np.arange(1, ncols + 1)
#    
#    depavg_grp = Dataset('depavg_test.nc', 'w', format='NETCDF4')
#    
#    depavg_grp.createDimension('we', nrows)    # west to east
#    depavg_grp.createDimension('sn', ncols)    # south to north
#    depavg_grp.createDimension('t',timesteps)
#    
#    horizontal = depavg_grp.createVariable('horizontal', 'i4', ('we',))
#    vertical = depavg_grp.createVariable('vertical', 'i4', ('sn',))
#    time = depavg_grp.createVariable('time','i4',('t',))
#    
#    u_velocity = depavg_grp.createVariable('u_velocity', 'f4', ('we', 'sn','t'))
#    v_velocity = depavg_grp.createVariable('v_velocity', 'f4', ('we', 'sn','t'))
#    
#    horizontal[:] = x
#    vertical[:] = y
#    time[:] = np.arange(0,timesteps)
#    
#    for t in np.arange(0,timesteps):
#        u_velocity[:,:,t]  = dep_avg_u[t]
#        v_velocity[:,:,t]  = dep_avg_v[t]
#    
#    depavg_grp.close()
#    

    
if __name__ == '__main__':
    main()