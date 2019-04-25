import math



time_vec


#Return the diffusin coeficient
def getD():
    D = 0.01
    return D


# Return the relaxation time
def getTd():
    Td = 0.01
    return Td

# Ignore
# The step function
def getU(t, vec_x, cd):
    return t-(vec_x/cd)


def getG():
    cd = math.sqrt(getD()/getTd())

    division_element = math.sqrt(t**2 - ((vec_x/cd)**2))))

    Gd = (t-(vec_x/cd))*(e**(-(t/2*getTd())))*(math.cos(division_element)/division_element)


# Dimension
n_dim = 1


# A vector multidimensional
vec_x = ?
