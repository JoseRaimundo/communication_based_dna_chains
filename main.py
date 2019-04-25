import math
import numpy as np
import random


def genereteCoordenates():
    vec_coordinates = []
    for i in range(particle_max):
        coordinates = []
        coordinates.append(random.uniform(0,  1))
        coordinates.append(random.uniform(0,  1))
        coordinates.append(random.uniform(0,  1))
        vec_coordinates.append(coordinates)
    return vec_coordinates



#Return the diffusin coeficient
def getD():
    # D ∼ 10^(−6) * m^2 * sec^(−1)
    D = 0.000001
    return D
    
# Return the relaxation time
def getTd():
    Td = 0.0000011
    return Td

# Return the inpuse response
def getG(x):  
    cd = math.sqrt(getD()/getTd())
    division_element =  math.sqrt(t**2 - ((x/cd)**2))
    return (t-(x/cd))*(np.exp(-(t/2*getTd())))*(math.cos(division_element)/division_element)


# Variable for configurations
particle_max = 50
dimensions = 3
range_scale = 10

# A multidimensional vector of distance from the transmitter and cd
vec_x = genereteCoordenates()

# the wavefront speed

t = 2


for x in vec_x:
    # ! Calcular distância Euclidiana de x
    x_dist = np.linalg.norm(x)
   # output = np.fft.fft(getG(x[0]))

    
    output = getG(x_dist)
    print(output)






