'''Ejercicio 5:
Una agencia de viajes debe sacar las tarifas de los viajes , se cobra $15.000
por cada estadía como base, se pide el ingreso de una estación del
año(Invierno/Verano/Otoño/Primavera) y localidad(Bariloche/Cataratas/Mar del
Plata/Córdoba) para vacacionar para poder calcular el precio final:
-en Invierno: Bariloche tiene un aumento del 20% Cataratas y Córdoba tiene un
descuento del 10% Mar del Plata tiene un descuento del 20%
-en Verano: Bariloche tiene un descuento del 20% Cataratas y Córdoba tiene
un aumento del 10% Mar del Plata tiene un aumento del 20%
-en Otoño y Primavera: Bariloche tiene un aumento del 10% Cataratas tiene un
aumento del 10% Mar del Plata tiene un aumento del 10% y Córdoba tiene el
precio sin descuento.
Validar el ingreso de datos'''
precio = 15000
precio_final = 0

respuesta = "si"

while respuesta == "si":
    estacion = input("ingrese estacion: ")
    while estacion != "invierno" and estacion != "verano" and estacion != "otoño" and estacion != "primavera":
        estacion = input("error, ingrese estacion (invierno/verano/otoño/primavera)")

    localidad = input("ingrese localidad: ")
    while localidad != "bariloche" and localidad != "cataratas" and localidad != "mar del plata" and localidad != "cordoba":
        localidad = input("error, ingrese estacion (bariloche/cataratas/mar del plata/cordoba)")

    match estacion:
        case "invierno":
            if localidad == "bariloche":
                precio_final = precio * 1.20
            elif localidad == "cataratas" or "cordoba":
                precio_final = precio * 0.90
            elif localidad == "mar del plata":
                precio_final = precio * 0.80
        case "verano":
            if localidad == "bariloche":
                precio_final = precio * 0.80
            elif localidad == "cataratas" or "cordoba":
                precio_final = precio * 1.10
            elif localidad == "mar del plata":
                precio_final = precio * 1.20
        case "otoño":
            if localidad == "bariloche" or "cataratas" or "mar del plata":
                precio_final = precio * 1.10
            elif localidad == "cordoba":
                precio_final = precio
        case "otoño":
            if localidad == "bariloche" or "cataratas" or "mar del plata":
                precio_final = precio * 1.10
            elif localidad == "cordoba":
                precio_final = precio

    print(f"el precio final es {precio_final}")

    respuesta = input('Desea continuar? si/no')