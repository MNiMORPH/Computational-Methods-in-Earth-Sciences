# 

# Formatting strings

# d -- integer
# f -- floating point
# s -- plain string

# Let's see how these change the formatting of a number.

num = 14.81
print "Original number", num
print ""
print '%d:',
print ('%d' %num)
print ""
print '%f:',
print ('%f' %num)
print ""
print '%s:',
print ('%s' %num)
print ""


# Note that the '%d' option just cuts off the decimal without rounding the 
# number! So it is doing floor division.

# The '%f' option has a pre-set decimal precision.

# The '%s' option just converts the number into a string, in the same way that 
# str(num) would do so.


# Now let's start having a bit more control.

# %d
# The number of digits in a decimal nummber may be specified
# This can create spaces before that number
print '%5d %14.81 :'
print ('%5d' %14.81)
print ""
# But will not truncate the number: it simply sets the minimum number of digits
# that must be displayed.
print '%5d %6132614.81 :'
print ('%5d' %6132614.81)
print ""
# It can also be used to generate zeros before a number instead of the spaces. 
# This is known as zero-padding (0-padding)
print '%05d %14.81 :'
print ('%05d' %14.81)
print ""

# %f
# Floating point numbers can be formatted as follows
# [TOTAL NUMBER OF CHARACTERS, INCLUDING DECIMAL].[NUMBER OF DIGITS AFTER DECIMAL POINT]

# If there is not enough precision, it still is truncated
print '%4.1f %14.89 :'
print ('%4.1f' %14.81)
print ""
# This is the perfect size for this
print '%5.2f %14.89 :'
print ('%4.1f' %14.81)
print ""
# Extra space and decimal places
print '%9.4f %14.81 :'
print ('%9.4f' %14.81)
print ""
# 0-padding with extra decimal places
print '%09.4f %14.81 :'
print ('%09.4f' %14.81)

