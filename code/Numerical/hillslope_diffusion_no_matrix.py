#! /usr/bin/python

# Import modules
import numpy as np
from matplotlib import pyplot as plt

"""
Copyright 2012 Andrew D. Wickert

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

################################################################################
# hill.py
# 
# HILLSLOPE PROFILE
# 
# Center of hill is at 0, two incising channels at steady rate at edges
# no channel-hillslope feedback and assuming entire hill is made of mobile 
# regolith
# 
# This is a very simple example code in which variables are defined inline, 
# and the equations are solved by forward difference methods without 
# consideration for stability
# 
# Written by Andrew D. Wickert; August, 2013
################################################################################

# We will have the simple boundary condition of rivers on either end of the 
# hillslope that are incising at the same, steady rate.
zdot_channel = 2E-4 # [m], 0.5 mm/yr boundary incision

# time
dt = 100. # [years], the time step (from guessing, not from stability analysis)
t_final = 4E5 # [years], the final time for hillslope evolution
timesteps = np.arange(0,t_final + dt/10.,dt) # [years]

# Set up domain
dx = 10 # [m]
xmax = 500 # [m]
x = np.arange(-xmax, xmax + dx/10., dx) # [m], +dx/10. to make sure that edges are included
z = t_final * zdot_channel * np.ones(x.shape) # [m], elevation in meters - set such that the edges are 0 at t_final

# We're using a very simplified assumption that the rate of hillslope 
# material transport is linearly proportional to local slope, and that this 
# constant of proportionality is constant across the hill
k = 5E-3 # Slope -- soil flux scaling

# Loop through time and evolve elevation
for t in timesteps:
  # The channels set the boundaries
  z[0] -= zdot_channel * dt
  z[-1] -= zdot_channel * dt
  # for np.diff, out[n] = a[n+1] - a[n]
  # We are calculating the slopes between each of the cells, then using 
  # these to solve for discharge of material between interior cells.
  S = np.diff(z) # [-] slope
  Q = -k*S # [m**2/yr] discharge, goes downslope, hence the negative sign # POSITIVE - WHY? CANCELLED OUT AGAIN!
  # The change in internal elevation, due to conservation of mass, is equal 
  # once again to the x-defivative
  dzdt_interior = np.diff(Q)
  z[1:-1] -= dzdt_interior * dt
  # (It would have been quicker to take both derivatives at once, but would be 
  # somewhat less intuitive for descriptive purposes)

# Plot
plt.plot(x,z,'k-',linewidth=3)
plt.title('Final hillslope profile', fontsize=20, weight='bold')
plt.xlabel('Distance across hillside [m]', fontsize=16)
plt.ylabel('Elevation [m]', fontsize=16)
plt.xlim((x[0],x[-1]))
plt.show()

