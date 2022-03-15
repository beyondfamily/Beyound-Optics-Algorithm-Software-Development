import numpy as np
import random
import pylab as plt
import math

def awgn(y, snr):
    x = np.copy(y)
    if isinstance(x[0], complex) == True:
        snr = 10 ** (snr / 10.0)
        xpower_real = np.sum(x.real ** 2) / len(x)
        npower_real = xpower_real / snr
        x.real = np.random.randn(len(x)) * np.sqrt(npower_real) + x.real
        xpower_imag = np.sum(x.imag ** 2) / len(x)
        npower_imag = xpower_imag / snr
        x.imag = np.random.randn(len(x)) * np.sqrt(npower_imag) + x.imag
        return x
    else:
        snr = 10 ** (snr / 10.0)
        xpower = np.sum(x ** 2) / len(x)
        npower = xpower / snr
        return np.random.randn(len(x)) * np.sqrt(npower) + x
