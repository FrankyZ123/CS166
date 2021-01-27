import matplotlib
matplotlib.use('TkAgg')
from pylab import *

n = 100 # size of space: n x n

def p_value(val=0.1):
    global p
    p = val

def initialize():
    global config, nextconfig, density
    config = zeros([n, n])
    for x in range(n):
        for y in range(n):
            config[x, y] = 1 if random() < p else 0
    nextconfig = zeros([n, n])
    density = [sum(config) / n**2]
    
def observe():
    global config, nextconfig, density
    cla()
    
    plt.title(p)

    ax = plt.subplot(1, 2, 1)
    imshow(config, vmin = 0, vmax = 1, cmap = cm.binary)

    ax = plt.subplot(1, 2, 2)
    plot(density)

def update():
    global config, nextconfig, density
    for x in range(n):
        for y in range(n):
            count = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    count += config[(x + dx) % n, (y + dy) % n]
            nextconfig[x, y] = 1 if count >= 4 else 0
    config, nextconfig = nextconfig, config
    density.append(sum(config) / n**2)

import pycxsimulator
pycxsimulator.GUI(parameterSetters=[p_value]).start(func=[initialize, observe, update])