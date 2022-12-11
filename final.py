import numpy as np
import matplotlib.pyplot as plt

# Define constants

Vg = 1
L1 = 0.1e-3
C1 = 1e-6
L2 = 0.4e-3
C2 = 1e-6
l = 1
w = 1e6
R = 40
Nsteps = 2000

# Exact solution

def Vexact(x):
    beta1 = w*np.sqrt(L1*C1)
    beta2 = w*np.sqrt(L2*C2)
    
    rho1 = (1 + np.exp(-2j*beta2*l))/(3*np.exp(-2j*beta1*l) + (1/3)*np.exp(-2j*(beta1+beta2)*l))
    rho2 = 1/3
    
    V1p = Vg/(np.exp(2j*beta1*l) + rho1*np.exp(-2j*beta1*l))
    V2p = V1p*(np.exp(1j*beta1*l) + rho1*np.exp(-1j*beta1*l))/(np.exp(1j*beta2*l) + rho2*np.exp(-1j*beta2*l))
    
    if -2 <= x < -1:
        return V1p*(np.exp(-1j*beta1*x) + rho1*np.exp(1j*beta1*x))
    elif -1 <= x <= 0:
        return V2p*(np.exp(-1j*beta2*x) + rho2*np.exp(1j*beta2*x))
    else:
        return 0

# Approximate solution

xgrid = np.linspace(-2, 0, Nsteps)

# Divide L and C into N/2 steps

L1a = L1/(Nsteps/2)
C1a = C1/(Nsteps/2)
L2a = L2/(Nsteps/2)
C2a = C2/(Nsteps/2)

# Calculate the equivalent impedance (from hw10)

Zequiv = R
for i in range(int(Nsteps/2)):
    Zequiv = (1j*w*L2a + Zequiv)/(1 - w**2*L2a*C2a + 1j*w*C2a*Zequiv)
for i in range(int(Nsteps/2)):
    Zequiv = (1j*w*L1a + Zequiv)/(1 - w**2*L1a*C1a + 1j*w*C1a*Zequiv)

Va = [Vg]
Ia = [Vg/Zequiv]

# Calculate ladder network

for i in range(1, Nsteps):
    if xgrid[i] < -1.0:
        Ia.append(Ia[-1] - 1j*w*C1a*Va[-1])
        Va.append(Va[-1] - 1j*w*L1a*Ia[-1])
    else:
        Ia.append(Ia[-1] - 1j*w*C2a*Va[-1])
        Va.append(Va[-1] - 1j*w*L2a*Ia[-1])

Va = np.array(Va)
Ia = np.array(Ia)

# Plot

plt.figure()
xlist = np.arange(-2, 0, .001)
Vexactlist = np.array([Vexact(xi) for xi in xlist])
plt.plot(xlist, np.abs(Vexactlist), '-k', label='Exact Solution')
plt.plot(xgrid, np.abs(Va), '--c', label='Approx Solution')
plt.xlabel("x Position (meters)")
plt.ylabel(r"$|V(x)|$ (Volts)")
plt.legend()
plt.savefig('final-plot.pdf')