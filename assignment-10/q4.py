# Take N (N >= 10) random 2-dimensional points represented in cartesian coordinate space.
# Store them in a numpy array. Convert them to polar coordinates.

import numpy as np
import math

def converter(x,y):
    r = round(math.sqrt(x**2 + y**2),2)
    theta = round(math.atan(y/x),2)
    return (r,theta)

x = np.linspace(0,100,num=20,dtype=int)
y = np.linspace(100,200,num=20,dtype=int)

plane = np.column_stack((x,y))

polar = []
for points in plane:
    polar.append(converter(points[0],points[1]))

print(polar)
