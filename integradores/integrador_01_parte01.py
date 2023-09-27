#Adrian Filippelli - 1B - Ejercicio integrador 01
from data_stark_01 import lista_personajes
from os import system


# 1 A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
# género M
def mostrar_heroes_género_masculino(genero):
    for heroe in lista_personajes:    
        if heroe["genero"] == genero == "M":
            print(f"superheroe: {heroe['nombre']}")

# 2 B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
# género F        
def mostrar_heroes_genero_femenino(genero):
    for heore in lista_personajes:    
        if heore["genero"] == genero == "F":
            print(f"Superheroína: {heore['nombre']}")


def mostrar_alto_m_f(genero):
    flag_mas_alto = True

    for heroe in lista_personajes:
        if flag_mas_alto == True or float(heroe['altura']) > heroe_alto and heroe['genero'] == genero == 'M':
            flag_mas_alto = False
            heroe_alto = float(heroe['altura'])
            nombre_alto = heroe['nombre']
        elif flag_mas_alto == True or float(heroe['altura']) > heroe_alto and heroe['genero'] == genero == 'F':
            flag_mas_alto = False
            heroe_alto = float(heroe['altura'])
            nombre_alto = heroe['nombre']
    
    print(f'El mas alto es:\n{nombre_alto} --- {heroe_alto} cm\n----------------')

    return genero


def mostrar_mas_bajo_m_f(genero):
    flag_mas_bajo = True

    for heroe in lista_personajes:
        if flag_mas_bajo == True or float(heroe['altura']) < heroe_bajo and heroe['genero'] == genero == 'M':
            flag_mas_bajo = False
            heroe_bajo = float(heroe['altura'])
            nombre_bajo = heroe["nombre"]
        elif flag_mas_bajo == True or float(heroe['altura']) < heroe_bajo and heroe['genero'] == genero == 'F':
            flag_mas_bajo = False
            heroe_bajo = float(heroe['altura'])
            nombre_bajo = heroe["nombre"]
    
    print(f'Mas bajo:\n{nombre_bajo} --- Altura: {heroe_bajo} cm\n----------------')

    return genero       


def mostrar_altura_promedio(genero):
    contador_heroes = 0
    acumulador_altura = 0

    for heroe in lista_personajes:

        altura = float(heroe['altura'])

        if heroe['genero'] == genero == 'F':
            acumulador_altura += altura
            contador_heroes += 1
        elif heroe['genero'] == genero == 'M':
            acumulador_altura += altura
            contador_heroes += 1
    
    promedio_altura = acumulador_altura / contador_heroes

    print (f'----------------------------\nEl promedio de altura es: {promedio_altura:.2f} cm\n----------------------------')

    return genero


def mostrar_nombre_genero_m_f(genero):
    for heroe in lista_personajes:
        if heroe['genero'] == genero:
            print(f'-------------------\n{heroe["nombre"]} -- Genero: {genero}\n-------------------')


def mostrar_ojos_color():
    lista = []
    for heroe in lista_personajes:
        ojos = heroe["color_ojos"]
        lista.append(ojos)
    set_lista_ojos = set(lista) 

    return set_lista_ojos


def calcular_tipos_ojos():
    tipos_ojos = mostrar_ojos_color()
    cantidad_tipos_de_ojos = []
    for ojo in tipos_ojos:
        contador = 0
        cantidad_ojos = {}
        for heroe in lista_personajes:
            ojos = heroe["color_ojos"]
            if ojos == ojo:
                contador = contador + 1
        cantidad_ojos[ojo] = contador        
        cantidad_tipos_de_ojos.append(cantidad_ojos)  
    print(f'{cantidad_tipos_de_ojos}')


def mostrar_pelo_color():
    lista = []
    for heroe in lista_personajes:
        pelos = heroe["color_pelo"]
        lista.append(pelos)
    set_lista_pelo = set(lista) 

    return set_lista_pelo


