import numpy as np
import matplotlib.pyplot as plt

a = 7 / 8
z = -5 / 8
delta = 0.005
alpha = 8
beta = np.log(2) / (36 * np.power(delta, 2))


def G(x, beta, z):
    return np.exp(-beta * np.power(x - z, 2))


def F(x, alpha, a):
    return np.sqrt(np.maximum(1 - np.power(alpha * (x - a), 2), np.zeros_like(0)))


dx = 1e-3
xl_1 = np.linspace(-1, -0.75, 25)
xref_1 = np.arange(-0.75 + dx, -0.5, dx)
xr_1 = np.linspace(-0.5, -0.25, 25)
x_1 = np.concatenate([xl_1, xref_1, xr_1])

xl_2 = np.linspace(-0.25, 0.25, 25)
xref_2 = np.arange(0.25 + dx, 0.5, dx)
x_2 = np.concatenate([xl_2, xref_2])

xl_3 = np.linspace(0.5, 0.75, 25)
xref_3 = np.arange(0.75 + dx, 1, dx)
x_3 = np.concatenate([xl_3, xref_3])

x = np.concatenate([x_1, x_2, x_3])
# x = np.linspace(start=-1, stop=1)

u_0 = np.piecewise(
    x=x,
    condlist=[
        (x >= -0.75) & (x <= -0.5),
        (x >= -0.25) & (x <= 0),
        (x >= 0.25) & (x <= 0.5),
        (x >= 0.75) & (x <= 1),
    ],
    funclist=[
        lambda x: 1
        / 6
        * (G(x, beta, z - delta) + G(x, beta, z + delta) + 4 * G(x, beta, z)),
        1,
        lambda x: 1 - np.absolute(8 * (x - 3 / 8)),
        lambda x: 1
        / 6
        * (F(x, alpha, a - delta) + F(x, alpha, a + delta) + 4 * F(x, alpha, z)),
        0,
    ],
)


fig, ax = plt.subplots(layout="constrained")
ax.plot(x, u_0, linewidth=0.75)
ax.set_ylim(-0.2, 1.2)
ax.set_title("Initial condition $u_{0}(x)$")
plt.savefig("initial condition.png")
