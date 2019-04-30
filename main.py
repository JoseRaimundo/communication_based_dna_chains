import numpy as np
import math
import random

# Transmitter-receiver distance from 0μm to 50μm and a frequency spectrum from 0Hz to 1kHz
def genereteDistance(particle_max):
    return np.array(abs(np.random.rand(particle_max)*10**-6))


def genereteTime(particle_max):
    return np.arange(1,51)

''' time
The diffusion coefficient is the one of calcium 
molecules diffusing in a biological environment 
(cellular cytoplasm, [11]) D ∼ 10 −6 m 2 sec −1
'''
#Return the diffusin coeficient
def getD():
    return ((10.0**(-6)))

'''
The relaxation time τd from Eq. (21) is 
set approximatively to the relaxation time 
computed for water molecules: τd ∼ 10 −9 sec.
'''
# Return the relaxation time
def getTd():
    return (10.0**(-9))
 
'''
The TFFT B̃(f ) of the signal propagation module is the
Fourier transform of the Green’s function g d (x̄, t)
'''
# Return the inpuse response
def gd():  
    t = time
    # print(t)
    vec_gd = []
    # Get the Euclidian Distance
    x_dist = vec_x
    # Get cd
    cd = np.sqrt(getD()/getTd())
    
    for x in x_dist:
        if t < x/cd:
            vec_gd.append(0)
        else:
            division_element =  np.sqrt(t**2 - ((x/cd)**2))
            vec_gd.append(np.exp(-(t/2*getTd()))*(np.cos(division_element)/division_element))
   
    return vec_gd

def getB():
    return np.fft.fft(gd())

'''The normalized gain ΓB(f) of the propagation module
B is the magnitude |B̃(f)| of the TFFT B̃(f) normalized
by its maximum value max f(|B̃(f)|)'''

def normalizeGain():
    return abs(getB())/(np.amax(abs(getB())))

def getPhaseB():
    return np.arctan(getB().real)
    
def delayCalculation():
    return -np.diff(getPhaseB())

# Variable for configurations
particle_max = 50
# Time
# time = 1
time_vec    = genereteTime(particle_max)
# A multidimensional vector of distance from the transmitter and cd
vec_x   = genereteDistance(particle_max)

# print(delayCalculation())

for time in time_vec:
    # delayCalculation()
    print(delayCalculation())
    
