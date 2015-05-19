#! /usr/bin/env python
import numpy as np

# Create a 2x3 numpy array
a = np.array([[1,2,3],[4,5,6]])

# Save it as a straight binary output with differnet precisions.
# Check the filesize after each of these
filename = 'testout.bin'

# 8-bit unsigned integer
a.astype('uint8').tofile(filename)

# 64-bit floating point
a.astype('float64').tofile(filename)

# Now load the saved file
b = np.fromfile(filename, dtype='float64')
# Hm, we lost the information about the line ending! This is because it
# is just a string of binary without any shape data.

# Let's see what happens if we try to load it as a 8-bit integer (signed)
c = np.fromfile(filename, dtype='int8')
# WOW! It worked. But what do the values look like? Hm... so you
# could combine those sets of binary values together in clumps of 8, and 
# convert those 64-bit clumps of binary data into the original set of
# values. Not bad, huh? That's binary for ya!
