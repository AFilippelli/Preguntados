'''Ejercicio 4:
Pedir una edad y un estado civil, si la edad es menor a 18 años y el estado civil
distinto a "Soltero", mostrar el siguiente mensaje: 'Es muy pequeño para NO
ser soltero.'''

respuesta = "si"

while respuesta == "si":
    edad = int(input("Ingrese su edad: "))

    estado_civil = input("Ingrese su estado civil: ")
    while estado_civil != "Soltero" and estado_civil != "Casado":
        estado_civil = int(input("Error. ingrese estado civil (soltero/casado): "))

    if edad <= 17 and estado_civil != "Soltero":
        print("es muy pequeño para NO ser soltero")
    else:
        print("felicidades")

    respuesta = input('Desea continuar? si/no')