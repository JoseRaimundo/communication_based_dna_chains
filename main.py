import numpy as np
import math
import random

# Transmitter-receiver distance from 0μm to 50μm and a frequency spectrum from 0Hz to 1kHz
def genereteCoordinates(particle_max):
    dimensions = 3
    vec_coordinates = []
    for i in range(particle_max):
        coordinates = []
        for j in range(dimensions):
            coordinates.append(random.uniform(0,  0.00000001))
        
        vec_coordinates.append(np.array(coordinates))
    return np.array(vec_coordinates)

''' 
The diffusion coefficient is the one of calcium 
molecules diffusing in a biological environment 
(cellular cytoplasm, [11]) D ∼ 10 −6 m 2 sec −1
'''
#Return the diffusin coeficient
def getD():
    m = 1.5 # See in [12]
    return ((10.0**(-6)) * (m**2) * (math.sinh(1)**-1))

'''
The relaxation time τd from Eq. (21) is 
set approximatively to the relaxation time 
computed for water molecules: τd ∼ 10 −9 sec.
'''
# Return the relaxation time
def getTd():
    return ((10.0**(-9)) * (math.sinh(1)))

'''
The TFFT B̃(f ) of the signal propagation module is the
Fourier transform of the Green’s function g d (x̄, t)
'''
# Return the inpuse response
def gd(t, x):  
    # Get the Euclidian Distance
    x_dist = []
    cont = 0
    for distance in x:
        x_dist.append(abs(np.linalg.norm(distance)))
    
    x_dist = np.array(x_dist)

    # Get cd
    cd = np.sqrt(getD()/getTd())
    division_element =  np.sqrt(t**2 - ((x_dist/cd)**2))
    return (t-(x_dist/cd))*(np.exp(-(t/2*getTd())))*(np.cos(division_element)/division_element)

def getB():
    return np.fft.fft(gd(time, vec_x))

'''The normalized gain ΓB(f) of the propagation module
B is the magnitude |B̃(f)| of the TFFT B̃(f) normalized
by its maximum value max f(|B̃(f)|)'''

def normalizeGain():
    return abs(getB())/abs(np.amax(getB()))

def getPhaseB():
    #return getB()
    return np.arctan(getB().real/getB().imag)

def delayCalculation():
    return -np.diff(getPhaseB())

# Variable for configurations
particle_max = 50
# Time
time = 2

# A multidimensional vector of distance from the transmitter and cd
vec_x = genereteCoordinates(particle_max)
print(delayCalculation())
