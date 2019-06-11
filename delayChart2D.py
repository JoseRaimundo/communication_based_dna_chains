import matplotlib.pyplot as plt
import numpy as np
from matplotlib import *
import sys
from pylab import *
from pylab import rcParams


def dnaChart2D():
    data = np.genfromtxt('data_delay2d.csv',delimiter=',')

    y1 = np.asarray(data[:,10]) 
    y2 = np.asarray(data[:,20]) 
    y3 = np.asarray(data[:,30]) 
    y4 = np.asarray(data[:,40]) 
    y5 = np.asarray(data[:,49]) 

    rcParams['axes.xmargin'] = 0
    rcParams['axes.ymargin'] = 0
    print(data[:,50])

    plt.xlabel('Frequency [x10 Hz]')
    plot(y1, linewidth=1)
    plot(y2, linewidth=1)
    plot(y3,linewidth=1)
    plot(y4, linewidth=1)
    plot(y5, linewidth=1)
    plt.ylabel('Delay [s]')
    plt.show()


