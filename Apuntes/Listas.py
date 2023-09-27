#Listas

lista = [5,9,8,7,3,6,4,5,5]
print(lista)
print(f"Elemento 3: {lista[3]}")
print(lista[0:3]) #[Desde:Hasta] D:Incluye el 0 / H: Excluye el ultimo numero
print(lista[3:5])

acumulador = 0
contador = 0

for i in range(len(lista)):
    acumulador = acumulador + lista[i] #suma todos los numeros de la lista
    if(lista[i] == 5):
        contador = contador + 1 #suma todas las veces que se repite el numero 5

print(acumulador)
print(contador)

lista.append(100) #agregar al final de la lista el valor que queramos (100)
lista.insert(2,80)#agrega un nuevo valor en la posicion que pidamos (2)
lista.extend([99,88,77])#se utiliza para agregar a la lista otra lista con nuevos valores.

#tema de hoy: listas, diccionarios, tuplas y set
'''
#LISTAS:
para definir una lista por extension significa q voy a darle valores al momento de asignar, como si fuera un conjunto de matematicas.

las listas se definen con corchetes, dentro de ellas puedo guardar lo que se me ocurra, inclusive otras listas.

'''

'''
mi_lista = [5,9,7,4,3,2,1]
#para ver lo q esta guardando la lista podes imprimirla pero nosotros vamos a RECORRER la lista para mostrar lo que vamos a hacer
print(mi_lista) #aca solo muestro lo que guarda
'''

#los elementos se agregan con el metodo append
mi_lista = []

mi_lista.append(4) #0
mi_lista.append(5) #1
mi_lista.append(6) #2
mi_lista.append(3) #3

#si  yo utilizo index, me va a decir por ejemmplo index(5) y va a decir el 5 esta en la posicion 1

print (mi_lista) #la muestra tambien.

#se puede recorrer la lista a traves del indice y por elementos 
for i in range(len(mi_lista)):
    print(mi_lista[i]) #si yo hago de la lista la posicion i, i va a tomar cada valor del rango entonces cada vez q itere va a tomar el valor de los numeros q yo puse en la lista

#otra forma de mostrar es recorriendo elemento por elemento
for numero in mi_lista: #en cada iteracion va a tomar un elemento de la lista
    print(numero)

#dif entre cada for: en el primero recorro el indice, si quiero puedo modificar la lista, y el otro no. Si uso el primero la variale va a ser una letra, si es el segundo, va a ser una variable especifica q indique que es

#eliminar elementos de una lista: 
mi_lista.remove(6) #elimino el elemento SEIS no la posicion SEIS
print (mi_lista)

#TUPLAS: COLECCIONES INMUTABLES
#DENTRO DE UNA LISTA ESTO ES INMUTABLE

mi_tupla = (3,6,9,7)
print(type(mi_tupla)) #SE DISTINGUE PORQUE LA LISTA SE DECLARA CON CORCHETES Y LA TUPLA CON parentesis o sin.

#el SET sirve para evitar los duplicados, se definen de esta manera
mi_set = set([5,6,5,4,5,42,2,3]) #O TAMBIEN {4,5,5,6,5,6,6,2,4,1}
print(mi_set)

#DICCIONARIOS
#SE DEFINE AL IGUAL QUE UN SET ({}) PERO TENEMOS LA PARTICULARIDAD DE QUE AL DICCIONARIO SE PUEDE DEFINIR CON EL NOMBRE MAS LA ASIGNACION
mi_diccionario = {"codigo":5, "descripcion":"coca cola"}
print(mi_diccionario) #lo veo tal como lo ingrese
#otra forma de crear un diccionario:
mi_diccionario["codigo"] = 5
print (mi_diccionario)#lo unico q tendria este diccionario seria una clave con un valor
#no se puede tener en un mismo diccionario 2 claves iguales 

mi_diccionario["codigo"] = 5
mi_diccionario["descripcion"] ="coca cola"
print (mi_diccionario["descripcion"]) #solo muestra la descripcion

#para mostrar solo las claves:
for clave in mi_diccionario:
    print(clave) #solo muestra la clave

for clave in mi_diccionario:
    print(f"{clave}: {mi_diccionario[clave]}") #muestro todas las claves y los valores q yo les di


#listas de diccionarios:
lista_diccionarios = []
producto1 = {"codigo": 5, "descripcion":"coca cola", "precio":400}
producto2 = {"codigo": 3, "descripcion":"pepsi", "precio":350}
producto3 = {"codigo": 9, "descripcion":"fanta", "precio":450}

lista_diccionarios.append(producto1)
lista_diccionarios.append(producto2)
lista_diccionarios.append(producto3)

print(lista_diccionarios)

#podria definirlo asi tambien

producto1 = {"codigo": 5, "descripcion":"coca cola", "precio":400}
producto2 = {"codigo": 3, "descripcion":"pepsi", "precio":350}
producto3 = {"codigo": 9, "descripcion":"fanta", "precio":450}

lista_diccionarios = []

print(lista_diccionarios)

#o tambien:
lista_diccionarios = [{"codigo": 5, "descripcion":"coca cola", "precio":400},
                    {"codigo": 3, "descripcion":"pepsi", "precio":350},
                    {"codigo": 9, "descripcion":"fanta", "precio":450}]



#pedirle al usuario datos y armar una lista
lista_diccionarios = []
cantidad = 3
for i in range(cantidad):
    codigo= int(input("ingrese el codigo: "))
    descripcion = input("ingrese descripcion: ")
    precio = float(input("ingrese el precio: "))
    un_producto = {} #se crea adentro siempre
    un_producto["codigo"] = codigo
    un_producto["descripcion"] = descripcion
    un_producto["precio"] = precio
    lista_diccionarios.append(un_producto)

#mostrar
for producto in lista_diccionarios:
    print(f"{producto['codigo']}---{producto['descripcion']}---{producto['precio']}")