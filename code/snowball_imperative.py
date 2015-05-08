#! /usr/bin/env python

# Snowball: imperative -- and assuming horizontal release

import numpy as np

name = 'standard snowball'
diameter = 10 # [cm]
density = 450 # [kg / m^3]
release_velocity = 15 # [m/s]
release_height = 1.5 # [m]

# Let's find its horizontal impact momentum when hitting a stopped object
p_horizontal = density * (4/3.) * np.pi * (diameter/2./1000.)**3 \
               * release_velocity                                   # [N s]

# Let's see how far it will go before hitting the ground
# Ignoring wind resistance
# z = 0.5 g * t**2
g = 9.8 # [m/s**2]
t = (2 * release_height / g)**0.5
x_flight = t * release_velocity

# Print output
print ""
print name, 'travels', round(x_flight,1), 'meters and strikes its target'
print 'with a momentum of', round(p_horizontal,5), 'Newton-seconds.'
print ""
