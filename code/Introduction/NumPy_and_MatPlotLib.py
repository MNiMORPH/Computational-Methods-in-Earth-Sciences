from matplotlib import pyplot as plt
import numpy as np

# ADW, 2017-02-20
# Code for demonstration purposes only!

a = np.zeros((10,2)) # 10 rows, 2 columns

# Populate first row with a set of values from 0 to 9;
a[:,0] = np.arange(10)

# Then make a half-parabola
a[:,1] = a[:,0]**2

# Now, plot it. Here's the easy way, but less flexible:
plt.plot(a[:,0], a[:,1])

# Here I'm using a lot more options
# See also: http://matplotlib.org/users/artists.html
fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(1,1,1) # you can set projection, etc. here
# You can now either use plt. (...) directly, because this is the currently-
# selected plot, or use the "ax" object you defined to modify it
ax.plot(a[:,0], a[:,1], 'ko') # Black circles; there are more ways to define
                              # marker, color, etc. properties; use
                              # help(plt.plot) or help(ax.plot)
# Two ways to add labels
ax.set_xlabel('x', fontsize=16)
plt.ylabel('y', fontsize=24)

#plt.ion() # If you want interactive plotting
plt.show()
