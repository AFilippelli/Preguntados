'''
Ejercicio 6:
Utilizar For
Dada la siguiente lista:
[82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]
mostrar el mayor.
'''
lista_numeros = [82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]
mayor_numero = 0
mayor_numero = lista_numeros[0]

for numero in lista_numeros:
    if numero > mayor_numero:
        mayor_numero = numero
        
print(f"el mayor numero es {mayor_numero}")