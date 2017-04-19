import numpy as np
from landlab import RasterModelGrid, HexModelGrid
from landlab.components import StreamPowerEroder, FlowRouter, \
    PrecipitationDistribution, LinearDiffuser, DepressionFinderAndRouter
from landlab import imshow_grid
from copy import deepcopy
from matplotlib import pyplot as plt

plt.ion()

# Change these
uplift_rate = 0.001
K_sp = 2E-4
K_hs = 0.1
ncells_side = 50 # number of raster cells on each side
dxy  = 500 # side length for raster model cells [m]

# Choose 1 model grid
mg = RasterModelGrid((ncells_side, ncells_side), dxy)

# More advanced options
dt = 1000# * np.ones(tmax/10)
end_thresh = uplift_rate * dt / 1E3 # Difference in cell elevations between time-steps
m_sp = 0.5
n_sp = 1.

title_text = '$K_{sp}$='+str(K_sp) + '; $K_{hs}$='+str(K_hs) + '; $t_{max}$='+str(K_hs) + '; $dx$='+str(dxy)

gridlist = []

# add initial noise to produce convergent flow from the initial conditions
np.random.seed(91) # so our figures are reproducible
mg_noise = np.random.rand(mg.number_of_nodes)/1000.

# set up the input fields
zr = mg.add_zeros('node', 'topographic__elevation')
zr += mg_noise

# Landlab sets fixed elevation boundary conditions by default. This is
# what we want, so we will not modify these here.

# instantiate the components:
frr = FlowRouter(mg) # water__unit_flux_in gets automatically ingested
spr = StreamPowerEroder(mg, K_sp=K_sp, m_sp=m_sp, n_sp=n_sp, threshold_sp=0,
                        use_Q=None)
lake = DepressionFinderAndRouter(mg)
    
# Hillslopes
dfn = LinearDiffuser(mg, linear_diffusivity=K_hs)

zr_last = -9999
keep_running = np.mean(np.abs(zr - zr_last)) >= end_thresh
ti = 0
while keep_running:
    zr_last = zr.copy()
    zr[mg.core_nodes] += uplift_rate*dt
    #dfn.run_one_step(dt) # hillslopes always diffusive, even when dry
    frr.run_one_step()
    lake.map_depressions()
    spr.run_one_step(dt, flooded_nodes=lake.lake_at_node)
    keep_running = np.mean(np.abs(zr - zr_last)) >= end_thresh
    ti += dt
    print ti/1000., 'kyr elapsed; ', np.mean(zr-zr_last) / dt * 1E6, \
          'um/yr surface uplift'
print "Convergence reached! Landscape is at steady state."

A = mg.at_node['drainage_area']#[not_edge]
A = A.reshape(ncells_side, ncells_side)
S = mg.at_node['topographic__steepest_slope']
S = S.reshape(ncells_side, ncells_side)

np.savetxt('Synthetic_data/z.txt', zr, fmt='%.2f')
np.savetxt('Synthetic_data/A.txt', A, fmt='%d')
np.savetxt('Synthetic_data/S.txt', S, fmt='%.5f')

# Do some plotting. First the topography:
plt.figure('topo ')
imshow_grid(mg, 'topographic__elevation', grid_units=('m', 'm'),
                var_name='Elevation (m)')
#plt.title(title_text)
plt.tight_layout()

#edge = np.unique(mg.neighbors_at_node[mg.boundary_nodes, :])
#not_edge = np.in1d(mg.nodes.flatten(), edge, assume_unique=True,
#                       invert=True)

plt.savefig('Synthetic_data/topo.png')

# Inner cells for slope--area diagram
plt.figure('S-A')
plt.loglog(A[5:-5, 5:-5],
           S[5:-5, 5:-5], 'kx')
#xlim([1.e3, 1.e7])
plt.ylabel('Topographic slope', fontsize=16)
plt.xlabel('Drainage area (m^2)', fontsize=16)
#plt.title(title_text)
plt.tight_layout()

plt.show()

