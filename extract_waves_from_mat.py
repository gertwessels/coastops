# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 15:52:43 2017

@author: gwessels
"""
import numpy as np
import pandas as pd
import h5py
from datetime import datetime,timedelta
import os

coord = pd.read_hdf('wave_coord.hdf')

f_hm0  = h5py.File('hsig wave height.mat','r')
f_wave = h5py.File('hsig wave vector (peak direction).mat','r')
f_tm0  = h5py.File('relative peak wave period.mat','r')
f_wind = h5py.File('wind velocity.mat','r')

time = f_hm0.get('data/Time')   # 1, 25
hm0  = f_hm0.get('data/Val')    # 246, 221, 25
x    = f_hm0.get('data/X')      # 247, 222
y    = f_hm0.get('data/Y')      # 247, 222

wav_x = f_wave.get('data/XComp')     # 246, 221, 25
wav_y = f_wave.get('data/YComp')     # 246, 221, 25

tm0 = f_tm0.get('data/Val')     # 246, 221, 25

wnd_x = f_wind.get('data/XComp')
wnd_y = f_wind.get('data/YComp')

temp = []
for t in range(len(time[0])):
    print t
    for m in range(40): # range(246):
        for n in range(40): # range(221):
            if not (x[m,n] != x[m,n]):
                tdf = coord.loc[coord['y'] == round(y[m,n],4)].loc[coord['x'] == round(x[m,n],4)]
                lat = str(tdf.latitude.values[0]).strip().strip('\'')
                lon = str(tdf.longitude.values[0]).strip().strip('\'')
                #temp.append([time[0][t],m,n,x[m,n],y[m,n],tdf.latitude,tdf.longitude,hm0[m,n,t],tm0[m,n,t],wav_x[m,n,t],wav_y[m,n,t],wnd_x[m,n,t],wnd_y[m,n,t]])
                temp.append([time[0][t],m,n,x[m,n],y[m,n],lat,lon,hm0[m,n,t],tm0[m,n,t],wav_x[m,n,t],wav_y[m,n,t],wnd_x[m,n,t],wnd_y[m,n,t]])
print 'done.'

df = pd.DataFrame(temp,columns=['matlabTime','M','N','X','Y','latitude','longitude','hm0','tm0','wave_x','wave_y','wind_x','wind_y'])

#df['speed'] = np.sqrt(df.wave_x**2 + df.wave_y**2)
df['wave direction'] = np.arctan2(df.wave_y,df.wave_x)*180/np.pi + 180
df['dateTime'] = [(datetime.fromordinal(int(x))+timedelta(days=x%1)-timedelta(days=366)).strftime("%d %B %Y, %H:%M:%S")  for x in df.matlabTime]

df['wind speed'] = np.sqrt(df.wind_x**2 + df.wind_y**2)
df['wind direction'] = np.arctan2(df.wind_y,df.wind_x)*180/np.pi + 180

pre = datetime.today().strftime("%Y%m%d_%Hh_")
datadir = 'data/'

df.to_csv(datadir+pre+'waves_wind.csv')
df.to_excel(datadir+pre+'waves_wind.xlsx')
df.to_hdf(datadir+pre+'waves_wind.hdf','w')

# Backup original .mat files
os.rename('hsig wave height.mat', datadir+pre+'hsig wave height.mat')
os.rename('hsig wave vector (peak direction).mat', datadir+pre+'hsig wave vector (peak direction).mat')
os.rename('relative peak wave period.mat', datadir+pre+'relative peak wave period.mat')
os.rename('wind velocity.mat', datadir+pre+'wind velocity.mat')


#  ======   ADDITIONAL INFO :

#f_hm0.get('data').items()
#Out[84]: 
#[(u'Name', <HDF5 dataset "Name": shape (16, 1), type "<u2">),
# (u'Time', <HDF5 dataset "Time": shape (1, 25), type "<f8">),
# (u'Units', <HDF5 dataset "Units": shape (1, 1), type "<u2">),
# (u'Val', <HDF5 dataset "Val": shape (246, 221, 25), type "<f8">),
# (u'X', <HDF5 dataset "X": shape (247, 222), type "<f8">),
# (u'XUnits', <HDF5 dataset "XUnits": shape (1, 1), type "<u2">),
# (u'Y', <HDF5 dataset "Y": shape (247, 222), type "<f8">),
# (u'YUnits', <HDF5 dataset "YUnits": shape (1, 1), type "<u2">)]
#
#f_wave.get('data').items()
#Out[85]: 
#[(u'Name', <HDF5 dataset "Name": shape (33, 1), type "<u2">),
# (u'Time', <HDF5 dataset "Time": shape (1, 25), type "<f8">),
# (u'Units', <HDF5 dataset "Units": shape (1, 1), type "<u2">),
# (u'X', <HDF5 dataset "X": shape (246, 221), type "<f8">),
# (u'XComp', <HDF5 dataset "XComp": shape (246, 221, 25), type "<f8">),
# (u'XUnits', <HDF5 dataset "XUnits": shape (1, 1), type "<u2">),
# (u'Y', <HDF5 dataset "Y": shape (246, 221), type "<f8">),
# (u'YComp', <HDF5 dataset "YComp": shape (246, 221, 25), type "<f8">),
# (u'YUnits', <HDF5 dataset "YUnits": shape (1, 1), type "<u2">)]
#
#f_tm0.get('data').items()
#Out[87]: 
#[(u'Name', <HDF5 dataset "Name": shape (25, 1), type "<u2">),
# (u'Time', <HDF5 dataset "Time": shape (1, 25), type "<f8">),
# (u'Units', <HDF5 dataset "Units": shape (1, 1), type "<u2">),
# (u'Val', <HDF5 dataset "Val": shape (246, 221, 25), type "<f8">),
# (u'X', <HDF5 dataset "X": shape (247, 222), type "<f8">),
# (u'XUnits', <HDF5 dataset "XUnits": shape (1, 1), type "<u2">),
# (u'Y', <HDF5 dataset "Y": shape (247, 222), type "<f8">),
# (u'YUnits', <HDF5 dataset "YUnits": shape (1, 1), type "<u2">)]

