# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 09:36:01 2017

@author: gwessels
"""
import numpy as np
import pandas as pd
import h5py
from datetime import datetime, timedelta
import os
import time

coord = pd.read_hdf('flow_coord.hdf')

f = h5py.File('horizontal velocity.mat','r')

time = f.get('data/Time')       # 1, 6
x = f.get('data/X')             # 10,170,99,1     10 layers. x, y shouldn't change
y = f.get('data/Y')             # 10,170,99,1
z = f.get('data/Z')             # 10,170,99,6     the layers, depth will change with time
x_comp = f.get('data/XComp')    # 10,170,99,6
y_comp = f.get('data/YComp')    # 10,170,99,6

temp = []
for t in range(len(time[0])):
    print t
    for m in range(170):
        for n in range(99):
#            for l in range(10):
            for l in [0,4,9]:    # Only extract top, middle, bottom 
            # test for nan
                if not (x[0,m,n,0] != x[0,m,n,0]):
#                   print x[0,m,n,0], y[0,m,n,0]
#                   find lat lon.
                    tdf = coord.loc[coord['y'] == round(y[0,m,n,0],4)].loc[coord['x'] == round(x[0,m,n,0],4)]
#                    print tdf
                    lat = str(tdf.latitude.values[0]).strip().strip('\'')
                    lon = str(tdf.longitude.values[0]).strip().strip('\'')
#                   temp.append([time[0][t],m,n,l,x[l,m,n,0],y[l,m,n,0],z[l,m,n,t],tdf.latitude,tdf.longitude,x_comp[l,m,n,t],y_comp[l,m,n,t]])
                    temp.append([time[0][t],m,n,l,x[l,m,n,0],y[l,m,n,0],z[l,m,n,t],lat,lon,x_comp[l,m,n,t],y_comp[l,m,n,t]])
                    # print temp
print 'done.'

df = pd.DataFrame(temp,columns=['matlabTime','M','N','layer','X','Y','Z','latitude','longitude','X_comp','Y_comp'])

df['speed'] = np.sqrt(df.X_comp**2 + df.Y_comp**2)
df['direction'] = np.arctan2(df.Y_comp,df.X_comp)*180/np.pi + 180
#df['dateTime'] = (datetime.fromordinal(int(df.matlabTime)) + timedelta(days=df.matlabTime%1) - timedelta(days = 366)).strftime("%d %B %Y, %H:%M:%S")
df['dateTime'] = [(datetime.fromordinal(int(x))+timedelta(days=x%1)-timedelta(days=366)).strftime("%d %B %Y, %H:%M:%S")  for x in df.matlabTime]

pre = datetime.today().strftime("%Y%m%d_%Hh_")
datadir = 'data/'

df.to_csv(datadir+pre+'currents.csv')
df.to_excel(datadir+pre+'currents.xlsx')
df.to_hdf(datadir+pre+'currents.hdf','w')

# Backup original .mat files
os.rename('horizontal velocity.mat', datadir+pre+'horizontal velocity.mat')



#  ======   ADDITIONAL INFO :

#In [7]: f.get('data').items()
#Out[7]: 
#[(u'Name', <HDF5 dataset "Name": shape (19, 1), type "<u2">),
# (u'Time', <HDF5 dataset "Time": shape (1, 6), type "<f8">),
# (u'Units', <HDF5 dataset "Units": shape (3, 1), type "<u2">),
# (u'X', <HDF5 dataset "X": shape (10, 170, 99, 1), type "<f8">),
# (u'XComp', <HDF5 dataset "XComp": shape (10, 170, 99, 6), type "<f8">),
# (u'XUnits', <HDF5 dataset "XUnits": shape (1, 1), type "<u2">),
# (u'Y', <HDF5 dataset "Y": shape (10, 170, 99, 1), type "<f8">),
# (u'YComp', <HDF5 dataset "YComp": shape (10, 170, 99, 6), type "<f8">),
# (u'YUnits', <HDF5 dataset "YUnits": shape (1, 1), type "<u2">),
# (u'Z', <HDF5 dataset "Z": shape (10, 170, 99, 6), type "<f8">),
# (u'ZUnits', <HDF5 dataset "ZUnits": shape (1, 1), type "<u2">)]
