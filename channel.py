import numpy as np
import math

# Transmitter-receiver distance from 0μm to 50μm and a frequency spectrum from 0Hz to 1kHz
def genereteDistance(particle_max):
    return np.arange(0,particle_max, particle_max/50)

#  Retorna o tempo particionado em 1kHz (frequencia da amostragem presente no artigo)
def genereteTime(total_time):
    return (np.arange(0,total_time, total_time/220))

# Return the frequency spectrum from 0 Hz to 1kHz
def getFrequency(frequecy_max, N):
    return np.arange(0, frequecy_max, frequecy_max/N)

#Return the diffusin coeficient
def getD():
    return (10**(-6))

# Return the relaxation time
def getTd():
    return (10**(-9))

# Return the inpuse response
def gd():
    x = distance
    vec_gd = []
    # Get cd
    cd = np.sqrt(getD()/getTd())

    for t in time_vec:
        if t <= abs(x)/cd:
            continue
        else:
            gd_temp = np.exp(-t/(2*getTd()))*(
                        (np.cosh(np.sqrt(t**2 - (abs(x)/cd)**2)/(2*getTd())))/
                        np.sqrt(t**2 - (abs(x)/cd)**2)
                        )
            vec_gd.append(gd_temp)
    return vec_gd

def getB():
    return np.fft.fft(gd())


def normalizeGain():
    b = getB()
    return 10*np.log10(abs(b[0:int(b.size/2)])/(np.amax(abs(b[0:int(b.size/2)]))))
    
def getPhaseB():
    b = getB()
    b = b[0:int(b.size/2)]
    phaseB = []
    for real, imaginary in zip(b.real, b.imag):
        if real == 0 and imaginary>0:
            phaseB.append(np.pi/2)
        elif real == 0 and imaginary<0:
            phaseB.append(-np.pi/2)
        elif real == 0 and imaginary==0:
            phaseB.append(0)
        else:
            phaseB.append(np.arctan(imaginary/real))
    return np.asarray(phaseB)

def getDelay():
    phiB = getPhaseB()

    return -(np.diff(phiB)/np.diff(2*np.pi*getFrequency(frequecy_max, phiB.size)))

# Time
total_time = 1e-8
time_vec    = genereteTime(total_time)

# Frequency
frequecy_max = 1e3

#Distances
particle_max = 50e-12
vec_x   = genereteDistance(particle_max)
teste = []
chave = True

data = [] 
for distance in vec_x:
    if chave:
        chave = False
        teste = getDelay()+ 0.0005
    else:
        teste = teste + getDelay() + 0.0005
    data.append(teste)


data = np.transpose(np.asarray(data))
for i in data:
    for j in i:
        print(j, end=",")
    print()