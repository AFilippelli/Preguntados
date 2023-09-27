#Adrian Filippelli stark 01
from data_stark import lista_personajes


'''
A. Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe
B. Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor
fuerza (MÁXIMO)
C. Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo
(MÍNIMO)
D. Recorrer la lista y determinar el peso promedio de los superhéroes
masculinos (PROMEDIO)
E. Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier
género) los cuales su fuerza supere a la fuerza promedio de todas las
superhéroes de género femenino

'''

def imprimir_datos_superheroe(personaje):
    for clave, valor in personaje.items():
        print(f"{clave}: {valor}")
    print()

def mostrar_lista():
    for heroe in lista_personajes:
        imprimir_datos_superheroe(heroe)


def mostrar_mas_fuerte():
    flag_mas_fuerte = True
    
    for heroe in lista_personajes:
        if flag_mas_fuerte == True or float(heroe['fuerza']) > heroe_fuerte:
            flag_mas_fuerte = False
            heroe_fuerte = float(heroe['fuerza'])
            identidad_fuerte = heroe['identidad']
            peso_fuerte = heroe['peso']

    print(f"La identidad del heroe mas fuerte es: {identidad_fuerte} y su peso es: {peso_fuerte}kg")


def mostrar_mas_bajo():
    flag_mas_bajo = True

    for heroe in lista_personajes:
        if flag_mas_bajo == True or float(heroe['altura']) < heroe_bajo:
            flag_mas_bajo = False
            heroe_bajo = float(heroe['altura'])
            nombre_bajo = heroe['nombre']
            identidad_bajo = heroe['identidad']

    print(f"{nombre_bajo} es el heroe mas bajo y su identidad es: {identidad_bajo}")


def mostrar_peso_promedio_m():
    contador_hombres = 0
    acumulador_peso = 0

    for heroe in lista_personajes:

        peso = float(heroe['peso'])

        if heroe['genero'] == 'M':
            acumulador_peso += peso
            contador_hombres += 1
    if contador_hombres > 0:
        promedio_peso = acumulador_peso / contador_hombres
    else:
        promedio_peso == 0

    print(f"El promedio del peso de genero masculino es: {promedio_peso}kg ")


def mostrar_fuerza_promedio_f():
    contador_mujeres = 0
    acumulador_fuerza = 0

    for heroe in lista_personajes:
        fuerza = float(heroe['fuerza'])

        if heroe['genero'] == 'F':
            acumulador_fuerza += fuerza
            contador_mujeres += 1
        
    promedio_fuerza = acumulador_fuerza / contador_mujeres

    return promedio_fuerza


def mostrar_fuerza_mayor_promedio_f():
    promedio_femenino = mostrar_fuerza_promedio_f()
    for heroe in lista_personajes:
        heroe_fuerte = float(heroe['fuerza'])
        if heroe_fuerte > promedio_femenino:

            nombre_fuertes = heroe['nombre']
            peso_fuertes = float(heroe['peso'])
            print(f"{nombre_fuertes} es mas fuerte que el promedio femenino y su peso es de: {peso_fuertes}kg")


menu = ["1. mostrar todos los datos de cada superhéroe",
        "2. mostrar  la identidad y el peso del superhéroe con mayor fuerza",
        "3. mostrar el mostrar nombre e identidad del superhéroe más bajo",
        "4. mostrar el peso promedio de los superhéroes masculinos",
        "5. mostrar el nombre y peso de los superhéroes  los cuales su fuerza supere a la fuerza promedio de todas las superhéroes de género femenino",
        "6. Salir"
        ]

def mostrar_menu():
    for opcion in menu:
        print(opcion)

seguir = True
while seguir == True:
    mostrar_menu()
    respuesta = input("Ingrese una opcion: ")
    while respuesta != "1" and respuesta != "2" and respuesta != "3" and respuesta != "4" and respuesta != "5" and respuesta != "6":
        respuesta = input("Error, ingrese una opcion valida (1,2,3,4,5,6)")
    match respuesta:
        case "1":
            mostrar_lista()
        case "2":
            mostrar_mas_fuerte()
        case "3":
            mostrar_mas_bajo()
        case "4":
            mostrar_peso_promedio_m()
        case "5":
            mostrar_fuerza_mayor_promedio_f()
        case "6":
            break











