
from math import sqrt
from collections import namedtuple

Coordenadas = namedtuple('Coordenadas', 'latitud, longitud')

def calcular_distancia(coord1, coord2):

    return sqrt( (coord2.latitud-coord1.latitud)**2 + (coord2.longitud-coord1.longitud)**2 )

def calcular_media_coordenadas(coordenadas):
    latitud = 0
    longitud = 0

    for n in coordenadas:
        latitud +=n.latitud
        longitud += n.longitud
    
    return Coordenadas(latitud,longitud)