def calcular_tipos_pelo():
    tipos_pelo = mostrar_pelo_color()
    cantidad_tipos_de_pelo = []
    for pelo in tipos_pelo:
        contador = 0
        cantidad_pelos = {}
        for heroe in lista_personajes:
            pelos = heroe["color_ojos"]
            if pelos == pelo:
                contador = contador + 1
        cantidad_pelos[pelo] = contador        
        cantidad_tipos_de_pelo.append(cantidad_pelos)  
    print(f'{cantidad_tipos_de_pelo}')


def mostrar_inteligencia():
    lista = []
    for heroe in lista_personajes:
        iq = heroe["inteligencia"]
        lista.append(iq)
    set_lista_inteligencia = set(lista) 

    return set_lista_inteligencia   


def calcular_tipo_inteligencia():
    tipos_inteligencia = mostrar_inteligencia()
    cantidad_tipos_inteligencia = []
    for inteligencia in tipos_inteligencia:
        contador = 0
        contador_cero_iq = 0
        cantidad_inteligencia = {}
        for heroe in lista_personajes:
            iq = heroe["inteligencia"]
            if iq == inteligencia == '':
                contador_cero_iq = contador_cero_iq + 1
                print(f'{contador_cero_iq} un superheroe no posee un nivel de inteligencia')
            elif iq == inteligencia:
                contador = contador + 1
        cantidad_inteligencia[inteligencia] = contador
        cantidad_tipos_inteligencia.append(cantidad_inteligencia)  
    print(f'{cantidad_tipos_inteligencia}')       


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

    return heroes_ojos            


def lista_color_pelo():
    set_pelo = mostrar_pelo_color()
    heroes_pelo = {}

    for pelo in set_pelo:
        lista_heroes = []
        for heroe in lista_personajes:
            pelos = heroe["color_pelo"]
            if pelos == pelo:
                lista_heroes.append(heroe["nombre"])

        heroes_pelo[pelo] = lista_heroes
    print(heroes_pelo)

    return heroes_pelo 


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

    return heroes_inteligencia         


menu = ["1. mostrar superheroes hombres", 
        "2. mostrar superheroes mujeres",
        "3. mostrar superheroe hombre mas alto", 
        "4. mostrar superheroe mujer más alta",
        "5. mostrar superheroe hombre mas bajo", 
        "6. Mostrar superheroe mujer mas baja",
        "7. mostrar altura promedio de superheroes hombres",
        "8. mostrar altura promedio de superheroes mujeres",
        "9. Mostrar datos anteriores con nombres de los superheroes",
        "10. Mostrar cuantos superheroes tienen cada tipo de color de ojos",
        "11. Mostrar cuantos superheroes tienen cada tipo de color de pelo",
        "12. Mostrar inteligencia de cada heroe",
        "13. Mostrar todos los superheroes agrupados por color de ojos",
        "14. Mostrar todos los superheroes agrupados por color de pelo",
        "15. Mostrar todos los superheroes agrupados por tipo de inteligencia"]


def mostrar_menu():
    for opcion in menu:
        print(opcion)

seguir = True
while seguir == True:
    mostrar_menu()
    respuesta = int(input("Ingrese una opcion: "))
    match respuesta:
        case 1:
            mostrar_heroes_género_masculino("M")
        case 2:
            mostrar_heroes_genero_femenino("F")
        case 3:
            mostrar_alto_m_f("M")
        case 4:
            mostrar_alto_m_f("F")
        case 5:
            mostrar_mas_bajo_m_f("M")
        case 6: 
            mostrar_mas_bajo_m_f("F")
        case 7:
            mostrar_altura_promedio("M")
        case 8: 
            mostrar_altura_promedio("F")    
        case 9:
            mostrar_nombre_genero_m_f("M")
        case 10:
            mostrar_nombre_genero_m_f("F")    
        case 11:
            calcular_tipos_ojos()
        case 12:
            calcular_tipos_pelo()
        case 13:
            calcular_tipo_inteligencia()
        case 14:
            lista_color_ojos()
        case 15:
            lista_color_pelo()
        case 16:
            lista_tipo_inteligencia()
        case 17:                
            seguir = False