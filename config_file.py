# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 14:49:01 2016

@author: gwessels
"""

from numpy import nan
from datetime import datetime
import pandas as pd
import os

class Config_File:
    
    def __init__(self,filename):
        self.file = filename
        self.columns = ['datetime','model_date','runid','model_zip',]

#        If the file exist, read it into self.df or else create a blank self.df
        if os.path.isfile(self.file):
            self.df = pd.read_csv(self.file)
        else:
            d = {'datatime':datetime.now(),'model_date':nan, 'runid':nan,'model_zip':'orig.zip'}
            self.df = pd.DataFrame(data=d)

        return self.data
        
    def get_config(self):
        return self.df
    
    def set_config(self,data):
        self.df = data

#    self,datetime,date,string,string
    def add_entry(self,dt=datetime.now(),model_date=datetime.today().date(),runid=nan,model_zip):
        
        if self.df.index.max() != self.df.index.max():
            index = -1
        else:
            index = self.df.index.max()
        
        self.df.loc[index + 1] = [dt, model_date, runid, model_zip]
        
    def get_last(self):
        if self.df.index.max() != self.df.index.max():
            return nan
        else:
            return self.df[self.df.index.max()]
    
    def write(self):
        self.data.to_csv(self.file,'config',mode='w')

        