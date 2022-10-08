from HW6_BiotSavart import *
import numpy as np
import matplotlib.pyplot as plt
radius = 1 # m
current = 1 # A

# Set up the wire grid
ngrid = 500
deltatheta = 2*np.pi/ngrid
wiregrid = []
for i in range(ngrid):
    theta = i*deltatheta
    wiregrid.append([radius*np.cos(theta), radius*np.sin(theta), 0])
    
# Check the wire grid
ax = plt.axes(projection='3d')
ax.scatter3D(np.array(wiregrid)[:,0], np.array(wiregrid)[:,1], np.array(wiregrid)[:,2])

# Check that B is azimuthally symmetric at the second ring
print(HW6_BiotSavart([0, 1, 2], wiregrid, current))
print(HW6_BiotSavart([0, -1, 2], wiregrid, current))
print(HW6_BiotSavart([1, 0, 2], wiregrid, current))
print(HW6_BiotSavart([-1, 0, 2], wiregrid, current))

# Compute the flux
flux = 0
rgrid = np.linspace(0, radius, 5)
for i in range(1, len(rgrid)):
    # Get the radial range
    rlo, rhi = rgrid[i-1], rgrid[i]
    rmid = (rhi + rlo)/2
   
    # Compute the area of the ring
    area = np.pi*(rhi**2 - rlo**2)    
    
    # Compute the field and flux
    Br = HW6_BiotSavart([0, rmid, 2], wiregrid, current)
    flux = flux + area*Br[2]

print(flux)
