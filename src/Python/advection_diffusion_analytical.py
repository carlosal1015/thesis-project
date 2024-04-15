#!/usr/bin/env python

"""
Uses the Python CAS (SymPy) to calculate the derivatives from advection-diffusion PDE.

    ∂u/∂t - ∂²u/∂x² = 0

[1] https://core.ac.uk/download/pdf/42967717.pdf
[2] https://en.wikipedia.org/wiki/False_diffusion
[3] https://en.wikipedia.org/wiki/Numerical_dispersion
[4] https://en.wikipedia.org/wiki/Numerical_diffusion  
"""
from sympy import Derivative as D
from sympy import Eq, Function, symbols, exp

x, t, c, v, alpha, beta = symbols("x, t, c, v, alpha, beta")
U = symbols("U", cls=Function)(x, t)
V = symbols("V", cls=Function)(x, t)
advection = D(U, t) + c * D(U, x)
diffusion = v * D(U, x, 2)
advection_diffusion_equation = Eq(advection, diffusion)

_U = V * exp(alpha * x + beta * t)
U_t = D(_U, t).simplify()
U_x = D(_U, x).simplify()
U_xx = D(_U, x, 2).simplify()

V_0 = advection_diffusion_equation.subs({t: 0})

print(U_t)
print(U_x)
print(U_xx)
# print(advection_diffusion_equation)
