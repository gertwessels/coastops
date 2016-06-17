# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 14:15:29 2016

@author: gwessels
"""

import pandas as pd
import numpy as np
import netCDF4 as nc

def main():
    
    dep_avg_cur_H = ['x_coord','y_coord','dep_avg_cur_u','dep_avg_cur_v','uvdams','z_coord','x-centre','y-centre']
    
    df = import_map2d('exp_map2d.dat',headers=dep_avg_cur_H)

    
    


def import_map2d(filename,nan=-999,headers=['x_coord','y_coord','u','v','uvdams','z_coord','x-centre','y-centre']):
    
    df = pd.read_table(filename,skiprows=13,delim_whitespace=True,names=headers)
    
    amt_rows = len(df['x_coord'])
    
    df_nozero = df.loc[df['x_coord'] != 0]
    df_reind  = df_nozero.reset_index()
    df        = df_reind.drop('index',1)
    



    return df
    
if __name__ == '__main__':
    main()