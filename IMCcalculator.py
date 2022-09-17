#Práctica 2 - Programación 
#Equipo 24 
#Arturo Flores Callejas     318553874
#Luis Alberto Cortés Nuño     318092070
#Mayte Giselle Ramírez Moreno     318173274

import urllib.request 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

url='http://jse.amstat.org/datasets/body.dat.txt'
text=urllib.request.urlopen(url).readlines()

def IMC(peso , altura):
  IMC= peso/altura**2
  print(IMC)
    

imc= []
XY=[]
XS=[]
YS=[]
a=[]
m=[]
s=[]
e=[]

for line in range(len(text)) :
 a.append(float(text[line][121:126])/100)
 m.append(float(text[line][115:120]))
 s.append(float(text[line][127:128]))
 e.append(float(text[line][110:114]))
 imc.append((float(text[line][115:120]))/(float(text[line][121:126])/100)**2)

Data= {'Altura':a, 'Peso':m, 'Sexo':s, 'Edad':e, 'IMC':imc } 
Graf= pd.DataFrame(Data)

#Regresion lineal 

for i in range(len(text)):
  XY.append(e[i]*imc[i])
  XS.append(e[i]**2)
  YS.append(imc[i]**2)

N=len(text)
sumX=sum(e)
sumY=sum(imc)
sumXY=sum(XY)
sumXSquared=sum(XS)
sumYSquared= sum(YS)

pendiente=(N*sumXY-(sumX*sumY))/(N*sumXSquared-(sumX)**2)
intersección=(sumY-(pendiente*sumX))/N

print(f'La pendiente es: {pendiente} y la intersección: {intersección}' )

D=np.sqrt((N*sumXSquared-(sumX)**2)*(N*sumYSquared-(sumY)**2))
corr=(N*sumXY-(sumX*sumY))/D

print(f'La correlación entre IMC y edad es de {corr}, es decir es una mala correlación')

y=[]
x=[]
for a in range(15,70):
  y.append(pendiente*a+intersección)
  x.append(a)

plt.scatter(e,imc, color='turquoise',  s=26)
plt.plot(x,y, color='darkviolet')
plt.xlabel('Edad')
plt.ylabel('IMC')
plt.title('Correlación IMC-Edad')
plt.legend(['Linea de regresión', 'Entradas individuales',])
plt.show()


numHombres=s.count(1)
numMujeres=len(text)-numHombres

pesoHombres=m[0:numHombres]
pesoMujeres=m[numHombres:len(text)]

edadHombres=e[0:numHombres]
edadMujeres=e[numHombres:len(text)]

plt.scatter(pesoHombres,edadHombres, color='darkorange' )
plt.scatter(pesoMujeres,edadMujeres, color='springgreen' )
plt.title('Correlación Peso-Edad')
plt.xlabel('Peso')
plt.ylabel('Edad')
plt.legend(['Hombres', 'Mujeres'])
plt.show()