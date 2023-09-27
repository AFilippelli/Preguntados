'''
Adrian Filippelli 1B

Una concesionaria de autos nos pide desarrollar un sistema para controlar el stock de
autos que tienen disponible a la venta. Para esto se necesita saber de cada auto: la
marca, el año del modelo y el precio (validar los tipos de datos ingresados) y
mostrarlos por pantalla en forma secuencial y ordenada. Realizar el ejercicio sin usar
listas primero, y despues usando listas y comparar la composición del código.
'''

'''
respuesta = "si"

while(respuesta == "si"):
    marca = input("Ingrese la marca del auto: ")
    modelo = input("Ingrese el modelo del auto: ")
    año = input("Ingrese el año del auto: ")
    precio = float(input("Ingrese el precio del auto: "))
    respuesta = input("Desea continuar? si/no")

    print("La marca del auto es: ", marca)
    print("El modelo del auto es: ", modelo)
    print(f'El auto es del año: {año}')
    print(f'El precio del auto es: {precio}\n----------------')
'''



respuesta = "si"
lista_marcas = []
lista_modelo = []
lista_año = []
lista_precio = []

while(respuesta == "si"):
    marca = input("Ingrese la marca del auto: ")

    modelo = input("Ingrese el modelo del auto: ")

    año = int(input("Ingrese el año del auto(1900-2023): "))
    while año < 1900 or año > 2023:
        año = int(input("Error, ingrese año del auto(1900-2023): "))

    precio = float(input("Ingrese el precio del auto: "))
    while precio < 1 or precio > 10000000:
        precio = float(input("Error, ingrese precio valido"))
    
    lista_marcas.append(marca)
    lista_modelo.append(modelo)
    lista_año.append(año)
    lista_precio.append(precio)
    respuesta = input("Desea continuar si/no")


for i in range(len(lista_marcas)):
    print(f'\n')
    print(f'{i+1}-Marca: {lista_marcas[i]}')
    print(f'{i+1}-Modelo: {lista_modelo[i]}') 
    print(f'{i+1}-Año: {lista_año[i]}') 
    print(f'{i+1}-Precio: {lista_precio[i]}\n---------------------')     