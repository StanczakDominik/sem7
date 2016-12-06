""" Przepływ cieczy **nielepkiej** wokół nieskończonego cylindra
z regulowaną cyrkulacją $\gamma$"""

import numpy as np
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("gamma_factor", nargs="?", default = 1, help="multiple of 4 pi U a")
args = parser.parse_args()
a = 1
U = 1
gamma_factor = float(args.gamma_factor)

gamma = gamma_factor * 4 * np.pi * U * a
y_stagnant = -gamma / (4 * np.pi * U)
if y_stagnant < -a:
    x_stagnant = [0, 0]
else:
    x_stagnant = np.array([-1, 1])* (a**2-y_stagnant**2)**0.5

x = y = np.linspace(-3, 3, 300)
X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2 + Y**2)
THETA = np.arctan2(Y, X)

UR = U *(1 - a**2 / R**2) * np.cos(THETA)
UTHETA = -U * (1 + a**2 / R**2) * np.sin(THETA) - gamma/(2*np.pi * R)

UX = UR * np.cos(THETA) - UTHETA * np.sin(THETA)
UY = UR * np.sin(UTHETA) + UTHETA * np.cos(THETA)

c = R <= a*0.99

# theta = np.linspace(0, 2*np.pi, 100)
#
# xball, yball = a*np.cos(theta), a*np.sin(theta)
UX[c] = 0
UY[c] = 0

# plt.plot(xball,yball, "k-")
fig, ax = plt.subplots()
ax.plot(x_stagnant, y_stagnant*np.ones(2), "ro")
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.streamplot(X, Y, UX, UY, color=np.sqrt(UX**2 + UY**2))
c1 = plt.Circle((0,0),a)
ax.add_artist(c1)
plt.show()
