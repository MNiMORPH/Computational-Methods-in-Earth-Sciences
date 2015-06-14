import numpy as np
from scipy.sparse import spdiags, identity
from scipy.sparse.linalg import spsolve, isolve
from matplotlib import pyplot as plt

# Time
dt = 5000 # [s]
Tend = 10000 # [s]

# Grid
Tstart = np.zeros(100)
T = Tstart.copy()
#T[50] = 1.
dx = 0.01 # [m]
x = np.arange(0, len(Tstart)*dx, dx)

# Parameters
kappa = 1E-6 # Thermal diffusivity [m**2 / s]

# Boundary conditions -- Dirichlet
bcl = np.array([50]) # Jumps up to 50 degrees at t=0
bcr = np.array([0])  # Stays at 0.

# Put boundary conditions into the RHS "a" array
a = np.hstack(( bcl, np.zeros(len(T)-2), bcr ))

# Let's be smarter this time and pull this part out:
# Because the diffusivity is constant, this portion is also going to be constant
# and therefore need not be recalculated every time
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
# Calling it base here to show that it does not have scalar applied yet
A = -spdiags(diagonals, offsets, len(T), len(T), format='csr')
AI = A + identity(A.shape[0])

# Solve as a forward difference
for i in range(int(np.floor(Tend/dt))):
  T = spsolve(AI, T + (kappa * dt / dx**2)*a)
# Plot
plt.plot(x, T); plt.show()

