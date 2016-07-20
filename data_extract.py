# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 11:28:35 2016

@author: gwessels
"""
from datetime import datetime
from numpy import nan
from numpy import random
import os
import pandas as pd


def get_range(a_start,a_end,a='latitude',b_start,b_end,b='longitude',df):
    if a_start>a_end:
        a_0 = a_end
        a_i = a_start
    else:
        a_0 = a_start
        a_i = a_end
        
    if b_start>b_end:
        b_0 = b_end
        b_i = b_start
    else:
        b_0 = b_start
        b_i = b_end            
    
    return df[(df.loc[:,a]>=a_0) & (df.loc[:,a]<=a_i) & (df.loc[:,b]>=b_0) & (df.loc[:,b]<=b_i)]
    

class Data_Extract_Config():
    
    def __init__(self,filename):
        self.file = filename
#        Description/name of the location(str), 
#           latitude (float), longitude (float), 
#           grid_x (int), grid_y (int), 
#           use_grid (bool) else will use coord
        self.columns = ['location','latitude','longitude','grid_x','grid_y','use_grid','date_added','user','client']

#        If the file exist, read it into self.df or else create a blank self.df
        if os.path.isfile(self.file):
            self.df = pd.read_csv(self.file)
        else:
            self.df = pd.DataFrame(columns=self.columns)

        return self.df
    
    def get_config(self):
        return self.df
    
    def set_config(self,data):
        self.df = data

#   Assumes that the grid coordinate will be used
    def add_entry(self,location="{}_{}".format('CSIR',random.random_integers(1000,9999)),latitude=nan, longitude=nan, 
                  grid_x, grid_y, use_grid=True, date_added=datetime.now(), user, client='CSIR'):
        
        if self.df.index.max() != self.df.index.max():
            index = -1
        else:
            index = self.df.index.max()
        
        self.df.loc[index + 1] = [location, latitude, longitude, grid_x, grid_y, use_grid, date_added, user, client]
        
#    only assumption is that the hdf_file contains necessary coordinate/ grid columns
#    This will find all the data given the config file
    def get_data(self,hdf_file):
        
        file_df = pd.read_hdf(hdf_file)
    
        if self.df.use_grid[0]:
            lookup_df = file_df[(file_df.loc[:,'grid_x']==self.df.grid_x[0]) & (file_df.loc[:,'grid_y']==self.df.grid_y[0])]
        else:
            lookup_df = file_df[(file_df.loc[:,'latitude']==self.df.latitude[0]) & (file_df.loc[:,'longitude']==self.df.longitude[0])]
        lookup_ind=0
        
        for index in self.df.index[1:]:
            lookup_ind=lookup_ind+1
            if self.df.use_grid[index]:
                lookup_df.append(file_df[(file_df.loc[:,'grid_x']==self.df.grid_x[index]) & (file_df.loc[:,'grid_y']==self.df.grid_y[index])])
            else:
                lookup_df.append(file_df[(file_df.loc[:,'latitude']==self.df.latitude[index]) & (file_df.loc[:,'longitude']==self.df.longitude[index])])

        return lookup_df

    
#   This doesn't make sense in this class
#    def get_last(self):
#        if self.df.index.max() != self.df.index.max():
#            return nan
#        else:
#            return self.df[self.df.index.max()]
    
    def write(self):
        self.data.to_csv(self.file,'loc_config',mode='w')