import numpy as np
import matplotlib.pyplot as plt

# Define constants
Vs = 1.0 
lambda1 = 10
lambda2 = lambda1/2
lambda3 = lambda1/3

delta1 = lambda1
delta2 = 3*lambda2/4

Z01 = 1 
Z02 = Z01/2
Z03 = Z01/3

V1p = Vs
V2p = -5*Vs*(1+1j)/(7*np.sqrt(2))
V3p = -4*Vs*(1+1j)/(7*np.sqrt(2))

rho1 = 1j/7
rho2 = -1/5

beta1 = 2*np.pi/lambda1
beta2 = 2*np.pi/lambda2
beta3 = 2*np.pi/lambda3

def V1(x):
    return V1p*(np.exp(-1j*beta1*x) + rho1*np.exp(1j*beta1*x))
def I1(x):
    return (V1p/Z01)*(np.exp(-1j*beta1*x) - rho1*np.exp(1j*beta1*x))

def V2(x):
    return V2p*(np.exp(-1j*beta2*x) + rho2*np.exp(1j*beta2*x))
def I2(x):
    return (V2p/Z02)*(np.exp(-1j*beta2*x) - rho2*np.exp(1j*beta2*x))

def V3(x):
    return V3p*np.exp(-1j*beta3*x)
def I3(x):
    return (V3p/Z03)*np.exp(-1j*beta3*x)

def voltage(x):
    if x >= 0:
        return V3(x)
    elif -delta2 <= x < 0:
        return V2(x)
    elif -(delta1+delta2) <= x < -delta2:
        return V1(x)
    else:
        return 0
    
def current(x):
    if x >= 0:
        return I3(x)
    elif -delta2 <= x < 0:
        return I2(x)
    elif -(delta1+delta2) <= x < -delta2:
        return I1(x)
    else:
        return 0

# Voltage plot
xlist = np.arange(-(delta1+delta2), 10, .02)
vlist = np.array([voltage(xi) for xi in xlist])
plt.figure()
plt.plot(xlist, np.abs(vlist))
plt.title(r"$|V(x)|/|V_s|$ VS x(cm)")
plt.ylabel(r"$|V(x)|/|V_s|$")
plt.xlabel("x (cm)")
plt.axvline(-delta2, color='k', linestyle='--', linewidth=1)
plt.axvline(0, color='k', linestyle='--', linewidth=1)

# Voltage/Current plot
plt.figure()
xlist = np.arange(-(delta1+delta2), 10, .02)
vlist = np.array([voltage(xi) for xi in xlist])
ilist = np.array([current(xi) for xi in xlist])
plt.plot(xlist, np.abs(vlist)/np.abs(ilist))
plt.title(r"Normalized to $Z_{01}$")
plt.ylabel(r"$|V(x)|/|I(x)|$")
plt.xlabel("x (cm)")
plt.axvline(-delta2, color='k', linestyle='--', linewidth=1)
plt.axvline(0, color='k', linestyle='--', linewidth=1)

