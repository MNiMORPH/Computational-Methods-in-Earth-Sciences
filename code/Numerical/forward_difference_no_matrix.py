import numpy as np
from scipy.sparse import spdiags
from scipy.sparse.linalg import spsolve, isolve
from matplotlib import pyplot as plt

# Time
dt = 50 # [s]
Tend = 10000 # [s]

# Grid
Tstart = np.zeros(100)
T = Tstart.copy()
dx = 0.01 # [m]
x = np.arange(0, len(Tstart)*dx, dx)

# Parameters
kappa = 1E-6 # Thermal diffusivity [m**2 / s]

# Boundary conditions
bcl = np.array([50]) # Jumps up to 50 degrees at t=0
bcr = np.array([0])  # Stays at 0.

# Solve as a forward difference with no matrix.
for i in range(int(np.floor(Tend/dt))):
  Tpad = np.hstack(( bcl, T, bcr ))
  T += (kappa * dt / dx**2) * (Tpad[2:] - 2*Tpad[1:-1] + Tpad[:-2])

# Plot
plt.plot(x, T); plt.show()
