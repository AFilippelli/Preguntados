'''
Desafío #02:
Usando como base lo realizado en el anterior desafío realizar los siguientes
informes en un menú
A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
género NB
B. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
D. Recorrer la lista y determinar cuál es el superhéroe más débil de género M
E. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
F. Recorrer la lista y determinar la fuerza promedio de los superhéroes de
género NB
G. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
H. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
I. Listar todos los superhéroes agrupados por color de ojos.
J. Listar todos los superhéroes agrupados por tipo de inteligencia

'''
from data_stark import lista_personajes

#PUNTO A
def mostrar_nombre_nb():
    for heroe in lista_personajes:
        if heroe["genero"] == "NB":
            print(f"Nombre -> {heroe['nombre']}")


'''
#PUNTO B
def calcular_mas_alta_femenina():

    flag_mas_alta = True

    for heroe in lista_personajes:
        if flag_mas_alta == True or float(heroe['altura']) > heroina_alta and heroe['genero'] == "F":
            flag_mas_alta = False
            heroina_alta = float(heroe['altura'])
            nombre_alta = heroe['nombre']
    
    print(f"La heroina mas alta es: {nombre_alta} y mide: {heroina_alta}cm")
'''

'''
#PUNTO C
def calcular_mas_alto_masculino():

    flag_mas_alto = True

    for heroe in lista_personajes:
        if flag_mas_alto == True or float(heroe['altura']) > heroe_alto and heroe['genero'] == "M":
            flag_mas_alto = False
            heroe_alto = float(heroe['altura'])
            nombre_alto = heroe['nombre']
    
    print(f"El heroe mas alto es: {nombre_alto} y mide: {heroe_alto}cm")
'''
#PUNTOS B Y C
def mostrar_mas_alto(heroe:dict):
    print("Heroe mas alto -> altura: {0} Nombre: {1}".format(heroe['altura'], heroe['nombre']))

dic_retornado_mas_alto = {}

def calcular_mas_alto(lista_recibida:list, altura:float, genero:str):
    dic_mas_alto = lista_recibida[0]
    flag_mas_alto = True

    for heroe in lista_recibida:
        if flag_mas_alto == True or float(heroe[altura]) > float(dic_mas_alto[altura]) and heroe['genero'] == genero:
            flag_mas_alto = False
            dic_mas_alto = heroe

    return dic_mas_alto

#PUNTOS D Y E
def mostrar_mas_debil(heroe:dict):
    print("Heroe mas debil -> fuera: {0} Nombre: {1}".format(heroe['fuerza'], heroe['nombre']))

dic_retornado_mas_debil = {}

def calcular_mas_debil(lista_recibida:list, fuerza:float, genero:str):
    dic_mas_debil = lista_recibida[0]
    flag_mas_debil = True

    for heroe in lista_recibida:
        if flag_mas_debil == True or float(heroe[fuerza]) > float(dic_mas_debil[fuerza]) and heroe['genero'] == genero:
            flag_mas_debil = False
            dic_mas_debil = heroe

    return dic_mas_debil


'''
#PUNTO D
def calcular_debil_masculino():
    flag_mas_debil = True

    for heroe in lista_personajes:
        if flag_mas_debil == True or float(heroe['fuerza']) < fuerza_debil and heroe['genero'] == "M":
            flag_mas_debil = False
            fuerza_debil = float(heroe['fuerza'])
            nombre_debil = heroe['nombre']
    
    print(f"El heroe mas debil es {nombre_debil} y su fuerza es de: {fuerza_debil}")
'''

'''
#PUNTO E
def calcular_debil_nb():
    flag_mas_debil_nb = True


    for heroe in lista_personajes:
        if flag_mas_debil_nb == True or float(heroe['fuerza']) < fuerza_debil_nb and heroe["genero"] == "NB":
            flag_mas_debil_nb = False
            fuerza_debil_nb = float(heroe['fuerza'])
            nombre_debil_nb = heroe['nombre']
    
    print(f"El heroe mas debil no binario es: {nombre_debil_nb} y su fuerza es de: {fuerza_debil_nb}")
'''


#PUNTO F
def mostrar_fuerza_promedio_nb():
    contador_no_binarios = 0
    acumulador_fuerza = 0

    for heroe in lista_personajes:

        fuerza = float(heroe['fuerza'])

        if heroe['genero'] == 'NB':
            acumulador_fuerza += fuerza
            contador_no_binarios += 1

    promedio_fuerza = acumulador_fuerza / contador_no_binarios

    print(f"El promedio de la fuerza del genero no binario es: {promedio_fuerza}kg ")


