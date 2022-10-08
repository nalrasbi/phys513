from HW6_BiotSavart import *
import numpy as np
import matplotlib.pyplot as plt
# Field from a wire along the y-axis

def Btrue_straightwire(current, r):
    mu0 = 1.256e-6
    return mu0*current/(2*np.pi*r)
# Set up the wire grid
ymin, ymax, ngrid = 0, 100, 20000

wiregrid = []
delta = (ymax - ymin)/ngrid
for i in range(ngrid):
    yval = ymin + i*delta
    wiregrid.append([0, yval, 0])
# Set up the point P. I am making a grid becuase I am going to plot B(r)
py = (ymax-ymin)/2
rgrid = np.arange(0.05, 10, 0.05)

# Solve numerically for the field
I = 1

Bnum = []
for r in rgrid:
    Bnum.append(HW6_BiotSavart([0, py, r], wiregrid, I))
    
# Plot
plt.figure()
plt.semilogy(rgrid, Btrue_straightwire(I, rgrid), '-k', label="Analytic")
plt.semilogy(rgrid, np.array(Bnum)[:,0], '--r', label="Numerical")
plt.xlabel("Radial distance at y=50 [m]")
plt.ylabel(r"$B_x$ [T]")
plt.title(r"$B_x$ [T] VS Radial distance at y=50 [m] ")
plt.legend()

# Move the origin and check the field at r=1m
p = [2, 5, 3]
wiregrid = [
    [2,2,2],
    [2,3,2],
    [2,4,2],
    [2,5,2],
    [2,6,2],
    [2,7,2],
    [2,8,2]
]
I = 1

print("Numerical: ", HW6_BiotSavart(p, wiregrid, I))
print("Analytic: ", Btrue_straightwire(I, 1))

# Field at the center of a ring of current in the x-y plane

def Btrue_ring(current, radius):
    mu0 = 1.256e-6
    return mu0*current/(2*radius)

# Set up the wire problem

p = [0, 0, 0]

r = 1
ngrid = 50
deltatheta = 2*np.pi/ngrid
wiregrid = []
for i in range(ngrid):
    theta = i*deltatheta
    wiregrid.append([r*np.cos(theta), r*np.sin(theta), 0])
    
# Check the wire grid

plt.figure()
plt.plot(np.array(wiregrid)[:,0], np.array(wiregrid)[:,1], 'ok')
plt.gca().set_aspect('equal', adjustable='box')

# Grid is defined CCW which is the direction a positive current flows

I = 1

# Find Check the solution, should be positive-z direction for positive current

print("Numerical: ", HW6_BiotSavart(p, wiregrid, I))
print("Analytic: ", Btrue_ring(I, r))