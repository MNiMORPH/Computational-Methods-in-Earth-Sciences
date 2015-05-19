#! /usr/bin/env python

# 1 -- numpy
import numpy as np
from matplotlib import pyplot as plt

# Strip out header information
# Just remember that columns are: x, z, lat, lon
data = np.genfromtxt('../../data/BattleCreekProfile.txt', skip_header=1, \
                      delimiter=',')

# Plot as distance profile
plt.plot(data[:,0], data[:,1], 'k', linewidth=2)
plt.xlabel('Distance [km]')
plt.ylabel('Elevation [m]')
plt.title('NUMPY!')
plt.show()

# 2 -- pandas
import pandas as pd

# Import it as a data frame -- keep information in a coordinate system
data = pd.read_csv('../../data/BattleCreekProfile.txt')

# Plot -- hey look, distance is inferred!
plt.plot(data['Elevation (m)'], 'k', linewidth=2)
plt.xlabel('Distance [km]')
plt.ylabel('Elevation [m]')
plt.title('PANDAS!')
plt.show()

# Think about how useful this could be for time-series data!
# Indeed, this is the main use of Pandas, which is designed as a
# data-management library

