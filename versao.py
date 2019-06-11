
import numpy as np
import math
import csv

#distancias
particle_max = 50e-6
distancias = np.arange(0,particle_max, particle_max/50)

#tempos
temp = np.arange(0, 2, 1/1000)
tempo = []
for t, i in zip(temp, range(2000)):
  if i%10 == 0:
    tempo.append(t)

frequecy_max = 1e3
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
    vec_gd = []
    # Get cd
    cd = np.sqrt(getD()/getTd())

    for t in tempo:
        if t <= abs(x)/cd:
            continue
        else:
       
            gd_temp = (
                        (np.cosh(np.sqrt(t**2 - (abs(x)/cd)**2)))/
                            np.sqrt(t**2 - (abs(x)/cd)**2)
                        )
            vec_gd.append(gd_temp)
                
            #print("Gd = ",gd_temp)
                
    # print("Gd = ",vec_gd)
    # print("Gd = ",len(vec_gd))
    return vec_gd


 

def getB():
    return np.fft.fft(gd())

'''The normalized gain ΓB(f) of the propagation module
B is the magnitude |B̃(f)| of the TFFT B̃(f) normalized
by its maximum value max f(|B̃(f)|)'''

def normalizeGain():
    b = getB()
    return 10*np.log10(abs(b[0:int(b.size/2)])/(np.amax(abs(b[0:int(b.size/2)]))))
    #return (abs(b.size)/(np.amax(abs(b))))
    
# def getPhaseB():
#     b = getB()
#     b = b[int(b.size/2):b.size]
#     #freq = np.fft.fftfreq(b.size, d=0.1)
#     phaseB = []
#     for real, imaginary in zip(b.real, b.imag):
#         if real == 0 and imaginary>0:
#             phaseB.append(np.pi/2)
#         elif real == 0 and imaginary<0:
#             phaseB.append(-np.pi/2)
#         elif real == 0 and imaginary==0:
#             phaseB.append(0)
#         else:
#             phaseB.append(np.arctan(imaginary/real))
#     return np.asarray(phaseB)#, freq

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

teste = []
chave = True
data = [] 
for x in distancias:
    if chave:
        chave = False
        teste = getDelay() + 0.0005
    else:
        teste = teste + getDelay() + 0.0005
    data.append(teste)


data = np.transpose(np.asarray(data))

with open('data.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    for i in data:
        employee_writer.writerow(i)