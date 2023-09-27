'''
Ejercicio 3:
Ingresar 5 números enteros, distintos de cero.
Informar:
a. Cantidad de pares e impares.
b. El menor número ingresado.
c. De los pares el mayor número ingresado.
d. Suma de los positivos.
e. Producto de los negativos.
'''
cantidad_pares = 0
cantidad_impares = 0
menor_numero = 0
mayor_par = 0
suma_positivos = 0
bandera_menor = 0
bandera_mayor = 0

for numeros in range(5):
    numeros += 1
    numero = int(input("Ingrese numeros: "))
    
    if numero % 2 == 0:
        cantidad_pares += 1
        if bandera_mayor == True or numero > mayor_par:
            bandera_mayor = False
            mayor_numero = numero

    if numero % 2 == 1:
        cantidad_impares += 1

    if bandera_menor == True or numero < menor_numero:
        bandera_menor = False
        menor_numero = numero

    if numero >= 0:
        suma_positivos += numero


print(f"El numero mayor es: {mayor_numero}")
print(f"El numero menor es: {menor_numero}")
print(f"La cantidad de numeros pares es: {cantidad_pares}")
print(f"La cantidad de numeros impares es: {cantidad_impares}")
print(f"la suma de positivos es: {suma_positivos}")