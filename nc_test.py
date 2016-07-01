# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 10:34:16 2016

@author: gwessels
"""

import numpy as np
from netCDF4 import Dataset

nrows = 87
ncols = 61
timesteps = 5
dep_avg_u = []
dep_avg_v = []

for t in np.arange(0,timesteps):
    dep_avg_u.append(np.abs(np.random.randn(nrows, ncols)*5)) # Random data
    dep_avg_v.append(np.abs(np.random.randn(nrows, ncols)*5)) # Random data

x = 100*np.arange(1, nrows + 1)
y = 100*np.arange(1, ncols + 1)

depavg_grp = Dataset('depavg_test.nc', 'w', format='NETCDF4')

depavg_grp.createDimension('we', nrows)    # west to east
depavg_grp.createDimension('sn', ncols)    # south to north
depavg_grp.createDimension('t',timesteps)

horizontal = depavg_grp.createVariable('horizontal', 'i4', ('we',))
vertical = depavg_grp.createVariable('vertical', 'i4', ('sn',))
time = depavg_grp.createVariable('time','i4',('t',))

u_velocity = depavg_grp.createVariable('u_velocity', 'f4', ('we', 'sn','t'))
v_velocity = depavg_grp.createVariable('v_velocity', 'f4', ('we', 'sn','t'))

horizontal[:] = x
vertical[:] = y
time[:] = np.arange(0,timesteps)

for t in np.arange(0,timesteps):
    u_velocity[:,:,t]  = dep_avg_u[t]
    v_velocity[:,:,t]  = dep_avg_v[t]
    
depavg_grp.close()
 