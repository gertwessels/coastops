# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 14:30:26 2016

@author: gwessels
"""

import pandas as pd
import datetime
from numpy import nan

class Ocean_HDF5:
    def __init__(self,filename,path='./'):
        self.file = filename
        self.path = path
        self.df_cols = ['date_time','latitude', 'longitude', 'grid_x', 'grid_y', 
                 'depth','total_depth', 'current_u', 'current_v', 'water_level',
                 'vorticity', 'enstrophy', 'sign_wave_height',
                 'peak_wave_period', 'peak_wave_dir',
                 'mean_wave_period', 'mean_wave_dir', 'direc_spread',
                 'energy_dissip', 'energy_leak', 'fraction_breaking',
                 'orbital_vel', 'mean_steepness', 'mean_wave_height',
                 'energy_dissipation']
        self.df = pd.DataFrame(columns=self.df_cols)
        
    def append(self,date_time=datetime.datetime.today(), 
                 latitude=nan, longitude=nan, grid_x=nan, grid_y=nan, depth=nan, 
                 total_depth=0, current_u=nan, current_v=nan, water_level=nan,
                 vorticity=nan, enstrophy=nan, sign_wave_height=nan,
                 peak_wave_period=nan, peak_wave_dir=nan, 
                 mean_wave_period=nan, mean_wave_dir=nan, direc_spread=nan,
                 energy_dissip=nan, energy_leak=nan, fraction_breaking=nan,
                 orbital_vel=nan, mean_steepness=nan, mean_wave_height=nan,
                 energy_dissipation=nan):

#        append_dframe = pd.DataFrame([[date_time, latitude, longitude, 
#                 grid_x, grid_y, depth, total_depth, current_u, current_v, 
#                 water_level, vorticity, enstrophy, sign_wave_height, 
#                 peak_wave_period, peak_wave_dir, mean_wave_period, 
#                 mean_wave_dir, direc_spread, energy_dissip, energy_leak, 
#                 fraction_breaking, orbital_vel, mean_steepness, mean_wave_height,
#                 energy_dissipation]],columns=self.df_cols)
                 
#        print append_dframe
        
        
        if self.df.index.max() != self.df.index.max():
            index = -1
        else:
            index = self.df.index.max()
        
        self.df.loc[index + 1] = [date_time, latitude, longitude, 
                 grid_x, grid_y, depth, total_depth, current_u, current_v, 
                 water_level, vorticity, enstrophy, sign_wave_height, 
                 peak_wave_period, peak_wave_dir, mean_wave_period, 
                 mean_wave_dir, direc_spread, energy_dissip, energy_leak, 
                 fraction_breaking, orbital_vel, mean_steepness, mean_wave_height,
                 energy_dissipation]
                 
    def write(self):
        self.df.to_hdf(self.path+self.file+'.hdf','test',mode='w')
        
    def write_csv(self):
        self.df.to_csv(self.file+'.csv',mode='w')
        
    def read(self):
        self.df = pd.read_hdf(self.path+self.file+'.hdf')
#        self.df.append(append_dframe)
        
        
    def dataframe(self):
        return self.df
    
    def dataframe_columns(self):
        return self.df_cols
    
    def max_index(self):
        return self.df.index.max()
        
        