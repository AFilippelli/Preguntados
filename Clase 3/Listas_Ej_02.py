'''
Adrian Filippelli - 1B

La real academia española nos pide desarrollar un pequeño programa que contenta el
diccionario de la lengua española y su traducción al inglés. Para esto necesitamos un
algoritmo que nos permita el ingreso de una palabra en español y su traducción al
ingles y guardarlo en una lista. Si la palabra no existe, debemos agregarla, y si la
palabra existe debemos informar que la palabra ya existe y su índice dentro del listado,
esta carga debe ser hasta que el usuario se canse de ingresar palabras. Al finalizar se
debe mostrar todo el listado de palabras ingresadas con su palabra equivalente en
inglés. Recordar validar los datos de forma correcta.
'''
# respuesta = "si"
# lista_español = []
# lista_ingles = []

# while(respuesta == "si"):
#     español = input("Ingrese palabra en español: ")
#     ingles = input("Ingrese palabra en ingles: ")

#     lista_español.append(español)
#     lista_ingles.append(ingles)
#     respuesta = input("Desea continuar: si/no ")
    
# for i in range(len(lista_español)):
#     print(f'{i+1}- La palabra agregada es: {lista_español[i]} y su traducción es: {lista_ingles[i]}')

from os import system

diccionario = {}

while True:
    español = input('ingrese palabra en español')
    while not español.isalpha():
        español = input('Error, ingrese una palabra en español: ')

    ingles = input('ingrese palabra en español')
    while not español.isalpha():
        ingles = input('Error, ingrese una palabra en español: ')    

    if español in diccionario:
        if diccionario[español] == ingles:
            print(f'La palabra {español} ya existe en el diccionario y su traduccion es: {ingles}')
        else:
            print(f'La palabra {español} ya existe en el diccionario con la siguiente traduccion en ingles:')
    else:
        diccionario[español] = ingles
        print(f'La palabra {español} se agregó al diccionario con su traducción al ingles {ingles}')

    seguir = input('desea continuar: ')   
    while seguir != 'no' and seguir != 'si':
        seguir = input('Error, desea continuar? ') 

    if seguir == 'no':
        break

print(f'diccionario:'
    f'\n ----------------------------------')
for español, ingles in diccionario.items():
    print(f'\n{español}: {ingles}')      