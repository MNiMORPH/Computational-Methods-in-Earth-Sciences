import numpy as np
from landlab import RasterModelGrid, HexModelGrid
from landlab.components import StreamPowerEroder, FlowRouter, \
    PrecipitationDistribution, LinearDiffuser, DepressionFinderAndRouter
from landlab import imshow_grid
from copy import deepcopy
from matplotlib import pyplot as plt

plt.ion()

# Change these
uplift_rate = 0.001 # m/yr
K_sps = sorted(100E-5 - 90E-5 * np.random.rand(100))
ncells_side = 10 # number of raster cells on each side
dxy  = 2500 # side length for raster model cells [m]

# Choose 1 model grid
mg = RasterModelGrid((ncells_side, ncells_side), dxy)

# More advanced options
dt = 1000
end_thresh = uplift_rate * dt / 1E3 # Difference in cell elevations between time-steps
m_sp = 0.5
n_sp = 1.

# add initial noise to produce convergent flow from the initial conditions
np.random.seed(91) # so our figures are reproducible
mg_noise = np.random.rand(mg.number_of_nodes)/1000.

# set up the input fields
zr = mg.add_zeros('node', 'topographic__elevation')
zr += mg_noise

# Run the loop for all of the cases and compare against data
model_zmax = np.zeros((len(K_sps)))
model_slope_area_relationship = np.zeros((len(K_sps)))
i = 0
for K_sp in K_sps:
    print K_sp
    # instantiate the components:
    frr = FlowRouter(mg) # water__unit_flux_in gets automatically ingested
    spr = StreamPowerEroder(mg, K_sp=K_sp, m_sp=m_sp, n_sp=n_sp, threshold_sp=0)
    lake = DepressionFinderAndRouter(mg)
        
    # Model run loop
    zr_last = -9999
    keep_running = np.mean(np.abs(zr - zr_last)) >= end_thresh
    ti = 0
    while keep_running:
        zr_last = zr.copy()
        zr[mg.core_nodes] += uplift_rate*dt
        frr.run_one_step()
        lake.map_depressions()
        spr.run_one_step(dt, flooded_nodes=lake.lake_at_node)
        keep_running = np.mean(np.abs(zr - zr_last)) >= end_thresh
        ti += dt
        A = mg.at_node['drainage_area']#[not_edge]
        A = A.reshape(ncells_side, ncells_side)
        S = mg.at_node['topographic__steepest_slope']
        S = S.reshape(ncells_side, ncells_side)
        #print ti/1000., 'kyr elapsed; ', np.mean(zr-zr_last) / dt * 1E6, \
        #      'um/yr surface uplift'
        
    print "Convergence reached! Landscape is at steady state."
    model_zmax[i] = np.max(zr)
    model_slope_area_relationship[i] = np.mean(A[2:-2]**m_sp * S[2:-2]**n_sp)
    i += 1

# Let's compare this against data
zdata = np.loadtxt('Synthetic_data/z.txt')
model_data_comparison_z = np.abs((model_zmax - np.max(zdata))/np.max(zdata))

fig = plt.figure()
ax = plt.plot(K_sps, model_data_comparison_z, 'ko-')
plt.ylabel('Misfit based on max(z)', fontsize=16)
plt.xlabel('K_{sp}', fontsize=16)

winning_point = (model_data_comparison_z == np.min(model_data_comparison_z)).nonzero()
winning_K_sp = float(K_sps[winning_point[0]])
plt.tight_layout()

print('Estimated K_sp from z =', winning_K_sp)

# Let's compare this against data
Sdata = np.loadtxt('Synthetic_data/S.txt')
Adata = np.loadtxt('Synthetic_data/A.txt')
model_data_comparison_SA = np.abs((model_slope_area_relationship - np.mean(Adata[2:-2]**m_sp * Sdata[2:-2]**n_sp)))

fig = plt.figure()
ax = plt.plot(K_sps, model_data_comparison_SA, 'ko-')
plt.title('Misfit based on S^{0.5} A', fontsize=16)
plt.xlabel('K_{sp}', fontsize=16)
plt.tight_layout()

winning_point = (model_data_comparison_SA == np.min(model_data_comparison_SA)).nonzero()
winning_K_sp = float(K_sps[winning_point[0]])

print('Estimated K_sp from S**0.5 * A**1 =', winning_K_sp)


