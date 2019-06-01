import numpy as np
import math
import csv
import os

# Transmitter-receiver distance from 0μm to 50μm and a frequency spectrum from 0Hz to 1kHz
def genereteDistance(particle_max = 50e-12):
    return np.arange(0,particle_max, particle_max/50)

# Return time arange
def genereteTime(total_time = 1e-8):
    return (np.arange(0,total_time, total_time/220))

# Return the frequency spectrum from 0 Hz to 1kHz
def getFrequency(frequecy_max = 1e3, N = 0):
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
    return -(np.diff(phiB)/np.diff(2*np.pi*getFrequency(N = phiB.size)))


# Apaga arquivos de dados antigos
def cleanFile():
    dir = os.listdir()
    for file in dir:
        if file == "data_delay.csv":
            os.remove(file)
        elif file == "data_gain.csv":
            os.remove(file)

# Time
time_vec  = genereteTime()

#Distances
vec_x   = genereteDistance()


temp_delay = []
temp_gain = []
chave = True

data_delay = [] 
data_gain = [] 
for distance in vec_x:
    if chave:
        chave = False
        temp_delay = getDelay()+ 0.0005
        temp_gain  = normalizeGain()
    else:
        temp_delay = temp_delay + getDelay() + 0.0005
        temp_gain  = temp_gain + normalizeGain() 
    
    data_delay.append(temp_delay)
    data_gain.append(temp_gain)


# Apagando arquivos csv antigos
cleanFile()


data_delay =    np.transpose(np.asarray(data_delay))
data_gain   =   np.transpose(np.asarray(data_gain))


# Salva  dados do delay direto em um csv
with open('data_delay.csv', mode='w') as delay_file:
    file_writer = csv.writer(delay_file, delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    for i in data_delay:
        file_writer.writerow(i)

# Salva  dados do ganho direto em um csv
with open('data_gain.csv', mode='w') as gain_file:
    file_writer = csv.writer(gain_file, delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    for i in data_gain:
        file_writer.writerow(i)



