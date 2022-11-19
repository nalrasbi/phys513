import numpy as np
import matplotlib.pyplot as plt


# Define constants

N = 100
w = 1e6
L = 0.1e-3/N
C = 1e-6/N
ZL = np.sqrt(L/C)

# Calculate the equivalent impedance 

Zequiv = ZL
for i in range(N):
    Zequiv = (1j*w*L + Zequiv)/(1 - w**2*L*C + 1j*w*C*Zequiv)

V0 = 1.
I0 = V0/Zequiv

# Loop to iteratively find the current and voltage

Vn = [V0]
In = [I0]

for i in range(N):
    In.append(In[-1] - 1j*w*C*Vn[-1])
    Vn.append(Vn[-1] - 1j*w*L*In[-1])

Vn = np.array(Vn)
In = np.array(In)

# Plot

plt.figure()
plt.plot(np.abs(Vn), '.k')
plt.xlabel('Number of nodes')
plt.ylabel(f'$|V_n|$')
plt.title(f'$|V_n|$''   VS Number of nodes' )

plt.figure()
plt.plot(np.abs(In), '.k')
plt.xlabel('Number of nodes')
plt.ylabel(f'$|I_n|$')
plt.title(f'$|I_n|$''   VS Number of nodes' )

plt.figure()
plt.plot(np.abs(Vn/In)/ZL, '.k')
plt.xlabel('Number of nodes')
plt.ylabel(f'$|Z_n|/Z_L$')
plt.title(f'$|Z_n|/Z_L$''   VS Number of nodes')

