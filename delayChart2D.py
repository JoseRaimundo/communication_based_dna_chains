import matplotlib.pyplot as plt
import numpy as np
from matplotlib import *
import sys
from pylab import *
from pylab import rcParams

def dnaChart2D():
    data = np.genfromtxt('data_delay2d.csv',delimiter=',')
    dataOriginal = np.genfromtxt('data_delay2dOriginal.csv',delimiter=',')

    y1 = np.asarray(data[:,10]) 
    # y2 = np.asarray(data[:,20]) 
    y3 = np.asarray(data[:,30]) 
    # y4 = np.asarray(data[:,40]) 
    y5 = np.asarray(data[:,49]) 

    x1 = np.asarray(dataOriginal[:,10]) 
    x2 = np.asarray(dataOriginal[:,30]) 
    x3 = np.asarray(dataOriginal[:,49]) 

    rcParams['axes.xmargin'] = 0
    rcParams['axes.ymargin'] = 0

    # plt
    plot(y1, linewidth=1, label='Present paper, X ≃ 10μm')
    plot(y3, linewidth=1, label='Present paper, X ≃ 30μm')
    plot(y5, linewidth=1, label='Present paper, X ≃ 50μm')

    plot(x1, linewidth=1, linestyle = '--', label='Obtained by [6], X ≃ 10μm')
    plot(x2, linewidth=1, linestyle = '--', label='Obtained by [6], X ≃ 30μm')
    plot(x3, linewidth=1, linestyle = '--', label='Obtained by [6], X ≃ 50μm')
    # plt.title(r'erser $\alpha > \beta$')
    plt.title('Delay curves for D ≃ 114')

    plt.legend( loc=1)
    plt.grid(b=True, which='major', color='#A9F5F2')

    plt.xlabel('Frequency [x10 Hz]')
    plt.ylabel('Delay [s]')
    plt.show()


