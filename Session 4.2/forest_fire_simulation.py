# Simple CA simulator in Python
#
# *** Forest fire ***
#
# Copyright 2008-2012 Hiroki Sayama
# sayama@binghamton.edu

# Modified to run with Python 3

import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

import pylab as PL
import random as RD
import scipy as SP
import numpy as np

RD.seed()

width = 100
height = 100
initProb = 0.4
empty, tree, fire, char = range(4)

def p_value(val=0.4):
    global initProb
    initProb = val

def init():
    global time, config, nextConfig, char_density, fire_density

    time = 0

    config = SP.zeros([height, width])
    for x in range(width):
        for y in range(height):
            if RD.random() < initProb:
                state = tree
            else:
                state = empty
            config[y, x] = state
    config[height//2, width//2] = fire

    nextConfig = SP.zeros([height, width])

    char_density = [0] # by default, no trees have burned at t = 0
    fire_density = [np.where(config == fire)[0].size]

def draw():
    PL.cla()

    plt.title(f'Initial Density: {initProb}')

    ax = plt.subplot(1, 2, 1)
    PL.imshow(config, vmin = 0, vmax = 3, cmap = PL.cm.binary)

    ax = plt.subplot(1, 2, 2)
    PL.plot(fire_density, label='fire_density')
    PL.plot(char_density, label='char_density')
    plt.legend()

def step():
    global time, config, nextConfig

    time += 1

    for x in range(width):
        for y in range(height):
            state = config[y, x]
            if state == fire:
                state = char
            elif state == tree:
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if config[(y+dy)%height, (x+dx)%width] == fire:
                            state = fire
            nextConfig[y, x] = state

    config, nextConfig = nextConfig, config

    char_density.append(
        np.where(config == char)[0].size
    )

    fire_density.append(
        np.where(config == fire)[0].size
    )

import pycxsimulator
pycxsimulator.GUI(parameterSetters=[p_value]).start(func=[init,draw,step])