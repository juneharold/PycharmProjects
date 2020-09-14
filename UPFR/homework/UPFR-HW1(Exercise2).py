import math
"""print(math.pi/4)"""

import random

"""random.seed(1)""" # Fixes the see of the random number generator.

def rand():
   # define `rand` here!
    return random.uniform(-1, 1)

def distance(x, y):
    return math.sqrt((x[0]-y[0])**2+(x[1]-y[1])**2)


def in_circle(x, origin = [0,0]):
   # Define your function here!
    if math.sqrt(x[0]**2 + x[1]**2) < 1:
        return True
    else:
        return False

# 2e
random.seed(1)
R = 10000
inside = []
for i in range(R):
    p = (rand(), rand())
    if in_circle(p) == True:
        inside.append(True)
    else:
        None

print(sum(inside))
print(sum(inside)/R)
print(math.pi/4 - sum(inside)/R)