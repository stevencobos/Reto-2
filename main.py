inicio = 'Para la resolucion del problema necetamos tener los siguientes datos'
print(inicio)

#Datos Algoritmicos
Dato_1 = float(input('ingrese el diametro de la polea en centimetros (cm): '))
Dato_2 = float(input('ingrese el largo de la puerta en metros (mts): '))
Dato_3 = float(input('ingrese la altura del  muro(mts)'))
Dato_4 = float(input('ingrese el tiempo maximo que desea (MIN): '))


#algoritmos para la solucion del problema
import math
L_Cuerda = (math.sqrt(Dato_2**2 + Dato_3**2))
L_Circulo = (math.pi*Dato_1)
DCE = L_Cuerda - (Dato_3-Dato_2)

#Solucion de Problemas 
#1
print("\033[;31m"+ '¿Cuántas vueltas deben darse para cerrar la puerta completamente?')
NV = DCE/Dato_3
print("\033[;36m"+'RESPUESTA PRIMERA PREGUNTA:\n', NV)
#2
print("\033[;31m"+ 'Como cada Chewbacca solo puede girar la polea 3 veces antes de caer exhausto ¿Cuántos Chewbaccas se necesitan para cerrar la puerta?')
N_Chew = NV/3
print("\033[;36m"+'RESPUESTA PRIMERA PREGUNTA:\n', N_Chew)
#3
print("\033[;31m"+ '¿Si se desea cerrar la puerta en un número máximo de minutos, que también nos dan, ¿A qué velocidad deben girar la polea (cms/seg) para poder cerrarla en ese tiempo?')
Dato_5 = Dato_4*60
DCE_2 = DCE*100
Vel_Max = DCE_2/Dato_5
print("\033[;36m"+'RESPUESTA PRIMERA PREGUNTA:\n', Vel_Max, '(cm/seg)')