#! /usr/bin/env python

from netCDF4 import Dataset
from matplotlib import pyplot as plt
import numpy as np

# Open NetCDF file for reading
ncfile = Dataset('../../data/3B43.20040601.7A.nc', 'r', format='NETCDF4')

# Check out the variables
print ncfile.variables.keys()
# Let's see a bit more about precipitation
print ncfile.variables['precipitation']
# And let's get the lat and lon values
lat = ncfile.variables['nlat'][:]
lon = ncfile.variables['nlon'][:]

# Let's get the dates of the observation
dates = ncfile.FileHeader.split('\n')[4:6]
print dates
start_date = dates[0].split('=')[-1]
end_date = dates[1].split('=')[-1]

# Now let's plot precipitation
plt.figure(figsize=(14,6))
# Show image
plt.imshow(np.flipud(ncfile.variables['precipitation'][:].transpose()), \
           extent=[lon.min(), lon.max(), lat.min(), lat.max()])
plt.colorbar()
# Label it with the contained information
plt.title('June 2004: ' + ncfile.variables['precipitation'].long_name + ', [' \
          + ncfile.variables['precipitation'].units + ']')
plt.xlabel('Longitude E')
plt.ylabel('Latitude N')
plt.tight_layout()
plt.show()

