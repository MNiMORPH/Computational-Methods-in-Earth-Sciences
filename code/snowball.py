import numpy as np

# Global constants
g = 9.8 # [m/s**2]
  
class Snowball(object):
  """
  snowball physics
  """

  # __init__ is a special function that is run when the class is instantiated.
  # "self" refers to all functions, variables, and anything else held by the 
  # class.

  # All of the "=" signs denote default values for the class.
  def __init__(self, name='default snowball', rho=450, D=10, rv=10, rh=1.5):
    """
    Set up and solve the snowball physics
    """
    # make these into class variables.
    # I more want to do it just mostly so the class stores the snowball's 
    # characteristics, but also so I don't have to pass variables explicitly.
    self.name = name
    self.density = rho
    self.diameter = D
    self.release_velocity = rv
    self.release_height = rh
    # And automatically run the first two functions
    # Note that with a class, we can run functions that lie below the current
    # point
    self.horizontal_momentum()
    self.travel_distance()

  # All relevant variables are part of "self" (i.e. the class), so do not 
  # need to be passed to each function. It's a help!
  def horizontal_momentum(self):
    """
    Let's find its horizontal impact momentum when hitting a stopped object
    """
    # And we don't need to return anything, because this c
    self.p = self.density * (4/3.) * np.pi * (self.diameter/2./100.)**3 \
                            * self.release_velocity # [N s]

  def travel_distance(self):
    """
    Let's see how far it will go before hitting the ground
    Ignoring wind resistance
    """
    # z = 0.5 g * t**2
    t = (2 * self.release_height / g)**0.5
    self.x = t * self.release_velocity

  def print_output(self):
    """
    Print output
    """
    print self.name, 'travels', round(self.x,1), 'meters and strikes its target'
    print 'with a momentum of', round(self.p,1), 'Newton-seconds.'













