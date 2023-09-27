#Adrian Filippelli - 1B - Ejercicio integrador 02
from data_stark_01 import lista_personajes
from os import system


'''
0. Crear la función 'stark_normalizar_datos' la cual recibirá por parámetro la lista
de héroes. La función deberá:
● Recorrer la lista y convertir al tipo de dato correcto las keys (solo con
las keys que representan datos numéricos)
● Validar primero que el tipo de dato no sea del tipo al cual será
casteado. Por ejemplo si una key debería ser entero (ejemplo edad)
verificar antes que no se encuentre ya en ese tipo de dato.
● Si al menos un dato fue modificado, la función deberá imprimir como
mensaje ‘Datos normalizados’, caso contrario no imprimirá nada.
● Validar que la lista de héroes no esté vacía para realizar sus acciones,
caso contrario imprimirá el mensaje: “Error: Lista de héroes vacía”
'''

def stark_normalizar_datos(lista_personajes):

    bandera_normalizados = False

    if len(lista_personajes) > 0:
        for heroe in lista_personajes:
            if type(heroe['altura']) != float:
                heroe['altura'] = float(heroe['altura'])
                bandera_normalizados = True

            if type(heroe['peso']) != float:
                heroe['peso'] = float(heroe['peso'])
                bandera_normalizados = True

            if type(heroe['fuerza']) != float:
                heroe['fuerza'] = float(heroe['fuerza'])
                bandera_normalizados = True

        if bandera_normalizados == True:
            print('--------Datos normalizados--------')
    else:
        print('Error: Lista vacía')

    return lista_personajes

'''
1.1. Crear la función 'obtener_nombre' la cual recibirá por parámetro un
diccionario el cual representara a un héroe y devolverá un string el cual
contenga su nombre formateado de la siguiente manera:
Nombre: Howard the Duck
'''

def obtener_nombre(heroe:dict, clave:str):
    heroe = {}
    for heroe in lista_personajes:
        print(f'heroe{lista_personajes[0]["nombre"]}')
    


