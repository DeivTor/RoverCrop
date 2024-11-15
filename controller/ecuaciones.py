import numpy as np
import math as m
import matplotlib.pylab as plb
import matplotlib.mlab as mlb
import matplotlib.pyplot as plt


class funcionVelocidad:

    def _init(self):  # Cambiado a __init_
        self.ruta = []

    def calcularVelocidad(self, terreno):
        if terreno == "Limoso":
            t = np.linspace(0, 0.25, 1000)
            p = 66.67
            K = 2963.8
            Vf = 1
            A = Vf * (K / p)
            exp = -p * t
            w = A * (1 - np.exp(exp))
            r = 0.1
            v = w * r
            velocidad = int(v.ptp())
            print(velocidad)

        elif terreno == "Franco":
            t = np.linspace(0, 0.25, 1000)
            p = 66.67
            K = 2963.8
            Vf = 2
            A = Vf * (K / p)
            exp = -p * t
            w = A * (1 - np.exp(exp))
            r = 0.1
            v = w * r
            velocidad = int(v.ptp())
            
        return velocidad
    
    def establecerRuta(self, velocidad):
        if velocidad <= 5:
            self.ruta = [
                {'direction': 'right', 'steps': 50},
                {'direction': 'down', 'steps': 20},
                {'direction': 'left', 'steps': 30},
                {'direction': 'up', 'steps': 40},
                {'direction': 'right', 'steps': 50},
                {'direction': 'down', 'steps': 20},
                {'direction': 'left', 'steps': 30},
                {'direction': 'up', 'steps': 40},
            ]
        elif velocidad <=9:
            self.ruta = [{'direction': 'right', 'steps': 50},
                        {'direction': 'down', 'steps': 20},
                        {'direction': 'left', 'steps': 30},
                        {'direction': 'up', 'steps': 40},
                        {'direction': 'right', 'steps': 50},
                        {'direction': 'down', 'steps': 20},
                        {'direction': 'left', 'steps': 30},
                    
            ] 
        else:
            print("Velocidad fuera del rango esperado.")
            return velocidad

        return self.ruta
    
   

    


