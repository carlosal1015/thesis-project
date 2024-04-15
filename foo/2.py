import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def circle(ax, x, y, r):
    ang = np.arange(0, 2*np.pi, 0.01)
    xp = r * np.cos(ang)
    yp = r * np.sin(ang)
    ax.plot(x + xp, y + yp, color=(0.75, 0.75, 0.75))

def C_analytical(x, y, t):
    mdot = 1  # kg/s
    D = 1e-3
    L = 1
    outer_term = mdot / (4 * np.pi * t * np.sqrt(D * D))
    exp_sum = 0

    for m in range(-20, 21):
        for n in range(-20, 21):
            term1 = -(x + n * L)**2 / (4 * D * t)
            term2 = -(y + m * L)**2 / (4 * D * t)
            exp_sum += np.exp(term1 + term2)

    return outer_term * exp_sum

domain = np.arange(-0.5, 0.505, 0.005)
X, Y = np.meshgrid(domain, domain)
Z = np.zeros_like(X)

cmap = plt.cm.hot
cmap = cmap[::-1][:, [2, 1, 0]]

outfile = 'aaa.gif'
t_vals = np.arange(0, 201, 4)
D = 1e-3

fig, ax = plt.subplots()

def update(t):
    for i, x in enumerate(domain):
        for j, y in enumerate(domain):
            Z[i, j] = C_analytical(x, y, t)

    hp = ax.pcolormesh(X, Y, Z, shading='auto')
    ax.set_aspect('equal')
    hp.set_edgecolor('none')
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_xlabel('X (m)')
    ax.set_ylabel('Y (m)')
    ax.set_title(f'Diffusion of Point Source in a Box (t={t}s)')

    for m in range(-20, 21):
        for n in range(-20, 21):
            circle(ax, n, m, 3 * np.sqrt(2 * D * t))

    cbar = plt.colorbar(hp, ax=ax)
    cbar.set_label('Concentration (kg/m^3)')

    if t == 0:
        plt.savefig('initial_state.png')

update(0)  # Create an initial state image
ani = FuncAnimation(fig, update, frames=t_vals, repeat=False)

ani.save(outfile, writer='imagemagick', fps=5)

plt.show()
