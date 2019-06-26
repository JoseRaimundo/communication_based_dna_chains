import math
import numpy as np
import random
# import data
# print(data.genereteCoordinates(1))

# particle_max = 50
# dimensions = 3
# range_scale = 10

# vec_coordinates = []


# for i in range(particle_max):
#     coordinates = []
#     coordinates.append(random.uniform(0,  1))
#     coordinates.append(random.uniform(0,  1))
#     coordinates.append(random.uniform(0,  1))
#     vec_coordinates.append(coordinates) 
# #     print(saida) # [69, 47, 43, 64, 16]
# print("teste")
# # t = np.arange(100)
# # # sp = np.fft.fft(np.sin(t))
# # # print(np.sin(t))

# # print(np.sin(t))
# for saida in vec_coordinates:
#     print(saida)

# x = (0, 0, 0)
# y = (8, 9, 9)
# distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))
# print("Euclidean distance from x to y: ",distance)

# x_dist = np.linalg.norm(y)
# print("Euclidean x_dist   from x to y: ",x_dist)
# output = np.fft.fft(getG(x[0]))

# print((10.0**(-6))* (1**2) * (math.sinh(1)**-1))



# print(1/1000000000)

# import numpy as np
# import matplotlib.pyplot as plt

# plt.style.use('ggplot')

# c = 100 * 10**(-6)
# v = 5
# r = 2000

# t = np.linspace(0,1,1000)

# q = c*v*(1-np.exp((-1/(r*c))*t))
# i = (v/r)*np.exp((-1/(r*c))*t)

# plt.plot([0,t[-1]],[c*v,c*v],label='Charge peak')
# plt.plot(t,q,label='Charge of the capacitor (C)')
# plt.plot(t,i,label='Current (A)')

# print('Tau',1/(r*c))
# print('Peak current (A)',v/r)

# plt.xlabel('Time (s)')
# plt.title('RC circuit')
# plt.legend()
# plt.show()


# a = 2.3
# print(a.real)

# print(a.imag)
# print(a)

# print(np.arctan(x))
# print(x)
# print(abs(x))




import numpy as np
# b = [0, 1, 2]
# a = np.array(b)

# a = a**2
# print(a/2)

# np.cos(2)

# print(np.arange(1,51))

# a = np.arange(1,10)
# b = np.arange(1,10)

# for i, t in zip(a, b):
#     print("i = ", i)
#     print("t = ", t)

# print(np.random.rand(50)*10**-6)
# import random

# result = []
# for i in range(50):
#     result.append(random.uniform(0.1,1) * 10**-6)
    
# result = np.array(result)
# print(result)

# array = np.array([[(1*10**-12), 2, 3], [4, 5, 6], [7, 8, 9]])
# print(array)
# print(np.fft.rfft(array))

# a =  np.array([[1,2,3, 7, 2, 3]])
# # print(np.amax(a))



# print((np.arange(1,(1001*2))/1000))
# print("italo")
# print(np.arange(0, 50*10**-6, 50*10**-8))
# print("z")
# print((np.arange(0, 50)*10**-6))

# teste = np.array([1, 2, 3])
# teste = np.flip(teste, 0)
# print(teste)



#####3 Plotagem em 2D

# import matplotlib.pyplot as plt
# import plotly.offline as py
# import plotly.graph_objs as go
# import pandas as pd
# import numpy as np


# data = np.genfromtxt('data.csv',delimiter=' ')

# tamanhos = [1, 2, 3]
# cont = 0
# for d in data:
#     frequency = np.linspace(0, 1, len(d))
#     plt.plot(frequency, d, label="Tamanho " + str(tamanhos[cont]), linewidth=1)
#     plt.legend(loc='upper right')
#     cont = cont + 1

# plt.xlabel('Frequency [x10 Hz]')
# plt.ylabel('Delay [s]')
# plt.show()


# import csv

# data = np.genfromtxt('data.csv',delimiter=',')
# print(data)
# with open('data.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=' ')

    # for row in csv_reader:
    #     print(row)
    #     print("..............")

# def contar (valor=11, caractere="+"):
#   for i in range(1,valor):
#     print(caractere)
# contar()
# print("Passando um caractere diferente:")
# contar()
print("Com N = 114", ((5.9e-10)*(114.698**-0.588)))
print("Com N = 58", ((5.9e-10)*(58.977**-0.588)))
print("Com N = 36", (5.9e-10)*(36.635**-0.588))