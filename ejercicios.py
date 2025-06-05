import numpy as np 
#Calcular producción semanal
Pozo1= [120, 130, 125, 140, 135, 128, 132]  # Pozo 1
Pozo2=[110, 115, 118, 120, 122, 119, 121]  # Pozo 2
Pozo3=[150, 155, 160, 158, 162, 159, 161]   # Pozo 3
pozos = np.array([Pozo1, Pozo2, Pozo3])
#sumar las producciones de cada pozo por día
produccion_semanal = np.sum(pozos, axis=1)
print("Producción semanal por pozo:", produccion_semanal)
#calcular los ingresos de cada pozo a la semana
precio_petroleo = [78, 82, 85, 80, 79, 83, 84]
array_precio = np.array(precio_petroleo)
ingresos_semanales = pozos * array_precio
print("Ingresos semanales por pozo:", ingresos_semanales)
ingresos_totales = np.sum(ingresos_semanales, axis=1)
print("Ingresos totales semanales por pozo:", ingresos_totales)
#guardar el resultado en un archivo de texto
np.savetxt('ingresos_semanales.txt', ingresos_semanales, delimiter=',', header='Pozo1,Pozo2,Pozo3')
#calcular el día con mayor ingresos
mayor_ingreso = np.max(ingresos_semanales, axis=1)
días = np.argmax(ingresos_semanales, axis=1) + 1  # +1 para ajustar al índice de días (1-7)
print("Día con mayor ingreso por pozo:", días)