import math
import random
import numpy 
import matplotlib.pyplot as plt

# Variables aleatorias Continuas

def normal(mu=0.5, sigma=0.1, lamb=0.1):
    while True:
        y1 = -(1 / lamb)*math.log(random.random())
        y2 = -(1 / lamb)*math.log(random.random())
        if y2 -((y1-1)**2)/2 > 0:
            y = y2 -((y1-1)**2)/2
            u = random.random()
            if u <= 0.5:
                return mu + sigma * y1
            else:
                return mu - sigma * y1

def F(fi, p):
    ac = 0
    for i in range(0, len(fi)):
        ac = ac + p[i] * fi[i]()
    return ac

a = numpy.zeros(1000)

LENGTH = 50

functions = [normal] * LENGTH

jumps = numpy.linspace(0, 1, num=LENGTH)

# make sure the sum is between 0 and 1
for i in range(LENGTH):
    jumps[i] = jumps[i]/LENGTH * 2


# run the program
for i in range(0, 1000):
    a[i] = F(functions, jumps)

# plot it
plt.hist(a/1000)
plt.show()