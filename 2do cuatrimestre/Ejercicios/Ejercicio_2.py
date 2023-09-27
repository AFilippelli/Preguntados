'''Ejercicio 2:
Pedir una edad. Informar si la persona es mayor de edad 
(más de 18 años),adolescente (entre 13 y 17 años) o niño
(menor a 13 años).'''

respuesta = "si"

while respuesta == "si":
    edad = int(input("ingrese edad: "))
    if edad >= 1 and edad <= 13:
        print("Usted es un niño")
    elif edad >= 13 and edad <= 17:
        print("Usted es un adolescente")
    elif edad >= 18:
        print("Usted es mayor de edad")

    respuesta = input('Desea continuar? si/no')

