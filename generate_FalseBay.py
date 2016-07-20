# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 08:12:59 2016

@author: gwessels
"""

from datetime import datetime
from zipfile import ZipFile
from config_file import Config_File

def generate_FalseBay_model():    
    # * Requires a zipfile with the original model files.
    # * Simulation will run once a day
    
    original_model_zipfile = ''
    new_model_dir = ''
    restart_file_dir = ''
    
#    Retrieve last run's details
    df_config = Config_File('FB_config')
    config = df_config.get_last()
    
#    zip and backup yesterday's run
    with ZipFile(original_model_zipfile) as model_zip:
        model_zip.extractall(new_model_dir)

    # check if restart file exists in old run
    # copy restart file and map file to new directory
    
        
    

def generate_foldername():
    
#    runid = yyyymmdd_HHZ_FB 
    return datetime.today().strftime("%Y%m%d_%HZ_FB")
        
    
