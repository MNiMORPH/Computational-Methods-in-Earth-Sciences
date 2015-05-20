#! /usr/bin/env python

import gdal
from matplotlib import pyplot as plt
import numpy as np

# GDAL is the GIS library that runs inside of standard GIS software.
# It is used for raster data (OGR is used for vector.)
# You can use it directly with Python.

# Here we are loading the 1 arcsecond SRTM DEM of Berlin (extending to around 
# Potsdam Hbf) as a GeoTIFF
ds = gdal.Open('../../data/n52_e013_1arc_v3.tif')

# Try typing "ds." (without the quotes) and then two tabs in iPython. Look at 
# how much extra information is packaged with this GeoTIFF!
# Try these:
ds.GetProjectionRef()
ds.GetGeoTransform()

band = ds.GetRasterBand(1) # only one band -- elevation
elevation = band.ReadAsArray() # So read it as a numpy array.

# OK -- let's plot it!
plt.imshow(elevation)
plt.colorbar()
plt.title('Berlin and surrounding Brandenburg')
plt.show()

# All right, now let's plot the proper coordinate system.
loc = ds.GetGeoTransform()
x = np.linspace(loc[0], \
                loc[0] + loc[1]*elevation.shape[1], \
                elevation.shape[1])
y = np.linspace(loc[3] + loc[5]*elevation.shape[0], \
                loc[3], \
                elevation.shape[0])

# Now plot
plt.imshow(elevation, extent=[x.min(), x.max(), y.min(), y.max()])
cbar = plt.colorbar() # Instantiate a class so I can modify its characteristics
cbar.set_label('Elevation [m]', fontsize=16, fontweight='bold')
plt.xlabel('Longitude E', fontsize=16, fontweight='bold')
plt.ylabel('Latitude N', fontsize=16, fontweight='bold')
plt.title('Berlin and surrounding Brandenburg\nSRTM 1-arcsecond data', \
           fontsize=20)
plt.tight_layout()
plt.show()
