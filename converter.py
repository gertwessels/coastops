# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 10:33:17 2016

@author: gwessels
"""
import os
from glob import glob
from netCDF4 import Dataset, num2date, date2num
from numpy import empty, size
from datetime import datetime, timedelta
import time as t

def main():
#    x = (a,b)
    x = (-65686/18.28667, 500000)
#    y = (a,b)
    y = (-3786230/-34.204, 4000000)
    
    falsebay = Converter(ax=x[0],bx=x[1],ay=y[0],by=y[1])
#    hdf_to_nc4(falsebay)
    
    
class Converter:
    
    def __init__(self,ax=1,bx=0,ay=1,by=0):
        """ 
            Grid X Coordinate = ax*Latitude + bx
            Grid Y Coordinate = ay*Longitude + by
        """
        self.ax = ax
        self.bx = bx
        self.ay = ay
        self.by = by
        
    def grid_coordinates(self,latitude,longitude):
        """
            Input can be either a single value or a array
        """
        x = []
        y = []
        try:
            for lat in latitude:
                x.append(float(lat)*self.ax + self.bx)
        except TypeError:
            x.append(float(latitude)*self.ax + self.bx)
            
        try:
            for lng in longitude:
                y.append(float(lng)*self.ay + self.by)
        except TypeError:
            y.append(float(longitude)*self.ay + self.by)

        return (x,y)
    
    def lat_long(self,grid_x,grid_y):
        """
            Input can be either a single value or a array
        """
        latitude = []
        longitude = []
        try:
            for x in grid_x:
                latitude.append((float(x)-self.bx)/self.ax)
        except TypeError:
            latitude.append((float(grid_x)-self.bx)/self.ax)
            
        try:
            for y in grid_y:
                longitude.append((float(y)-self.by)/self.ay)
        except TypeError:
            longitude.append((float(grid_y)-self.by)/self.ay)

        return (latitude,longitude)


# Rework of a script by Bjorn Backeberg
def hdf_to_nc4(converter,ohdf, ahdf=0, nc4_out='from_hdf.nc'):
    
    rootgrp = nc.Dataset(nc4_out, "w", format="NETCDF4")

    grid_x = ohdf['grid_x']
    grid_y = ohdf['grid_y']

    lat,lon = converter(grid_x, grid_y)
    
#    lon = ohdf['longitude']
#    lat = ohdf['latitude']

    # define dimensions
    rootgrp = Dataset(nc4_out, "w", format="NETCDF4")
    longitude = rootgrp.createDimension("longitude", len(lon))
    latitude  = rootgrp.createDimension("latitude", len(lat))
    time      = rootgrp.createDimension("time",len(ohdf["date_time"]))

    longitudes = rootgrp.createVariable("longitude","f8",("longitude",),fill_value = 9.9999996169031625e+35)
    longitudes.units = "degrees_east"
    longitudes.standard_name = "longitude"
    longitudes.long_name = "longitude"
    
    latitudes = rootgrp.createVariable("latitude","f8",("latitude",),fill_value = 9.9999996169031625e+35)
    longitudes.units = "degrees_north"
    longitudes.standard_name = "latitude"
    longitudes.long_name = "latitude"
    
    times = rootgrp.createVariable("time","f8",("time",),fill_value = -32767.0)
    
    
    
    
    return 0
    

    
if __name__ == '__main__':
    main()