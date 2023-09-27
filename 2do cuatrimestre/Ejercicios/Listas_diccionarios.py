dic = {"nombre" : "Adrian" , "Edad" : 19 , "dni" : 101010}
dic_dos = {"nombre" : "Juan" , "Edad" : 18 , "dni" : 101011 , "hijos" : [2,4,6]}
#nombre -> key
#Adrian -> value

print(dic.keys()) #-> metodo para obtener todas las claves de un dic

print(dic.values())#-> metodo para obtener todos los valores de un dic

print(dic.items())#-> metodo para obtener claves y valores de un dic

#se puede tener una lista con uno o mas diccionarios adentro

lista = [dic,dic_dos]

print(lista[0])  #->muestr la posicion 0 de la lista, en este caso
                #el primer diccionario

#si quiero acceder a el valor de una key especifica dentro de la lista
#se debe hacer lo siguiente

print(lista[0]["nombre"])
#con esto estoy pidiendo el valor de la key "nombre" del primer
#diccionario de la lista

#puedo hacer una lista con un valor de otra lista ya existente
lista_hijos = lista[1]["hijos"]
print(lista_hijos)