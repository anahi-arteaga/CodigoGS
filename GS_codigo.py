# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 14:21:47 2020

@author: anahi
"""
import numpy as np
import math 
import pandas as pd
import matplotlib.pyplot as plt

N = float(input("Ingrese el numero de membranas pares:  "))
Ai = float(input("Ingrese el area de las membranas (m^2):  "))

Pcem = float(0.92)
Paem = float(0.92)
Raem = float(0.00013)
Rcem = float(0.00027)
T = float(25+273.15)   #temperatura en grados Kelvin
R = float(8.314)  #Constante universal de los gases J/molK
F = float(96485.3365)  #Constante de Faraday C/mol
z = float(1**2)   #valencia
Es = float(0.05) # Espaciamiento de membranas 

# coeficiente de actividad 
ANa = 450 #radio de efectividad del ion hidratado 
ACl = 300
gnac = math.exp((-0.5*z*math.sqrt(0.6))/(1+(ANa/305)*math.sqrt(0.6)))
gnad = math.exp((-0.5*z*math.sqrt(0.1))/(1+(ANa/305)*math.sqrt(0.1)))
gclc = math.exp((-0.5*z*math.sqrt(0.6))/(1+(ACl/305)*math.sqrt(0.6)))
gcld = math.exp((-0.5*z*math.sqrt(0.1))/(1+(ACl/305)*math.sqrt(0.1)))

acem = math.log((gnac*0.6)/(gnad*0.1))
aaem = math.log((gclc*0.6)/(gcld*0.1))

#calculo de voltaje 
Ecem = Pcem*((R*T)/(z*F))*acem
Eaem = Paem*((R*T)/(z*F))*aaem
Ecell = N*(Ecem+Eaem)

#Calculo de la resistencia 

fo = 1.8
Rl = fo*(1/7)*(Es/Ai)
Rh = fo*(1/55)*(Es/Ai)
r = Raem+Rcem+Rh+Rl
Rel = 2*(1/2380000)
Ri = N*r+Rel

# intensidad 
Re =np.array([92,47,22,10,6.8,5.6,4.7,3.3,2.2,1.8,1.2,0.56,0.39,0.22,0.1])
i = Ri+Re
I = Ecell/i #corriente electrica 

#Potencia 
Pgross = (I**2)*Re
Pd = Pgross/(N*Ai)
#Voltaje 
Ec = Pgross/I

df = pd.DataFrame({'Ri (ohms)': Ri,'Re (ohms)':Re,'Potencia (W)':Pgross,
                   'DPotencia (W/m^2)':Pd,'CE (A)':I,'Voltaje (V)':Ec})

#Graficas
fig = plt.figure(figsize=(10,10))
fig.tight_layout()
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)
ax1.plot(I,Pgross,'ro')
ax2.plot(I,Ec,marker='*')
ax1.set_xlabel('Intensidad')
ax1.set_ylabel('Potencia')
ax2.set_xlabel('Intensidad')
ax2.set_ylabel('Voltaje')
ax1.set_title('Potencial maximo')
ax2.set_title('Intensidad vs Potencia')
ax1.grid()
ax2.grid()
plt.show()




