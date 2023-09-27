''' 
Adrian Filippelli - 1B - Ejercicio 01
La división de higiene está trabajando en un control de stock para productos
sanitarios. Debemos realizar la carga de
una compra de productos de prevención de contagio, de cada una debe obtener los
siguientes datos:
· El tipo ("barbijo"; "jabón"; o "alcohol")
· El precio
· La cantidad de unidades
· La marca
· El fabricante
Se debe informar los datos de la compra procesados para poder iniciar el control de
stock.
'''

tipo = input("ingrese tipo 'barbijo', 'jabon', 'alcohol' ")
while tipo != 'barbijo' and tipo != 'jabon' and tipo != 'alcohol':
        tipo = input("Error, ingrese tipo ('barbijo', 'jabon', 'alcohol')")
precio = float(input("Ingrese precio")) 
while precio <= 0 or precio >= 100000:
        precio = float(input("Error: ingrese precio"))
cantidad_Unidades = int(input("Ingrese cantidad de unidades"))
while cantidad_Unidades <= 0 or cantidad_Unidades > 50:
        cantidad_Unidades = int(input("Error, ingrese cantidad de unidades"))
marca = input("Ingrese marca")
fabricante = input("Ingrese fabricante")


print("el tipo de producto es " + tipo)
print(f"el precio del producto es $ {precio}")
print(f"la cantidad de unidades es {cantidad_Unidades}")
print("la marca es " + marca)
print("El fabricante es" + fabricante)

