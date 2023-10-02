#!/usr/bin/env python


from scipy.integrate import newton_cotes
import numpy as np


def f(x):
    return np.sin(x)


a = 0
b = np.pi

exact = 2

if __name__ == "__main__":
    for N in [2, 4, 6, 8, 10]:
        x = np.linspace(a, b, N + 1)
        an, B = newton_cotes(N, 1)
        dx = (b - a) / N
        quad = dx * np.sum(an * f(x))
        error = abs(quad - exact)
        print("{:2d}  {:10.9f}  {:.5e}".format(N, quad, error))

