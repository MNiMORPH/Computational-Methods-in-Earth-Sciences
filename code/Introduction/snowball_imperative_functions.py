#! /usr/bin/env python

# Snowball: with functions -- and assuming horizontal release

import numpy as np

# Global constants
g = 9.8 # [m/s**2]

# Values in functions that are not output belong to those functions
# and cannot be accessed from the outside.
# Functions must be listed before they are accessed in the code.
def horizontal_momentum(rho, D, rv):
  """
  Let's find its horizontal impact momentum when hitting a stopped object
  """
  return rho * (4/3.) * np.pi * (D/2./100.)**3 * rv # [N s]

def travel_distance(rv, rh):
  """
  Let's see how far it will go before hitting the ground
  Ignoring wind resistance
  I have renamed the internal variables to better show how they are passed to 
  functions
  """
  # z = 0.5 g * t**2
  t = (2 * rh / g)**0.5
  return t * rv

def print_output(n, x, p):
  """
  Print output
  """
  print n, 'travels', round(x,1), 'meters and strikes its target'
  print 'with a momentum of', round(p,1), 'Newton-seconds.'


# First run
name = 'standard snowball'
diameter = 10 # [cm]
density = 450 # [kg / m^3]
release_velocity = 15 # [m/s]
release_height = 1.5 # [m]
x_flight = travel_distance(rv=release_velocity, rh=release_height)
p_horizontal = horizontal_momentum(rho=density, D=diameter, rv=release_velocity)
print ""
print "Run 1:"
print_output(n=name, x=x_flight, p=p_horizontal)
print ""

# Second run -- directly pass values
print "Run 2:"
x_flight = travel_distance(rv=5, rh=1.5)
p_horizontal = horizontal_momentum(rho=250, D=15, rv=5)
print_output(n='fluff ball', x=x_flight, p=p_horizontal)
print ""

# Third run -- pass values just in right order (no keywords)
print "Run 3:"
x_flight = travel_distance(15, 2.3)
p_horizontal = horizontal_momentum(450, 10, 15)
print_output('high release', x_flight, p_horizontal)
print ""

# Fourth run -- pass everything straight to print_output, 
#               including use of other functions
print "Run 4:"
print_output('wicked tiny iceball', travel_distance(35, 1.5), \
             horizontal_momentum(917, 7, 35) )
print ""

