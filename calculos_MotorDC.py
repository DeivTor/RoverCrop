import numpy as np
import math as m
import matplotlib.pylab as plb
import matplotlib.mlab as mlb
import matplotlib.pyplot as plt


#t es el tiempo de medición
#w es el valor de la velocidad angular del motor: rad/seg
#p es el polo no dominante del sistema
#K es la ganancia en bajas frecuencias del motor (valor máximo deseado de la función de transferencia en lazo abierto)
#Vf es la amplitud del voltaje que alimenta el motor


#Para las pruebas de simulación tomamos el siguiente motor DC
#https://pages.mtu.edu/~wjendres/ProductRealization1Course/Motor_Specs.pdf

t = np.linspace(0, 0.25, 1000)
p = 66.67
K = 2963.8
Vf = 1
A = Vf*(K/p)
exp = -p*t

#Se escribe la ecuación en el tiempo continuo de la velocidad angular del motor. NO es la velocidad lineal.
w = A*(1-pow(m.e,exp))

#Se genera la gráfica de rad/seg en el tiempo.
fig1 = plt.figure()
fig1.clf()
plt.plot(t,w)
plt.xlabel('tiempo (seg)')
plt.ylabel('w (rad/seg)')
plt.title('Velocidad angular del motor DC en el tiempo')
fig1.show()

#Se podría interpretar con rpm que es la medida que dan las hojas de datos de los motores DC

#Se realiza la conversión de los datos a rpm con la velocidad angular (rad/seg)
#conv es la razón de conversión respecto a los radianes por segundo
#Vrpm es la velocidad en revoluciones por minuto
conv = m.pi/30
Vrpm = w / (conv)

#Se genera la gráfica de rpm en el tiempo.
fig2 = plt.figure()
fig2.clf()
plt.plot(t,Vrpm)
plt.xlabel('tiempo (seg)')
plt.ylabel('rpm')
plt.title('Velocidad rpm del motor DC en el tiempo')
fig2.show()



#Se ajustan los datos para una velocidad lineal del Rover.
#r es el radio del neumático utilizado (puede incluir el grosor de la oruga en caso de que se utilice esta) en mts
#v es la velocidad lineal que puede proveer el motor DC a la estructura (De manera ideal)

r=0.1
v = w * r


#Se genera la gráfica de velocidad lineal en el tiempo.
fig3 = plt.figure()
fig3.clf()
plt.plot(t,v)
plt.xlabel('tiempo (seg)')
plt.ylabel('v (m/seg)')
plt.title('Velocidad en m/seg del motor DC en el tiempo')
fig3.show()








