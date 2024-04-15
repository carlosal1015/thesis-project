import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

plt.rcParams["figure.autolayout"] = True
plt.rcParams["figure.dpi"] = 750
plt.rcParams["font.family"] = "serif"
plt.rcParams["text.usetex"] = True
plt.rcParams[
    "text.latex.preamble"
] = """
\\usepackage{siunitx}
\\usepackage{fourier}
"""
plt.style.use("seaborn-v0_8-dark")
# Define our constants.
R_, p_ = 0.01, 0.00


# NOTE: Define our differential equations.
def F(z, phi) -> list:
    x, y = z
    denominator = R_**2 * x * y + x * p_ - np.sin(phi)
    dx = (x * np.cos(phi)) / denominator
    dy = (x * np.sin(phi)) / denominator
    return [dx, dy]


# Set our initial conditions.
# NOTE: We cannot set them to 0.0, otherwise we get a division by zero error.
z_initial = [1e-5, 1e-5]  # x(0), y(0)

n = 2 * (10**3)
phi_vals = np.linspace(0, np.deg2rad(99), n)

MIN_TOLERANCE = 1e-9
solutions = sp.integrate.odeint(
    F,
    z_initial,
    phi_vals,
    atol=MIN_TOLERANCE,
    rtol=MIN_TOLERANCE,
)

X_PHI, Y_PHI = "x\left(\\varphi\\right)", "y\left(\\varphi\\right)"
x_vals, y_vals = solutions[:, 0], solutions[:, 1]
plt.plot(x_vals, y_vals, label=f"${Y_PHI}$ against ${X_PHI}$")
plt.title(
    "Plot of water droplet governed by parametric equations "
    + f"$\left[ {X_PHI}, {Y_PHI} \\right]$"
)
plt.xlabel(f"${X_PHI}$")
plt.ylabel(f"${Y_PHI}$")
plt.ticklabel_format(style="sci", axis="both", scilimits=(0, 0), useMathText=True)
plt.legend(loc="best")
plt.savefig("foo.pdf")
