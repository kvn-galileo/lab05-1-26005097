# Ejercicio #2: (Nombre del archivo: ejercicio2.py)
# Para este ejercicio lea un numero N, mayor que 3, del usuario,
# el cual representa la cantidad de palabras que dicho usuario va a ingresar al programa.
# Luego lea N palabras , y despliegue la palabra mas corta y la mas larga. Utilice ciclos for.

try:
    n = int(input("Ingrese N mayor a 3: "))

    if (n<=3):
        print("Tu numero no es mayor que 3")
        exit()
    
    lista_de_palabras = []

    for i in range(1, n + 1):
        nueva_palabra = input(str(i) + ") Ingrese una palabra: ")
        lista_de_palabras.append(nueva_palabra)
    
    palabra_mas_corta = lista_de_palabras[0]
    for palabra in lista_de_palabras:
        if (len(palabra) < len(palabra_mas_corta)):
            palabra_mas_corta = palabra

    palabra_mas_larga = lista_de_palabras[0]
    for palabra in lista_de_palabras:
        if (len(palabra) > len(palabra_mas_larga)):
            palabra_mas_larga = palabra

    print("")
    print("Palabra mas corta: ", palabra_mas_corta)
    print("Palabra mas larga: ", palabra_mas_larga)
    print("")


except ValueError:
    print("El valor que ingreso no es un numero")