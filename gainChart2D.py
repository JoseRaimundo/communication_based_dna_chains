import matplotlib.pyplot as plt
import numpy as np
from matplotlib import *
import sys
from pylab import *
from pylab import rcParams

def dnaChart2D():
    # data = np.genfromtxt('data_delay2d.csv',delimiter=',')
    dataOriginal = np.genfromtxt('data/data_ganho2dOriginal.csv',delimiter=',')
    # N = 144
    # D = 3.629
    a = np.genfromtxt('data/data_ganho2d114.csv',delimiter=',')
    # N = 58
    # D = 5.366
    b = np.genfromtxt('data/data_ganho2d58.csv',delimiter=',')
    # N = 36
    # D = 7.100
    c = np.genfromtxt('data/data_ganho2d36.csv',delimiter=',')

    distancias = [10, 30, 50]

    rcParams['axes.xmargin'] = 0
    rcParams['axes.ymargin'] = 0
    for d in distancias:
        plot(np.asarray(a[:,d]), linewidth=1,  linestyle = '--',label='D ≃ 3.629^-11, X = ' + str(d) + 'μm')

    for d in distancias:
        plot(np.asarray(b[:,d]), linewidth=1,linestyle = '--',   label='D ≃ 5.366^-11, X = ' + str(d) + 'μm')


    for d in distancias:
        plot(np.asarray(c[:,d]), linewidth=1, linestyle = '--', label='D ≃ 7.100^-11, X = ' + str(d) + 'μm')

    for d in distancias:
        plot(np.asarray(dataOriginal[:,d]), linewidth=1, label='D ≃ 10^-6, X = ' + str(d) + 'μm')

    plt.legend( loc=1)
    plt.grid(b=True, which='major', color='#A9F5F2')
    # xlim(0, 30)
    plt.xlabel('Frequency [x 10 Hz]')
    plt.ylabel('Gain [dBs]')
    plt.show()


