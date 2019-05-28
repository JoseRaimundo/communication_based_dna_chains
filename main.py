import numpy as np
import math

# Transmitter-receiver distance from 0μm to 50μm and a frequency spectrum from 0Hz to 1kHz
def genereteDistance(particle_max):
    return np.arange(0,particle_max, particle_max/50)

# Return time arange
def genereteTime(total_time):
    # Retorna o tempo particionado em 1kHz (frequencia da amostragem presente no artigo)
    #x_r+total_time/10000
    return (np.arange(0,total_time, total_time/220))

# Return the frequency spectrum from 0 Hz to 1kHz
def getFrequency(frequecy_max, N):
    return np.arange(0, frequecy_max, frequecy_max/N)

''' 
The diffusion coefficient is the one of calcium 
molecules diffusing in a biological environment 
(cellular cytoplasm, [11]) D ∼ 10 −6 m 2 sec −1
'''
#Return the diffusin coeficient
def getD():
    return (10**(-6))

'''
The relaxation time τd from Eq. (21) is 
set approximatively to the relaxation time 
computed for water molecules: τd ∼ 10 −9 sec.
'''
# Return the relaxation time
def getTd():
    return (10**(-9))

'''
The TFFT B̃(f ) of the signal propagation module is the
Fourier transform of the Green’s function g d (x̄, t)
'''
# Return the inpuse response
def gd():
    x = distance
    vec_gd = []
    # Get cd
    cd = np.sqrt(getD()/getTd())

    for t in time_vec:
        # print("t ", t)
        # print("x ", abs(x)/cd)
        if t <= abs(x)/cd:
            # print("x c = ", abs(x)/cd)
            # print("t c = ", t)
            continue
        #     #vec_gd.append(0)
        else:
            # print(">>>>>>>>>>>>> 1")
            # print("x = ", abs(x)/cd)
            # print("t = ", t)
            # print("Argumento = ", -(t/(2*getTd())))
            # print("Exponencial = ", np.exp(-(t/(2*getTd()))))
            # print("Arg cosh = ", t**2 - (abs(x)/cd)**2)
            # print("Cosh = ", np.cosh(np.sqrt(t**2 - (abs(x)/cd)**2)/(2*getTd())))
          
            # print("Raiz arg = ", np.cosh(np.sqrt(t**2 - (abs(x)/cd)**2)/(2*getTd())))
            # print(">>>>>>>>>>>>> 2")
            gd_temp = np.exp(-t/(2*getTd()))*(
                        (np.cosh(np.sqrt(t**2 - (abs(x)/cd)**2)/(2*getTd())))/
                        np.sqrt(t**2 - (abs(x)/cd)**2)
                        )
            vec_gd.append(gd_temp)
                
            #print("Gd = ",gd_temp)
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
    
def getPhaseB():
    b = getB()
    b = b[0:int(b.size/2)]
    #freq = np.fft.fftfreq(b.size, d=0.1)
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
    return np.asarray(phaseB)#, freq

def getDelay():
    #phiB, f = getPhaseB()
    phiB = getPhaseB()
    # return -(np.diff(phiB))/np.diff(f)
    #return -np.diff(getPhaseB())

    return -(np.diff(phiB)/np.diff(2*np.pi*getFrequency(frequecy_max, phiB.size)))

# Time
total_time = 1e-8
time_vec    = genereteTime(total_time)
#print(time_vec)

# Frequency
frequecy_max = 1e3

#Distances
particle_max = 50e-12
vec_x   = genereteDistance(particle_max)
#print(max(vec_x))
teste = []
chave = True

#
# vec_x = np.flip(vec_x, 0)
# print(vec_x)
data = [] 
for distance in vec_x:
    if chave:
        chave = False
        teste = getDelay()+ 0.0005
    else:
        teste = teste + getDelay() + 0.0005
    # teste = getDelay()
    data.append(teste)
    # for i in teste:
    #     #i=0
    #     print(i, end=",")
    # print()

data = np.transpose(np.asarray(data))
for i in data:
    for j in i:
        print(j, end=",")
    print()