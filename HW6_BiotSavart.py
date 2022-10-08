import numpy as np

def HW6_BiotSavart(point, wire, current): 
    point = np.asarray(point)
    wire = np.asarray(wire)
    prefactor = 1.256e-6 * current / (4 * np.pi)
  
    B = 0
    for i in range(len(wire)):
        Rvec = point - wire[i]
        Ri = np.sqrt(np.sum(Rvec**2))
        if i == len(wire)-1:
            Lvec = wire[i] - wire[i-1]
        else:
            Lvec = wire[i+1] - wire[i]
        B= B+np.cross(Lvec, Rvec)/Ri**3
    
    return prefactor*B