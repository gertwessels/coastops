# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 08:37:35 2016

@author: gwessels
"""

import pandas as pd
import datetime
from numpy import nan

class Atmos_HDF5:
    def __init__(self,filename,path='./'):
        self.file = filename
        self.path = path
        self.df_cols = ['date_time','latitude', 'longitude', 'grid_x', 'grid_y', 
                 'altitude', 'x_wind', 'y_wind', 'air_pressure',
                 'air_temperature', 'precipitation_amount', 'relative_humidity']
        self.df = pd.DataFrame(columns=self.df_cols)
        
    def append(self,date_time=datetime.datetime.today(), 
                 latitude=nan, longitude=nan, grid_x=nan, grid_y=nan, 
                 altitude=0, x_wind=nan, y_wind=nan, air_pressure=nan,
                 air_temperature=nan, precipitation_amount=nan, 
                 relative_humidity=nan):

        if self.df.index.max() != self.df.index.max():
            index = -1
        else:
            index = self.df.index.max()
        
        self.df.loc[index + 1] = [date_time, latitude, longitude, grid_x, 
                 grid_y, altitude, x_wind, y_wind, air_pressure,
                 air_temperature, precipitation_amount, relative_humidity]
                 
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
        
        