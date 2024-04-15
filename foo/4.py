import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colorbar import ColorbarBase
from matplotlib.colors import Normalize
from matplotlib.patches import Circle


def circle(x, y, r):
    # x and y are the coordinates of the center of the circle
    # r is the radius of the circle
    # 0.01 is the angle step, bigger values will draw the circle faster but
    # you might notice imperfections (not very smooth)
    ang = np.linspace(0, 2 * np.pi, 100)
    xp = r * np.cos(ang)
    yp = r * np.sin(ang)
    plt.plot(x + xp, y + yp, color="gray")


def C_analytical(x, y, t):
    mdot = 1  # kg/s
    D = 10**-3
    L = 1
    outer_term = mdot / (
        4 * np.pi * t * np.sqrt(D**2 + 1e-10)
    )  # Avoid division by zero
    exp_sum = 0

    for m in range(-20, 21):
        for n in range(-20, 21):
            term1 = -((x + n * L) ** 2) / (4 * D * t + 1e-10)  # Avoid division by zero
            term2 = -((y + m * L) ** 2) / (4 * D * t + 1e-10)  # Avoid division by zero
            exp_sum += np.exp(term1 + term2)

    return outer_term * exp_sum


domain = np.arange(-0.5, 0.51, 0.005)
X, Y = np.meshgrid(domain, domain)
Z = np.zeros_like(X)
cmap = plt.cm.hot
outfile = "aaa.gif"
t_vals = np.arange(0, 201, 4)
D = 10**-3

for t in range(len(t_vals)):
    for i in range(len(domain)):
        for j in range(len(domain)):
            x = domain[i]
            y = domain[j]
            Z[i, j] = C_analytical(x, y, t_vals[t])

    plt.figure()
    hp = plt.pcolor(X, Y, Z, cmap=cmap)
    hp.set_edgecolor("none")
    plt.axis("square")
    plt.clim(0.0, 2.0)
    hc = ColorbarBase(plt.gca(), cmap=cmap, norm=Normalize(vmin=0.0, vmax=2.0))
    hc.set_label("Concentration (kg/m^3)")
    plt.xlabel("X (m)")
    plt.ylabel("Y (m)")
    plt.title(f"Diffusion of Point Source in a Box (t={t_vals[t]}s)")
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)

    for m in range(-20, 21):
        for n in range(-20, 21):
            circle(n, m, 3 * np.sqrt(2 * D * t_vals[t]))

    # gif utilities
    plt.gca().set_facecolor("w")
    plt.draw()
    plt.savefig("frame.png")
    plt.close()
