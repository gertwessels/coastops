# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 10:33:17 2016

@author: gwessels
"""

import netCDF4 as nc

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

    lon = ohdf['longitude']
    lat = ohdf['latitude']

    # define dimensions
    longitude = rootgrp.createDimension("longitude", len(lon))
    latitude = rootgrp.createDimension("latitude", len(lat))
    time = rootgrp.createDimension("time", len(julday))
    
    return
    
    
    