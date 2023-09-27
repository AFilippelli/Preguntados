
'''
Para definir el largo y ancho del juego se debe usar una TUPLA ya que
las medidas del ancho y largo de la pantalla son valores que no van
a cambiar
(la tupla se declara con parentesis a diferencia de las listas que son
declaradas con corchetes)
'''

'''
los diccionarios a diferencia de las listas se
definen con llaves y tienen dos partes, la clave y el valor.
Ej mi_diccionario = {"codigo": 5, "descripcion": "coca cola"}
Tambien se puede asignar manual mente una clave y un valor a un diccionario
vacio.
Ej:''' 
mi_diccionario = {}
mi_diccionario["codigo"] = 5
mi_diccionario["descripcion"] = "Coca cola"

#para mostrar solo las claves de un diccionario:
for clave in mi_diccionario:
    print(clave)

#para mostrar los valores de un diccionario:
for clave in mi_diccionario:
    print(mi_diccionario[clave])

#para mostrar las claves con los valores de los diccionarios:
for clave in mi_diccionario:
    print(f"{clave}: {mi_diccionario[clave]}")    


#LISTAS de DICCIONARIOS
lista_productos = []
producto1 = {"codigo":5, "descripcion":"Coca Cola","precio":400}
producto2 = {"codigo":3, "descripcion":"Pepsi","precio":350}
producto3 = {"codigo":9, "descripcion":"Fanta","precio":450}
#para agregar los diccionarios a la lista de productos:
lista_productos.append(producto1)
lista_productos.append(producto2)
lista_productos.append(producto3)

#tambien se pueden copiar los codigos y valores y meterlos directamente
#dentro de la lista
lista_productos = [{"codigo":5, "descripcion":"Coca Cola","precio":400},
                   {"codigo":3, "descripcion":"Pepsi","precio":350},
                   {"codigo":9, "descripcion":"Fanta","precio":450}
                   ]

#para crear una lista de diccionarios pidiendo datos se debe hacer:
lista_productos2 = []
for i in range(3):
    codigo = int(input("Ingrese el codigo: "))
    descripcion = (input("Ingrese descripcion: "))
    precio = float(input("Ingrese precio: "))
    un_producto = {}
    un_producto["codigo"] = codigo
    un_producto["descripcion"] = descripcion
    un_producto["precio"] = precio
#el diccionario debe ser creado dentro del for para que 
#en cada vuelta tome un diccionario nuevo y no reemplace al anterior

#para mostrar la lista creada:
for producto in lista_productos:
    print(f'{producto["codigo"], producto["descripcion"], producto["precio"]}')  


#para recorrer una lista se pueden utilizar 2 tipos de for:
#1).for i in range(len(lista)):
#    print(f"{lista[i]['codigo']}") 
#en este caso, i va a tomar el valor de cada elemento de la lista
#2).for clave in lista:
#    print(f"{clave['codigo']} - {clave['descripcion']}")
