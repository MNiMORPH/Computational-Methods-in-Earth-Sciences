#! /usr/bin/env python

from netCDF4 import Dataset
import matplotlib as mpl
from matplotlib import pyplot as plt
import numpy as np
import cartopy
import cartopy.crs as ccrs

# Open NetCDF file for reading
ncfile = Dataset('../../data/3B43.20040601.7A.nc', 'r', format='NETCDF4')
lats = ncfile.variables['nlat'][:]
lons = ncfile.variables['nlon'][:]
precip = np.flipud(ncfile.variables['precipitation'][:].transpose())

# After this, we will set up the plotting domain
fig = plt.figure()
ax = fig.add_axes()

# Next, we will set up the projection and background map features
ax = plt.axes(projection=ccrs.Orthographic(100, 15))
ax.coastlines()
ax.set_global()
ax.gridlines()

# And then plot precipitation
im = ax.contourf(lons, lats, precip,
                 transform=ccrs.PlateCarree(),
                 cmap='spectral')
fig.colorbar(im)
ax.set_title('June 2004: mean ' + ncfile.variables['precipitation'].long_name \
              + ' [' + ncfile.variables['precipitation'].units + ']', \
              fontweight='bold', fontsize=16)
plt.tight_layout()
plt.show()

