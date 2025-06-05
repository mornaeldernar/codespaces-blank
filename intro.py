# importamos numpy 
import numpy as np
import time

#creamos un arreglo de temperaturas
mi_lista_de_temperaturas = [20.5, 22.0, 19.5, 21.0, 23.5, 25.5 ,54]

# Convertimos la lista a un array de NumPy
temperaturas =  np.array(mi_lista_de_temperaturas)
# Imprimimos el array y sus tipos
print("Array de temperaturas:")
print(temperaturas)
print("Tipo de numpy array:",type(temperaturas))
print("Tipo de lista:",type(mi_lista_de_temperaturas))

# creamos una lista de 1_000_000 elementos
lista = list(range(1_000_000))
#empezamos a medir el tiempo de ejecución
start = time.time()
# realizamos una operacion con la lista
resultado_lista = [x * 9/5 + 32 for x in mi_lista_de_temperaturas]
#imprimimos cuánto tiempo tardó la operación en la lista
print("Tiempo con lista:", time.time() - start)

# Convertimos la lista a un array de NumPy
array = np.array(lista)
# empezamos a medir de nuevo el tiempo de ejecución
start = time.time()
#hacemos la misma operación con el array
resultado_array = temperaturas * 9/5 + 32
#imprimimos cuánto tiempo tardó la operación en el array 
print("Tiempo con array:", time.time() - start)

# creamos un array de de 10 elementos con valores de 0 a 3000 con el mismo espaciado
profundidades = np.linspace(0, 3000, 10)  # en metros
print(profundidades)

presion_superficie = 1200  # psi
gradiente = 0.35  # psi/m

# Calculamos la presión a diferentes profundidades
presion_pozo = presion_superficie - gradiente * profundidades
print("Presión a diferentes profundidades (psi):")
print(presion_pozo)

# Convertimos la lista de presiones a un array de NumPy
presiones = np.array(lista)
# Imprimimos el array de presiones y sus propiedades
print("Presiones:", presiones)
print("Dimensiones:", presiones.ndim)
print("Forma:", presiones.shape)
print("Tipo de dato:", presiones.dtype)
# Imprimimos estadísticas de la presión del pozo
print("Presión máxima:", np.max(presion_pozo))
print("Presión mínima:", np.min(presion_pozo))
print("Promedio:", np.mean(presion_pozo))
print("Desviación estándar:", np.std(presion_pozo))

# Creamos un arreglo 3D y calculamos estadísticas
arreglo3d = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]]
)
print("promedio por columas", np.mean(arreglo3d, axis=0))  # Promedio por columnas
print("promedio por filas", np.mean(arreglo3d, axis=1))  # Promedio por filas

print("promedio total", np.mean(arreglo3d))  
print("mediana", np.median(arreglo3d))  # Mediana
print(arreglo3d[0:2]) #Filas
print(arreglo3d[0:2, 1:3])  # Filas 0 y 1, columnas 1 y 2

print(np.ones((3,3)))  # Crea un arreglo de unos
print(np.zeros((2, 3)))  # Crea un arreglo de ceros

print(np.eye(3)) # Crea una matriz identidad de 3x3
unos = np.ones((3,3))  # Crea una matriz de 1s de 3x3

arreglo3d = np.array([
    [1,2,3],
    [4,5,6]]
)
arreglo3d2 = np.array([
    [2,3,6],
    [2,7,6]]
)
# sumamos, restamos, multiplicamos y dividimos los arreglos
print(arreglo3d + arreglo3d2) # suma posicion en arreglo3d + posicion en unos
print(arreglo3d - arreglo3d2) # resta posicion en arreglo3d + posicion en unos
print(arreglo3d * arreglo3d2) # multiplicación posicion en arreglo3d + posicion en unos
print(arreglo3d / arreglo3d2) # división posicion en arreglo3d + posicion en unos

print(arreglo3d.shape) # Dimensiones del arreglo

