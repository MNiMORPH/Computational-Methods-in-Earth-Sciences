import numpy as np
from scipy.sparse import spdiags, identity
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

# Boundary conditions -- Dirichlet
bcl = np.array([50]) # Jumps up to 50 degrees at t=0
bcr = np.array([0])  # Stays at 0.

# Put boundary conditions into the RHS "a" array
a = np.hstack(( bcl, np.zeros(len(T)-2), bcr ))

# Build tridiagonal matrix
left =   np.ones(len(T)) # If these weren't all the same value, would have
                         # to use np.roll() to arrange in proper order due
                         # to values being outside of matrix
center = -2 * np.ones(len(T))
right =   np.ones(len(T))

diagonals = (kappa * dt / dx**2) * np.vstack((left, center, right))
offsets = np.array([-1, 0, 1])

# Build it as a sparse matrix to save on memory
# Very important if you are building a big system!
A = spdiags(diagonals, offsets, len(T), len(T), format='csr')
AI = A + identity(A.shape[0])

# Solve as a forward difference
for i in range(int(np.floor(Tend/dt))):
  T = AI*T + (kappa * dt / dx**2)*a

# Plot
plt.plot(x, T); plt.show()
