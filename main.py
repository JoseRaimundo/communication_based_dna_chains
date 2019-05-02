import numpy as np
import math
import random

# Transmitter-receiver distance from 0μm to 50μm and a frequency spectrum from 0Hz to 1kHz
def genereteDistance(particle_max):
    result = []
    for i in range(particle_max):
        ##randon
        ##result.append(random.uniform(0.1,1) * 10**-6)
        ##range
        result.append(i * 10**-9)
    return  np.array(result)

# Return time arange
def genereteTime(total_time):
    # Retorna o tempo particionado em 1Khtz (frequencia da amostragem presente no artigo)
    return (np.arange(1,(total_time) + 1)/1000)

''' 
The diffusion coefficient is the one of calcium 
molecules diffusing in a biological environment 
(cellular cytoplasm, [11]) D ∼ 10 −6 m 2 sec −1
'''
#Return the diffusin coeficient
def getD():
    return (10.0**(-6))

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
    # Get cd
    cd = np.sqrt(getD()/getTd())
    
    for x in vec_x:
        if t < x/cd:
            vec_gd.append(0)
        else:
            vec_gd.append(np.exp(-(t/2*getTd()))*(np.cos(np.sqrt(t**2 - ((x/cd)**2)))/np.sqrt(t**2 - ((x/cd)**2))))
    return vec_gd

def getB():
    return np.fft.fft(gd())

'''The normalized gain ΓB(f) of the propagation module
B is the magnitude |B̃(f)| of the TFFT B̃(f) normalized
by its maximum value max f(|B̃(f)|)'''

def normalizeGain():
    return abs(getB())/(np.amax(abs(getB())))

def getPhaseB():
    b = getB()
    #return np.arctan(.imag/b.real)
    return np.arctan(b.real)

def getDelay():
    return -np.diff(getPhaseB())


# Time
total_time = 100
time_vec    = genereteTime(total_time)

#Distances
particle_max = 50
vec_x   = genereteDistance(particle_max)

ignore_key_y = 0
for time in time_vec:
    ignore_key_x = 0    
    if ignore_key_y < 10:
        ignore_key_y = 1 + ignore_key_y
    else:
        for i in getDelay():
            # ignorar a primeira linha X
            if ignore_key_x <= 0:
                ignore_key_x = ignore_key_x + 1
            else:
                print(abs(i), end=",")
        print()