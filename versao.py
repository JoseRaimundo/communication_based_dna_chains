import numpy as np
import math
import csv

#distancias
particle_max = 50e-6
distancias = np.arange(0,particle_max, particle_max/50)

#tempos
temp = np.arange(0, 2, 1/100000)
tempo = []
for t, i in zip(temp, range(2000)):
    if i%10 == 0:
        tempo.append(t)
print(len(tempo))
frequecy_max = 1e3
def getFrequency(frequecy_max, N):
    return np.arange(0, frequecy_max, frequecy_max/N)

#Return the diffusin coeficient
def getD():
    # return ((5.9e-10)*(114.698**-0.588))
    # return ((5.9e-10)*(58.977**-0.588))
    # return ((5.9e-10)*(36.635**-0.588))
    return (10**(-6))

# Return the relaxation time
def getTd():
    return (10e-9)

# Return the inpuse response
def gd():
    vec_gd = []
    # Get cd
    cd = np.sqrt(getD()/getTd())

    for t in tempo:
        if t <= abs(x)/cd:
            continue
        else:
            # print(t)
            # z = t 114.698
            # print("exp * cos  ", np.exp(-z)*np.cosh(z))
            # print("exp ", np.exp(-z/2))
            # print("cos ", np.cosh(np.sqrt(z**2 - (abs(x)/cd)**2)))
            gd_temp = np.exp(t/2)*((np.cosh(np.sqrt(t**2 - (abs(x)/cd)**2)))/np.sqrt(t**2 - (abs(x)/cd)**2))
            vec_gd.append(gd_temp)
            
    return vec_gd[0:190]

def getB():
    return np.fft.fft(gd())

def normalizeGain():
    b = getB()
    return 4*np.log10(abs(b[0:int(b.size/2)])/(np.amax(abs(b[0:int(b.size/2)]))))

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

constante = 0.0005

# Descomente essa parte para gerar os gráficos 2D
teste = []
chave = True
data = [] 
cont = 0
for x in distancias:
    delay = getDelay()
    if chave:
        chave = False
        teste = delay + constante
    else:
        teste = teste + delay + constante
    

    data.append(teste)

data = np.transpose(np.asarray(data))
data = data[1:12]
with open('data_delay2d.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    for i in data:
        employee_writer.writerow(i)

# Descomente essa parte para gerar os gráficos 3D do delay
# teste = []
# chave = True
# data = [] 
# for x in distancias:
#     if chave:
#         chave = False
#         teste = getDelay()+ constante
#     else:
#         teste = teste + getDelay() + constante
#     data.append(teste)

# data = np.transpose(np.asarray(data))

# with open('data_delay.csv', mode='w') as employee_file:
#     employee_writer = csv.writer(employee_file, delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
#     for i in data:
#         employee_writer.writerow(i)

# Descomente essa parte para gerar os gráficos 3D do ganho

# teste = []
# chave = True
# data = [] 
# for x in distancias:
#     if chave:
#         chave = False
#         teste = normalizeGain() + constante
#     else:
#         teste = teste + normalizeGain() + constante
#     data.append(teste)

# data = np.transpose(np.asarray(data))
# with open('data_gain.csv', mode='w') as employee_file:
#     employee_writer = csv.writer(employee_file, delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
#     for i in data:
#         employee_writer.writerow(i)
