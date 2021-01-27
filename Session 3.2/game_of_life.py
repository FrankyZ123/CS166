import matplotlib
matplotlib.use('TkAgg')
from pylab import *

n = 100 # size of space: n x n
p = 0.5 # probability of initially panicky individuals

def initialize():
    global config, nextconfig, density
    config = zeros([n, n])
    for x in range(n):
        for y in range(n):
            config[x, y] = 1 if random() < p else 0
    nextconfig = zeros([n, n])
    density = [sum(config)]
    
def observe():
    global config, nextconfig, density
    cla()

    ax = plt.subplot(1, 2, 1)
    imshow(config, vmin = 0, vmax = 1, cmap = cm.binary)

    ax = plt.subplot(1, 2, 2)
    plot(density)

def update():
    global config, nextconfig, density
    for x in range(n - 1):
        for y in range(n - 1):
            '''
                Given the neighborhood, only 4 neighbors need to be checked (x +- 1, y +- 1)
            '''

            current_state = config[x, y]

            left_index = n - 1 if x == 0 else x - 1
            right_index = 0 if x == n - 1 else x + 1
            upper_index = n - 1 if y == 0 else y + 1
            lower_index = 0 if y == n - 1 else y - 1
            
            # Check the neighborhood
            upper_neighbor = config[x, upper_index]
            lower_neighbor = config[x, lower_index]
            left_neighbor = config[left_index, y]
            right_neighbor = config[right_index, y]

            living_cells = upper_neighbor + lower_neighbor + left_neighbor + right_neighbor

            if current_state == 0 and living_cells == 3:
                current_state = 1
            elif current_state == 1 and living_cells not in [2, 3]:
                current_state = 0

            nextconfig[x, y] = current_state
    config, nextconfig = nextconfig, config
    density.append(sum(config))

import pycxsimulator
pycxsimulator.GUI().start(func=[initialize, observe, update])