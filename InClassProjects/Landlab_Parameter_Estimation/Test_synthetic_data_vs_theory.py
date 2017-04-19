# Test to see if the synthetic data follow the equation that produced them
# Run after running Create_synthetic_topography_FluvialOnly.py

import numpy as np

# E = U = K_sp * A**m_sp * S**n_sp
m_sp = 0.5
n_sp = 1
U = 1E-3

Sdata = np.loadtxt('Synthetic_data/S.txt')
Adata = np.loadtxt('Synthetic_data/A.txt')

K_sp_actual = 2E-4
K_sp_from_synthetic_data = U / np.mean(Adata**m_sp * Sdata**n_sp)

print "Input K_sp:", K_sp_actual
print "K_sp from synthetic data:", K_sp_from_synthetic_data
print "Misfit = ", (K_sp_from_synthetic_data - K_sp_actual)/K_sp_actual, '%'
