import matplotlib.pyplot as plt
import numpy as np



def dnaChart2D():
    data = np.genfromtxt('data.csv',delimiter=',')
    
    fig = plt.figure() 

    
    y1 = []
    y2 = []
    y3 = []

        
    y1.append(data[0])
    y1.append(data[2])
    y1.append(data[3])
    
    y2.append(data[4])
    y2.append(data[5])
    y2.append(data[6])
    
    y3.append(data[7])
    y3.append(data[8])
    y3.append(data[9])

    x = np.linspace(0, 1, len(data[9]))

    yn = (y1,y2, y3)
    COLORS = ('b','g','r')

    for i,jy in enumerate(yn):
        cont = 0
        ax = fig.add_subplot(len(yn),1,i+1)
        for y in jy:
            ax.plot(x, y, ls='solid', color=COLORS[cont]) 

            if i != len(yn) - 1:
                # all but last 
                ax.set_xticklabels( () )
            else:
                for tick in ax.xaxis.get_major_ticks():
                    tick.label.set_fontsize(14) 
                    # specify integer or one of preset strings, e.g.
                    #tick.label.set_fontsize('x-small') 
                    tick.label.set_rotation('vertical')
            cont = cont + 1
   
   

    fig.suptitle('Matplotlib xticklabels Example')
    plt.xlabel('Frequency [x10 Hz]')
    plt.ylabel('Delay [s]')
    plt.show()

if __name__ == '__main__':
    dnaChart2D()