import math
import numpy as np

#Return the diffusin coeficient
def getD():
    D = 0.01
    return D


# Return the relaxation time
def getTd():
    Td = 0.01
    return Td

# The step function
def getU():
    return t-(vec_x/cd)

# Return the inpuse response
def getG():  
    division_element = math.sqrt(t**2 - ((vec_x/cd)**2))
    return getU()*(e**(-(t/2*getTd())))*(math.cos(division_element)/division_element)
     


# the wavefront speed
cd = math.sqrt(getD()/getTd())

# A multidimensional vector of distance from the transmitter and cd
vec_x = 0

vec_time = 0

t = 0


# Test
print(getG())
