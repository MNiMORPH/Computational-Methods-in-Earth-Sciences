def quadratic(a,b,c):
    try:
        xpos = (-b + (b**2 - (4*a*c))**.5) / (2*a)
    except:
        xpos = None
    try:
        xneg = (-b - (b**2 - (4*a*c))**.5) / (2*a)
    except:
        xneg = None
    return xpos, xneg

x1, x2 = quadratic(1, 0, -5)
print x1, x2
