import numpy as np
import random
import pylab as plt
import math


def qam4demod(x):
    x_real = x.real
    x_imag = x.imag
    angle = math.atan2(x_real, x_imag)
    if 0 < angle < math.pi / 2:
        x = math.sqrt(2)/2 + math.sqrt(2)/2j
    elif math.pi/2 < angle < math.pi:
        x = -math.sqrt(2)/2 + math.sqrt(2)/2j
    elif -math.pi < angle < -math.pi/2:
        x = -math.sqrt(2)/2 - math.sqrt(2)/2j
    else: x = math.sqrt(2)/2 - math.sqrt(2)/2j
    return x

print(qam4demod(complex(1,-1)))