print(len(arreglo3d)) # Número de filas
print(arreglo3d.size)  # Número total de elementos
print(arreglo3d.ndim)  # Número de dimensiones
print(arreglo3d.dtype)  # tipo de dato
print(arreglo3d == arreglo3d2) # Compara elemento a elemento
print(arreglo3d.flatten())  # Aplana el arreglo a una dimensión  


celsius = [15, 20, 305, 405]
arr_c = np.array(celsius)
start = time.time()
# El convertidor de Celsius a Fahrenheit
fahrenheit = [temp * 9/5 + 32 for temp in celsius]
# Mostrar resultados
print("Tiempo con list:", time.time() - start)
print("Resultado de Temperaturas en Fahrenheit:", fahrenheit)
start = time.time()
# Convertir a Fahrenheit: F = C * 9/5 + 32
arr_f = arr_c * 9/5 + 32
# Convertir el arreglo de Fahrenheit a lista
print("Tiempo con array:", time.time() - start)


mi_lista_de_temperaturas = [15, 33, 60, 70, 80, 90, 100, 105, 120, 14] # Lista de temperaturas en grados Celsius

print(mi_lista_de_temperaturas)
mi_array_de_temperaturas = np.array(mi_lista_de_temperaturas, dtype=float) # Convertir la lista a un array de NumPy
print(mi_array_de_temperaturas)
farenheit = (mi_array_de_temperaturas * 9/5) + 32
print(farenheit) # Conversión de Celsius a Fahrenheit
"""
np.array, 0 - 5000, 50 valores
sacar la media, mediana, desviación estándar, máximo y mínimo
"""

numberlist = np.linspace(0, 5000, 100) # Crear un array de 100 valores entre 0 y 5000
print(numberlist)
print(numberlist.shape)
print(numberlist.dtype)
print(numberlist.ndim)
print(numberlist.size)
print(min(numberlist))
print(max(numberlist))
print(len(numberlist))

pozo1= [120, 130, 125, 140, 135, 128, 132]  # Pozo 1
pozo2= [110, 115, 118, 120, 122, 119, 121]  # Pozo 2
pozo3= [150, 155, 160, 158, 162, 159, 161]  # Pozo 3

pozos = np.array([pozo1, pozo2, pozo3])  # Crear un array 2D con los pozos
total_por_pozo = np.sum(pozos, axis=1)  # Sumar por filas (cada pozo)
total = np.sum(pozos)  # Sumar por filas (cada pozo)
print("Total por pozo:", total_por_pozo)
print("Total :", total)

# obtener los ingresos totales por pozo, y los ingresos totales generales
precio_petroleo = [78, 82, 85, 80, 79, 83, 84]  # Precios del petróleo
precio_petroleo_array = np.array(precio_petroleo)  # Convertir a un array de NumPy
ingresos = pozos*precio_petroleo_array  # Multiplicar cada pozo por el precio del petróleo
print("Ingresos por pozo:", ingresos)
ingresos_totales = np.sum(ingresos, axis=1)  # Sumar los ingresos por pozo
print("Ingresos totales por pozo:", ingresos_totales)
ingresos_totales_generales = np.sum(ingresos_totales)  # Sumar los ingresos totales por pozo
print("Ingresos totales generales:", ingresos_totales_generales)

días = np.argmax(ingresos, axis=1)+1  # Obtener el día con mayor ingreso por pozo (ajustando el índice a 1-7)
print("Día con mayor ingreso por pozo:", días)
#MEDIA DE INGRESOS POR POZO
media_ingresos = np.mean(ingresos, axis=1)  # Calcular la media de ingresos por pozo
print("Media de ingresos por pozo:", media_ingresos)

"""
esto es un comentario de varias líneas
aqui va otra linea 
"""
# Guardar los ingresos por pozo en un archivo CSV
np.savetxt('ingresos_por_pozo.csv', ingresos, delimiter=',', header='Lunes,Martes,Miercoles,Jueves,Viernes,Sabado,Domingo', comments='')
