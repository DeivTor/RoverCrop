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

            t = np.linspace(0, 0.25, 1000)
            p = 66.67
            K = 2963.8
            Vf = 1
            A = Vf*(K/p)
            exp = -p*t

            w = A*(1-pow(m.e,exp))

            r=0.1
            v = w * r
            velocidad = v.ptp()
            print(velocidad)

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
        elif(velocidad != 10 and velocidad !=30):
            print("Prueba con las ecuaciones.")
            
            return self.ruta

    


