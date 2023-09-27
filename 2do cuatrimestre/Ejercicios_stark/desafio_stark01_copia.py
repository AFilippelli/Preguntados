#Adrian Filippelli
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

def mostrar_lista():
    for i in range(len(lista_personajes)):
        print(f"Heroe Nº{i+1}: \nNombre: {lista_personajes[i]['nombre']}")
        print(f"Identidad: {lista_personajes[i]['identidad']}")
        print(f"Empresa: {lista_personajes[i]['empresa']}")
        print(f"Altura: {lista_personajes[i]['altura']}")
        print(f"Peso: {lista_personajes[i]['peso']}")
        print(f"Genero: {lista_personajes[i]['genero']}")
        print(f"Color de ojos: {lista_personajes[i]['color_ojos']}")
        print(f"Color de pelo: {lista_personajes[i]['color_pelo']}")
        print(f"Fuerza: {lista_personajes[i]['fuerza']}")
        print(f"Inteligencia: {lista_personajes[i]['inteligencia']}\n")


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

    promedio_peso = acumulador_peso / contador_hombres

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
        "5. mostrar el nombre y peso de los superhéroes  los cuales su fuerza supere a la fuerza promedio de todas las superhéroes de género femenino"
        ]

def mostrar_menu():
    for opcion in menu:
        print(opcion)

seguir = True
while seguir == True:
    mostrar_menu()
    respuesta = int(input("Ingrese una opcion: "))
    match respuesta:
        case 1:
            mostrar_lista()
        case 2:
            mostrar_mas_fuerte()
        case 3:
            mostrar_mas_bajo()
        case 4:
            mostrar_peso_promedio_m()
        case 5:
            mostrar_fuerza_mayor_promedio_f()