import matplotlib.pyplot as plt
import numpy as np
from matplotlib import *
import sys
from pylab import *
from pylab import rcParams

def dnaChart2D():
    # data = np.genfromtxt('data_delay2d.csv',delimiter=',')
    dataOriginal = np.genfromtxt('data/data_delay2dOriginal.csv',delimiter=',')
    # N = 144
    # D = 3.629
    a = np.genfromtxt('data/data_delay2d114.csv',delimiter=',')
    # N = 58
    # D = 5.366
    b = np.genfromtxt('data/data_delay2d58.csv',delimiter=',')
    # N = 36
    # D = 7.100
    c = np.genfromtxt('data/data_delay2d36.csv',delimiter=',')

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


    # y1 = np.asarray(data[:,10]) 
    # print(distancias)
    # y2 = np.asarray(data[:,20]) 
    # y3 = np.asarray(data[:,30]) 
    # y4 = np.asarray(data[:,40]) 
    # y5 = np.asarray(data[:,49]) 

    # x1 = np.asarray(dataOriginal[:,10]) 
    # x2 = np.asarray(dataOriginal[:,30]) 
    # x3 = np.asarray(dataOriginal[:,49]) 

   

    
    # # plt
    # plot(y1, linewidth=1, label='D ≃ ' + str(N_1) + '^-11, X = 10μm')
    # plot(y3, linewidth=1, label='D ≃ ' + str(N_1) + '^-11, X = 30μm')
    # plot(y5, linewidth=1, label='D ≃ ' + str(N_1) + '^-11, X = 50μm')

    # plot(x1, linewidth=1, linestyle = '--', label='D ≃ 10^-6, X = 10μm')
    # plot(x2, linewidth=1, linestyle = '--', label='D ≃ 10^-6, X = 30μm')
    # plot(x3, linewidth=1, linestyle = '--', label='D ≃ 10^-6, X = 50μm')
    # # plt.title(r'erser $\alpha > \beta$')
    # # plt.title('Comparação entre a proposta e  o [6]')

    plt.legend( loc=1)
    plt.grid(b=True, which='major', color='#A9F5F2')
    # xlim(0, 30)
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Delay [s]')
    plt.show()


