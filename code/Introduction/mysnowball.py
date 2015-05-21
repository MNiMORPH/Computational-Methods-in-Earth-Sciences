#! /usr/bin/env python

# check out how easy this is with a class!

import snowball

# instantiate
boringsnowball = snowball.Snowball() # class has built-in default values

# create another instance, with custom values
# keyword--value pairs, if given, do not have to be in order!
mysnowball = snowball.Snowball(name='Deadly Ice Boulder', rho=917, \
                               D=50, rh=1.3, rv=2.)

print ""
boringsnowball.print_output()
print ""
mysnowball.print_output()
print ""

