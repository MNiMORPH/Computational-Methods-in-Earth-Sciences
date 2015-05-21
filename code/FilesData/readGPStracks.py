#! /usr/bin/env python

import numpy as np
from matplotlib import pyplot as plt

# Open text file for reading
f = open('../../data/PG_astgtm2_dgps_tracks.txt', 'r')

# Prepare a list to contain each individual track
tracks = []

# Now there are two ways to do this. The first is easier, and requires more 
# memory on your computer. In this, we will read in the whole file at once
# and then parse it.

# This reads all lines in the file, and creates a list in which
# each entry is a string that is that line.
text = f.readlines()


# Go back to the beginning of the file
f.seek(0)

# This list will contain the points in each individual track.
track = []
# and this will contain the track number as recorded by the GPS
track_numbers = []

# This next statement is *asking* for an infinite loop. That is why
# I am introducing a new flow-control statement, break, that will get
# us out of it.
while True:
  # readline() reads the next line; strip() removes newline characters
  line = f.readline().strip()
  if line:
    try:
      # if the line is an integer, it is a track number
      track_numbers.append(int(line))
    except:
      # Check if the line is ending a section; if it is, package the section
      # and ship it off to the "tracks" list in its own numpy array.
      if line == 'END':
        # Only do this if we need another track to be entered; there are 
        # two "END"s at the end of the file, so this will prevent it from
        # adding an empty track there that does not correspond to the numbers
        if len(track_numbers) > len(tracks):
          tracks.append(np.array(track))
        # reset individual track list for the next one
        track = []
      else:
        # I will here in two steps split the line with data into a list and
        # turn it into a numpy array of floating point values.
        tmp0 = line.split(' ') # Split it at the spaces
        # Everything is still a string, so need to tell numpy to make the 
        # array of floating-point values
        tmp1 = np.array(tmp0, dtype=float)
        # Now append it to track -- we will change this to an array in the
        # step before we append it to the "tracks" master list (above)
        track.append(tmp1)
  else:
    # This is how we get out of the potentially infinite loop: if the 
    # line is empty
    break      
    
# Now let's plot all of these tracks' x and y components
# with the default set of different colors per line
# Remember, [:,i] means ALL ROWS IN iTH COLUMN
fig = plt.figure()
for line in tracks:
  plt.plot(line[:,0], line[:,1]) # Easting, Northing
plt.title('GPS tracks', fontsize=20, fontweight='bold')
plt.ylabel('Northing', fontsize=20)
plt.xlabel('Easting', fontsize=20)
plt.tight_layout() # Formatting helper
plt.show()

# And let's now combine all of the tracks together into a single numpy array
# to create a large set of points
# Numpy arrays play nicely with numpy lists, so we just need to use the 
# concatenate command to do this in one step!
# Other ways to combine numpy arrays include using "np.vstack" and "np.hstack"
alltracks = np.concatenate(tracks)

# And let's see if there is any statistical clustering of elevations
plt.hist(alltracks[:,-1], bins=100)
plt.title('GPS track hypsometry', fontsize=20, fontweight='bold')
plt.ylabel('Number of measurements', fontsize=20)
plt.xlabel('Elevation [m]', fontsize=20)
plt.tight_layout() # Formatting helper
plt.show()
# Yep, there are some distinct hypsometric peaks!
# But look at the x-axis and how crowded those labels are. We'll fix that
# in the next plot.

# Now, let's get some practice plotting both together:
plt.figure(figsize=(14,6)) # Wide figure
# 1 row, 2 columns, panel 1
ax1 = plt.subplot(121)
for line in tracks:
  ax1.plot(line[:,0], line[:,1]) # Easting, Northing
# You have to set the axis object properties here
ax1.set_title('GPS tracks', fontsize=20, fontweight='bold')
# Rotate x-ticks
# Can also use strings like "vertical"
# And can use plt.xticks (or plt.yticks) to set many other tick-related
# parameters.
# See, for a straightforward example:
# http://matplotlib.org/examples/ticks_and_spines/ticklabels_demo_rotation.html
plt.xticks(rotation=60) # use of "plt" explained below for ax2
ax1.set_ylabel('Northing', fontsize=20)
ax1.set_xlabel('Easting', fontsize=20)
# 1 row, 2 columns, panel 2
ax2 = plt.subplot(122)
ax2.hist(alltracks[:,-1], bins=100)
# Check this out -- "plt" applies to the currently-selected axis. So it works 
# here just as well as "ax2."
plt.title('GPS track hypsometry', fontsize=20, fontweight='bold')
plt.xticks(rotation=60)
ax2.set_ylabel('Number of measurements', fontsize=20)
ax2.set_xlabel('Elevation [m]', fontsize=20)
# Now autoformat a nice layout and show the figure
plt.tight_layout() # Formatting helper
plt.show()

