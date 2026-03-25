# Ejercicio #1: (Nombre del archivo: ejercicio1.py)
# Escriba un programa en Python que dado un numero N, mayor que 5, leido de el usuario,
# cree una lista con los con N numeros aleatorios entre 10 y 99.
# Despliegue la lista generada, y luego cree una segunda lista con los numeros
# de la primera lista al cuadrado. Luego despliegue la segunda lista.
# Para generar las listas, DEBE utilizar ciclos for
# Ejemplo:
# 			Ingrese N: 5
# 			Lista: [50, 20, 41, 58, 37]
# 			Lista cuadrados: [2500, 400, 1681, 3364, 1369]

import random

try:
    n = int(input("Ingrese N: "))

    lista_valores_random = []
    lista_de_cuadrados = []

    for _ in range(1, n + 1):
        numero_random = random.randint(10, 99)
        lista_valores_random.append(numero_random)

    for current in lista_valores_random:
        lista_de_cuadrados.append(current * current)
    
    print("Lista: ", lista_valores_random)
    print("Lista cuadrados: ", lista_de_cuadrados)


except ValueError:
    print("Lo que ingreso no es un numero")