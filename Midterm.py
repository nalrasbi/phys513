import numpy as np
import matplotlib.pyplot as plt

# Constants
eps0 = 8.85e-12
V0 = 1
a = 1
rho0 = V0*eps0/a**2
rboundary = 2*a
smallnumber = 0.00001
maxitr = 100000


# Set up the rgrid
rmin, rmax = a, 3*a
deltar = a/3

rgrid = np.arange(rmin, rmax+smallnumber, deltar)

# Set up the V grid with boundary conditions

Vgrid = np.ones(len(rgrid))
for i in range(len(Vgrid)):
    Vgrid[i] = i*V0/(len(Vgrid)-1)
    
# Calculate Potential

for i in range(maxitr):
    Vtemp = np.copy(Vgrid)
    for i in range(1, len(rgrid)-1):
        if np.abs(rgrid[i]-rboundary) < smallnumber:
            Vgrid[i] = (2*Vgrid[i+1] + Vgrid[i-1])/3.0
        elif rgrid[i] < rboundary:
            Vgrid[i] = 0.5*Vgrid[i+1]*(deltar/rgrid[i] + 1.0) \
                        + 0.5*Vgrid[i-1]*(1.0 - deltar/rgrid[i]) \
                        - rho0*deltar**2/(2*eps0)
        else:
            Vgrid[i] = 0.5*Vgrid[i+1]*(deltar/rgrid[i] + 1.0) \
                        + 0.5*Vgrid[i-1]*(1.0 - deltar/rgrid[i])
    
    # Check for convergence
    if np.max(np.abs((Vtemp-Vgrid)/Vgrid)) < 0.001:
        break

# Analytic
rgrid_analytic1 = np.linspace(rmin, rboundary, 100)
rgrid_analytic2 = np.linspace(rboundary, rmax, 100)

A1 = 12*a*V0/7 - (rho0*a**3/eps0)*(26/21)

# print(A1)
Vanalytic1 = (rho0/(6*eps0))*(rgrid_analytic1**2 - a**2) + A1*(1/a - 1/rgrid_analytic1)
Vanalytic2 = V0 + (6*a*V0 - 3*rho0*a**3/eps0 - 3*A1)*(1/(3*a) - 1/rgrid_analytic2)

# Plot
plt.figure()
plt.plot([0,a], [0,0], '-c')
plt.plot(rgrid_analytic1, Vanalytic1, '-c', label='Analytic')
plt.plot(rgrid_analytic2, Vanalytic2, '-c')
plt.plot([3*a,3*a,4*a], [Vanalytic2[-1],0,0], '-c')
plt.plot(rgrid, Vgrid, 'ok', label='Numeric')
plt.legend(loc=2)
plt.xlabel("Radius (m)")
plt.ylabel("Electric Potential (V)")
plt.title("Electric Potential (V) VS Radius (m)")

# print(Vgrid)