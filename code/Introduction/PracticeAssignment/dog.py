# Import modules up here
import random

# If global constants are needed, add them up here
  
class Dog(object):
  """
  This is a docstring. You can access its text by typing help(<object_name>).
  
  This is the beginning of a class to describe a dog, its behavior, etc.
  """

  # __init__ is a special function that is run when the class is instantiated.
  # "self" refers to all functions, variables, and anything else held by the 
  # class.

  # All of the "=" signs denote default values for the class.
  def __init__(self, name):
    """
    Instantiate the class and name the dog
    """
    self.name = name

  def bark(self):
    """
    Select from one of four random barks, and print the result
    """
    whichBark = random.randint(1,5)
    bark = None # not needed, but can be a good habit to have a default
    if whichBark == 1:
      bark = 'Woof, woof!'
    elif whichBark == 2:
      bark = 'Arf... arrrrrrruff!'
    elif whichBark == 3:
      bark = 'yip! yip yipooooo!'
    elif whichBark == 4:
      bark = 'Wow! Bow wow!'
    print self.name + ': ' + bark

