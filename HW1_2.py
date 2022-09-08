import numpy as np       
import matplotlib.pyplot as plt
# The analytic calculation
L = 1 # meters
Eye = 2/(np.sqrt(2)*L)
print("Exact Field =", Eye)

# The approximation
n = 5

delta = L/((n-1)//2)
prefactor = 2*L/n
Eya = 1/L**2

for i in range((n-1)//2):
    m = i + 1
    Eya += 2*L/((m*delta)**2 + L**2)**(1.5)

Eya = prefactor*Eya

print("Number of Charges", n)
print("Charge sep, delta =", delta)
print("Approximated Field =", Eya)
# Compute the error

found_1percent = False
nlist, errorlist = [], []
for k in range(1,250):
    n = 1 + 2*k
    
    # Compute the approximation
    delta = L/((n-1)//2)
    prefactor = 2*L/n
    Eya = 1/L**2
    
    for i in range((n-1)//2):
        m = i + 1
        Eya += 2*L/((m*delta)**2 + L**2)**(1.5)
    Eya = prefactor*Eya

    # Save the error and n for plotting
    nlist.append(n)
    error = (Eye - Eya)/Eye
    errorlist.append(error)
    
    # Find when we go under 1 percent error
    if error <= 0.01 and not found_1percent:
        print("Error below 1% with n =", n)
        found_1percent = True
plt.semilogy(nlist, errorlist, '-k')
plt.axhline(0.01, linestyle='--')
plt.xlabel("Number of charges")
plt.ylabel("Error")
plt.title("Error vs Number of charges ")