#PUNTO G
def mostrar_ojos_color():
    lista = []
    for heroe in lista_personajes:
        ojos = heroe["color_ojos"]
        lista.append(ojos)
    set_lista_ojos = set(lista) 

    return set_lista_ojos

def calcular_ojos_color():
    tipos_ojos = mostrar_ojos_color()
    cantidad_tipos_ojos = []
    for ojo in tipos_ojos:
        contador = 0
        cantidad_ojos = {}
        for heroe in lista_personajes:
            if heroe["color_ojos"] == ojo:
                contador+= 1
        cantidad_ojos[ojo] = contador
        cantidad_tipos_ojos.append(cantidad_ojos)
    print(f"{cantidad_tipos_ojos}")

#PUNTO H
def mostrar_pelo_color():
    lista = []
    for heroe in lista_personajes:
        pelo = heroe["color_pelo"]
        lista.append(pelo)
    set_lista_pelo = set(lista) 

    return set_lista_pelo

def calcular_pelos_color():
    tipos_pelo = mostrar_pelo_color()
    cantidad_tipos_pelo = []
    for ojo in tipos_pelo:
        contador = 0
        cantidad_pelo = {}
        for heroe in lista_personajes:
            if heroe["color_pelo"] == ojo:
                contador+= 1
        cantidad_pelo[ojo] = contador
        cantidad_tipos_pelo.append(cantidad_pelo)
    print(f"{cantidad_tipos_pelo}")


#PUNTO I
def lista_color_ojos():
    set_ojos = mostrar_ojos_color()
    heroes_ojos = {}

    for ojo in set_ojos:
        lista_heroes = []
        for heroe in lista_personajes:
            ojos = heroe["color_ojos"]
            if ojos == ojo:
                lista_heroes.append(heroe["nombre"])

        heroes_ojos[ojo] = lista_heroes
    print(heroes_ojos)

#PUNTO J
def mostrar_inteligencia():
    lista = []
    for heroe in lista_personajes:
        iq = heroe["inteligencia"]
        lista.append(iq)
    set_lista_inteligencia = set(lista) 

    return set_lista_inteligencia  


def lista_tipo_inteligencia():
    set_inteligencia = mostrar_inteligencia()
    heroes_inteligencia = {}

    for int in set_inteligencia:
        lista_heroes = []
        for heroe in lista_personajes:
            inteligencia = heroe["inteligencia"]
            if inteligencia == int:
                lista_heroes.append(heroe["nombre"])

        heroes_inteligencia[int] = lista_heroes
    print(heroes_inteligencia)





menu = ["1. Mostrar nombre de los no binarios", 
        "2. Mostrar superheroina mas alta",
        "3. Mostrar superheroe mas alto", 
        "4. Mostrar superheroe masculino mas debil",
        "5. Mostrar superheroe no binario mas debil", 
        "6. Mostrar fuerza promedio genero no binario",
        "7. Mostrar cantidad de tipos de color de ojos",
        "8. Mostrar cantidad de tipos de color de pelo",
        "9. Mostrar superheroes agrupados por color de ojos",
        "10.Mostrar superheroes agrupados por tipo de inteligencia",
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
            mostrar_nombre_nb()
        case 2:
            dic_retornado_mas_alto = calcular_mas_alto(lista_personajes, 'altura', 'F') 
            mostrar_mas_alto(dic_retornado_mas_alto)
        case 3:
            dic_retornado_mas_alto = calcular_mas_alto(lista_personajes, 'altura', 'M')
            mostrar_mas_alto(dic_retornado_mas_alto)
        case 4:
            dic_retornado_mas_debil = calcular_mas_debil(lista_personajes, 'fuerza', 'M')
            mostrar_mas_debil(dic_retornado_mas_debil)
        case 5:
            dic_retornado_mas_debil = calcular_mas_debil(lista_personajes, 'fuerza', 'NB')
            mostrar_mas_debil(dic_retornado_mas_debil)
        case 6: 
            mostrar_fuerza_promedio_nb()
        case 7:
            calcular_ojos_color()
        case 8: 
            calcular_pelos_color()   
        case 9:
            lista_color_ojos()
        case 10:
            lista_tipo_inteligencia() 