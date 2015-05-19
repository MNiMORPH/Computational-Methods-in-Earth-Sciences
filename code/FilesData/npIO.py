#! /usr/bin/env python
import numpy as np

# Create two 2x3 numpy arrays
# int8 is more than enough to represent these data
a = np.array([[1,2,3],[4,5,6]], dtype='int8')
# float16 is a really rarely-used format, but I am using it here just to
# illustrate how it stores these data
b = np.array([[1.6,0.1,3.512],[-27,5,6.5109]], dtype='float16')
# look at how imprecise b is!
print b

# Let's look at a magic trick that numpy does. You know already that int8 can 
# only take numbers from -128 to +127. Well, what happens if we add 500 to a?
c = a + 500
print c
print c.dtype
# Hey -- it made it be a int16! That's pretty cool
# (Other languages like C would instead wrap around to -128 and continue
# forward, causing potential big problems)

# Now let's save an array into an *.npy file
np.save('testout.npy', a)
# And load it -- it keeps the structure of the rows and columns, great!
d = np.load('testout.npy')

# How about saving multiple arrays? we can use a compressed *.npz file
np.savez('testout.npz', a=a, b=b, c=c)
# The reason for the i=i format is because this is telling us to take array
# "c", for example, and to also call it "c" in the *.npz file.
# We could likewise change the names:
np.savez('testout.npz', x=a, y=b, z=c)

# Now let's load it
zfile = np.load('testout.npz')
print zfile['x'] == a
print zfile['y'] == b
print zfile['z'] == c
