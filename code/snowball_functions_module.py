import numpy as np

# Global constants
g = 9.8 # [m/s**2]

# Values in functions that are not output belong to those functions
# and cannot be accessed from the outside
def horizontal_momentum(rho, D):
  """
  Let's find its horizontal impact momentum when hitting a stopped object
  """
  return rho * (4/3.) * np.pi * (D/2./1000.)**3 # [N]

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
  print 'with a momentum of', round(p,5), 'Newton-seconds.'

