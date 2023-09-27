#Adrian Filippelli - 1B - Ejercicio integrador 01
from data_stark_00 import lista_personajes
from os import system

def mostrar_nombres_superheroes():
    #B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
    for i in range(len(lista_personajes)):
        print(f"{i+1}->{lista_personajes[i]['nombre']}\n")

def mostrar_nombres_altura(): 
    #C. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a
    #la altura del mismo
    for heroe in lista_personajes:
        print(f"------------------------------\nnombre: {heroe['nombre']}\naltura: {heroe['altura']}")

def mostrar_superheroe_mas_alto():
    #D. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
    flag_mas_alto = True

    for heroe in lista_personajes:
        altura = float(heroe['altura'])
        if flag_mas_alto == True or altura > maxima_altura:
            maxima_altura = altura
            flag_mas_alto = False 

    for heroe in lista_personajes:
        altura = float(heroe['altura'])
        if altura == maxima_altura:
            print(f"------------------------------\nel mas alto es: {heroe['nombre']}\n")

def mostrar_superheroe_mas_bajo():
    #E. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
    flag_mas_petiso = True

    for heroe in lista_personajes:
        altura = float(heroe['altura'])
        if flag_mas_petiso == True or altura < minima_altura:
            minima_altura = altura
            heroe_mas_petiso = heroe['nombre']
            flag_mas_petiso = False
    for heroe in lista_personajes: 
        altura = float(heroe['altura'])
        if altura == minima_altura:
            print(f"------------------------------\nel mas bajo es:{heroe_mas_petiso}\n")

def mostrar_promedio_altura_superheroes():
    #F. Recorrer la lista y determinar la altura promedio de los superhéroes
    #(PROMEDIO)
    acumulador_altura = 0
    
    for heroe in lista_personajes:
        acumulador_altura +=  float(heroe['altura'])
        contar_altura = len(lista_personajes)
        promedio_altura = acumulador_altura / contar_altura
        
    print(f"------------------------------\nEl promedio de altura es: {promedio_altura}\n")


def mostrar_nombre_superheroes_bajos_y_altos():
    #G. Informar cual es el Nombre del superhéroe asociado a cada uno de los
    #indicadores anteriores (MÁXIMO, MÍNIMO)
    flag_mas_alto = True
    
    for heroe in lista_personajes:
        altura = float(heroe['altura'])
        if flag_mas_alto == True or altura > maxima_altura:
            maxima_altura = altura
            heroe_mas_alto = heroe['nombre']
            flag_mas_alto = False
    for heroe in lista_personajes:
        altura = float(heroe['altura'])
        if altura == maxima_altura:
            print(f"------------------------------\nel mas alto es: {heroe_mas_alto} y mide: {maxima_altura}")
    
    flag_mas_petiso = True

    for heroe in lista_personajes:
        altura = float(heroe['altura'])
        if flag_mas_petiso == True or altura < minima_altura:
            minima_altura = altura
            heroe_mas_petiso = heroe['nombre']
            flag_mas_petiso = False
    for heroe in lista_personajes: 
        altura = float(heroe['altura'])
        if altura == minima_altura:       
            print(f"------------------------------\nel mas bajo es:{heroe_mas_petiso} y mide: {minima_altura}\n")

def mostrar_superheroe_mas_pesado_y_mas_flaco():  
    #H. Calcular e informar cual es el superhéroe más y menos pesado. 
    #Super heroe mas pesado
    flag_mas_gordo = True
        
    for heroe in lista_personajes:
        peso = float(heroe['peso'])
        if flag_mas_gordo == True or peso > maximo_peso:
            maximo_peso = peso
            heroe_mas_gordo = heroe['nombre']
            flag_mas_gordo = False
    for heroe in lista_personajes: 
        peso = float(heroe['peso']) 
        if peso == maximo_peso:  
            print(f"------------------------------\nel mas pesado es: {heroe_mas_gordo} -> {maximo_peso}")
    
    #Super heroe mas flaco
    flag_mas_flaco = True

    for heroe in lista_personajes:
        peso = float(heroe['peso'])
        if flag_mas_flaco == True or peso < minimo_peso:
            minimo_peso = peso
            heroe_mas_flaco = heroe['nombre']
            flag_mas_flaco = False
    for heroe in lista_personajes: 
        peso = float(heroe['peso'])
        if peso == minimo_peso:   
            print(f"------------------------------\nel menos pesado es: {heroe_mas_flaco} -> {minimo_peso}\n")


menu = ["1. mostrar nombres", "2. mostrar nombres con alturas", "3. mostrar superheroe mas alto",
        "4. mostrar superheroe mas bajo", "5. mostrar promedio altura", "6. Mostrar nombre del superheroe mas alto y mas bajo",
        "7. mostrar superheroe mas pesado y mas flaco"]

def mostrar_menu():
    for opcion in menu:
        print(opcion)

seguir = True
while seguir == True:
    mostrar_menu()

    respuesta = int(input("Ingrese una opcion: "))
    match respuesta:
        case 1:
            mostrar_nombres_superheroes()
        case 2:
            mostrar_nombres_altura()
        case 3:
            mostrar_superheroe_mas_alto()
        case 4:
            mostrar_superheroe_mas_bajo()
        case 5:
            mostrar_promedio_altura_superheroes()
        case 6: 
            mostrar_nombre_superheroes_bajos_y_altos()
        case 7:    
            mostrar_superheroe_mas_pesado_y_mas_flaco()
        case 8:    
            seguir = False







