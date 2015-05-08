import snowball_functions_module as sb

# First run
print "Run 1:"
name = 'standard snowball'
diameter = 10 # [cm]
density = 450 # [kg / m^3]
release_velocity = 15 # [m/s]
release_height = 1.5 # [m]
x_flight = sb.travel_distance(rv=release_velocity, rh=release_height)
p_horizontal = sb.horizontal_momentum(rho=density, D=diameter)
print ""
print "Run 1:"
sb.print_output(n=name, x=x_flight, p=p_horizontal)
print ""

# Second run -- directly pass values
print "Run 2:"
x_flight = sb.travel_distance(rv=5, rh=1.5)
p_horizontal = sb.horizontal_momentum(rho=250, D=15)
sb.print_output(n='fluff ball', x=x_flight, p=p_horizontal)
print ""

# Third run -- pass values just in right order (no keywords)
print "Run 3:"
x_flight = sb.travel_distance(15, 2.3)
p_horizontal = sb.horizontal_momentum(450, 10)
sb.print_output('high release', x_flight, p_horizontal)
print ""

# Fourth run -- pass everything straight to print_output, 
#               including use of other functions
print "Run 4:"
sb.print_output('wicked tiny iceball', sb.travel_distance(35, 1.5), \
                sb.horizontal_momentum(917, 7) )
print ""

