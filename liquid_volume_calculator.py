# Please write a function that calculates liquid volume in a sphere using the following formula.
# The radius r  is always 10, so consider making it a default parameter.
# V = (4 * pi * r^3)/3 - (pi * hc^2 * (3 * r - hc))/3

# Solution
from math import pi


def liquid_volume(hc, r=10):
    V = (4 * pi * r ** 3) / 3 - (pi * hc ** 2 * (3 * r - hc)) / 3
    return V


print(liquid_volume(2))
