
# Adrian Filippelli - 1B

# Realizar una carga indefinida de números, añadirlos a una lista
# e indicar que posición de memoria es la que mas ocurrencias tiene 
# dentro de esa lista.

respuesta = "si"
lista_numeros = []

while(respuesta == "si"):
    numero = int(input("Ingrese numero/s: "))
    un_numero = {}
    un_numero['numeros'] = numero

    lista_numeros.append(numero)
    respuesta = input("Desea continuar: si/no ")

    for i in range(len(lista_numeros)):
        print(f'{i+1}- El/los numeros agregados son: {lista_numeros[i]}')


    flag_primero = True
    for numero in lista_numeros:
        if flag_primero == True or numero['numero'] > numero_maximo:
            numero_maximo = numero['numero']
            flag_primero = False
    
    for numero in lista_numeros:
        if numero['numero'] == numero_maximo: 
            print(f"{numero['numero']}")    
    
