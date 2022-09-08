import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Set constants


def charge(x, y, q, loc):
    xp, yp = loc
    s3 = ((x-xp)**2 + (y-yp)**2)**(1.5)
    Ex = q*(x-xp)/s3
    Ey = q*(y-yp)/s3
    return Ex, Ey

def dipole(x, y, q1, q2, loc1, loc2):
    E1x, E1y = charge(x, y, q1, loc1)
    E2x, E2y = charge(x, y, q2, loc2)
    Ex = E1x+E2x
    Ey = E1y+E2y
    E = (Ex**2 + Ey**2)**(1/2)
    return Ex/E, Ey/E

def rhs(s, pos, d):
    q1, loc1 = 1, [d, 0]
    q2, loc2 = -1, [-d, 0]
    x, y = pos
    return dipole(x, y, q1, q2, loc1, loc2)
def termination_event(s, pos, _):
    return (pos[0]+1) + pos[1]
termination_event.terminal = True
termination_event.direction = 1

# Set up the problem
d = 1.0

# Plot some field lines every 15 degrees
tgrid = np.arange(0, 20000, 0.01)

for theta in np.arange(40, 340, 20):
    # Compute the starting position of the line to draw
    offset = 0.001
    xoffset = offset*np.cos(theta*np.pi/180)
    yoffset = offset*np.sin(theta*np.pi/180)

    sol = solve_ivp(rhs, [min(tgrid),max(tgrid)], [d+xoffset, yoffset], args=[d], t_eval=tgrid, events=termination_event)
    plt.plot(sol.y[0], sol.y[1])

# Plot the charges
plt.plot([d, -d], [0,0], 'ok')
plt.xlabel("X Plane")
plt.ylabel("Y plane")
plt.title("Field Lines for a dipole")
plt.savefig("HW1_3.pdf", bbox_inches=[])
