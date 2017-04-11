# Started by ADW in class on 10 April 2017
# Thermal diffusion with a staggered grid Euler forward scheme
# Using two steps (Fourier --> flux, then energy (T) balance)
# For better illustration of how to build equations

import numpy as np
from matplotlib import pyplot as plt
#plt.ion()

# INITIALIZE

T = 1. * np.arange(100)
T[0] = 1000.
T[-1] = 0.
x = 1000. * np.arange(100) # 100 km

k = 2.
rho_c_p = 2E6

dt = 1E4 * 3.15E7 # years (3.15E7 is seconds per year)

fig = plt.figure()
plt.plot(x, T, 'k-', linewidth=4)

# RUN

# Run for 100 time steps
for i in range(int(10000)):

  dT = np.diff(T)
  dx = np.diff(x)

  q = - k * dT/dx

  x_inner = np.cumsum(dx)
  dx_inner = np.diff(x_inner)

  dT_dt = -1/(rho_c_p) * np.diff(q) / dx_inner
  
  T[1:-1] = T[1:-1] + dT_dt * dt
  
  if i%200 == 0:
    plt.plot(x, T, 'r-', linewidth=1)
  
plt.plot(x, T, 'r-', linewidth=4)

# FINALIZE -- SHOW THE PLOT

plt.show()

