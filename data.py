import random

# Transmitter-receiver distance from 0μm to 50μm and a frequency spectrum from 0Hz to 1kHz
def genereteCoordinates(particle_max):
    dimensions = 3
    vec_coordinates = []
    for i in range(particle_max):
        coordinates = []
        for j in range(dimensions):
            coordinates.append(random.uniform(0,  0.00000001))
        vec_coordinates.append(coordinates)
    return vec_coordinates