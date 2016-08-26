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
            d = {'datatime':[datetime.now()],'model_date':[nan], 'runid':[nan],'model_zip':['model.zip']}
            self.df = pd.DataFrame(data=d)

#        return self.df

    def get_config(self):
        return self.df
    
    def set_config(self,data):
        self.df = data

#    self,datetime,date,string,string
    def add_entry(self,model_zip,dt=datetime.now(),model_date=datetime.today().date(),runid=nan):
        
        if self.df.index.max() != self.df.index.max():
            index = -1
        else:
            index = self.df.index.max()
        
        self.df.loc[index + 1] = [dt, model_date, model_zip, runid]
        
    def get_last(self):
        ind = self.df.index.max()
#        print ind
#        print self.df
#        print self.df.loc[0]
#        
        if self.df.index.max() != self.df.index.max():
            return nan
        else:
            return self.df.loc[self.df.index.max()]
    
    def generate_runid(self, ident='run'):
#        The runid should have a format:  <some unique 3 letter identifier>_0000
#       A unique runid is required if you wish to use the restart file
        df = self.get_last()
        print df        
        
        runid = ''
        if df['runid'] != df['runid']:
            runid = '%s_%04d' % (ident[:3],0)
        else:
            old_id = df['runid'].split('_')
            runid = '%s_%04d' % (old_id[0],int(old_id[1])+1)
        return runid
    
    def write(self):
#        self.df.to_csv(self.file,'config',mode='w')
        self.df.to_csv(self.file,sep=',',mode='w')
    