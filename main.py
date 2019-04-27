
import numpy as np
import matplotlib.pyplot as plt
import math
import random

import sympy as sy

# Transmitter-receiver distance from 0μm to 50μm and a frequency spectrum from 0Hz to 1kHz


# Generate random coordenates x, y, z
def genereteCoordinates():
    vec_coordinates = []
    for i in range(particle_max):
        coordinates = []
        for j in range(dimensions):
            coordinates.append(random.uniform(0,  0.0000001))
        vec_coordinates.append(coordinates)
        print(coordinates)
    return vec_coordinates




''' 
The diffusion coefficient is the one of calcium molecules 
diffusing in a biological environment 
(cellular cytoplasm, [11]) D ∼ 10 −6 m 2 sec −1
'''
#Return the diffusin coeficient
def getD():
    # D ∼ 10^(−6) * m^2 * sec^(−1)
    m = 1
    return ((10.0**(-6)) * (m**2) * (math.sinh(1)**-1))
    

'''
The relaxation time τd from Eq. (21) 
is set approximatively to the relaxation 
time computed for water molecules: 
τd ∼ 10 −9 sec.
'''
# Return the relaxation time
def getTd():
    return ((10.0**(-9)) * (math.sinh(1)))


# Return the inpuse response
def getG(t, x):  
    x_dist = np.linalg.norm(x)
    cd = math.sqrt(getD()/getTd())
    division_element =  math.sqrt(t**2 - ((x_dist/cd)**2))
    return [(t-(x_dist/cd))*(np.exp(-(t/2*getTd())))*(math.cos(division_element)/division_element)]


def normalizedGain():
    return 0

# Return the delay τB(f) of the propagation module B
# def getTb():
#     np.arctan(
#     return 0


def getB():
    result = []

    for xr in vec_x:
        output = np.fft.fft(getG(time, xr))
        result.append(output)
    
    return result

# Variable for configurations
particle_max = 50
dimensions = 3
range_scale = 10

# A multidimensional vector of distance from the transmitter and cd
vec_x = genereteCoordinates()
time = 1
result = getB()


for saida in result:
    print(saida)