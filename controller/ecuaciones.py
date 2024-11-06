import numpy as np
import math as m
import matplotlib.pylab as plb
import matplotlib.mlab as mlb
import matplotlib.pyplot as plt

class funcionVelocidad:

    def __init__(self):
        self
        self.ruta = []
        

    def calcularVelocidad (self, terreno):
        if (terreno == "Limoso"):
            velocidad= 30
        elif(terreno == "Franco"):
            velocidad= 10
        return velocidad
    
    def establecerRuta (self, velocidad):
        if(velocidad == 10):
            self.ruta = [
                {'direction': 'right', 'steps': 50},
                {'direction': 'down', 'steps': 20},
                {'direction': 'left', 'steps': 30},
                {'direction': 'up', 'steps': 40},
            ]
        elif(velocidad==30):
            self.ruta=[
                {'direction': 'right', 'steps': 5},
                {'direction': 'down', 'steps': 5},
                {'direction': 'left', 'steps': 5},
                {'direction': 'up', 'steps': 5},
                {'direction': 'right', 'steps': 5},
                {'direction': 'down', 'steps': 5},
                {'direction': 'left', 'steps': 5},
                {'direction': 'up', 'steps': 5},
                {'direction': 'right', 'steps': 5},
                {'direction': 'down', 'steps': 5},
                {'direction': 'left', 'steps': 5},
                {'direction': 'up', 'steps': 5},
                {'direction': 'right', 'steps': 5},
                {'direction': 'down', 'steps': 5},
                {'direction': 'left', 'steps': 5},
                {'direction': 'up', 'steps': 5},
                {'direction': 'right', 'steps': 5},
                {'direction': 'down', 'steps': 5},
                {'direction': 'left', 'steps': 5},
                {'direction': 'up', 'steps': 5},
            ]
        return self.ruta

    
