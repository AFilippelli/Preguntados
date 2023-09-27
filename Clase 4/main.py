

from data import lista_bzrp  
from os import system

def mostrar_lista_temas(lists_bzrp = list):
    #B. Recorrer la lista imprimiendo por consola el título de cada video
    for tema in lista_bzrp:
        print(tema["title"])
def mostrar_lista_temas_views():
    #C. Recorrer la lista imprimiends por consola el título de cada video junto a la
    #cantidad de reproducciones del mismo
    for tema in lista_bzrp:
        print(f"{tema['title']} - {tema['views']}")

def buscar_temas_mas_views():
    #D. Recorrer la lista y determinar cuál es la cantidad máxima de reproducciones
    #MÁXIMO)    
    flag_primero = True
    #for para encontrar el tema con mas views
    for tema in lista_bzrp:
        if flag_primero == True or tema['views'] > maxima_views:
            maxima_views = tema['views']
            flag_primero = False
    #este for sirve para saber si hay mas de un tema con las mismas vistas
    for tema in lista_bzrp:
        if tema['views'] == maxima_views: 
            print(f"{tema['title']}")          

def buscar_temas_menos_views():
    #E. Recorrer la lista y determinar cuál es la cantidad mínima de reproducciones
    #(MÍNIMO)
    flag_primero = True

    for tema in lista_bzrp:
        if flag_primero == True or tema['views'] < minima_views:
            minima_views = tema['views']
            flag_primero = False

    print(f"Cantidad minima de reproduccion: {minima_views}") 
    for tema in lista_bzrp: 
        if tema['views'] == minima_views:    
                print(f"{tema['title']}")

def calcular_promedio():
    #F. Recorrer la lista y determinar la cantidad total de reproducciones del canal
    acumulador_views = 0
    for tema in lista_bzrp:
        acumulador_views += tema['views']

    print(f"Sumatoria de reproducciones: {acumulador_views}")

    #G. Recorrer la lista y determinar la cantidad promedio de reproducciones que
    #tiene un video (PROMEDIO)
    contar_temas = len(lista_bzrp)
    promedio_views = acumulador_views / contar_temas

    print(f"El promedio de vistas es: {promedio_views}")


menu = ["1. Mostrar temas", "2. Mostrar temas con vistas", "3. Mostrar temas mas vistos",
        "4. Mostrar temas menos vistos", "5. Mostrar el promedio de reproducciones", "6. Salir"]


def mostrar_menu():
    for opcion in menu:
        print(opcion)


seguir = True
while seguir == True:
    system("cls")
    mostrar_menu()

    respuesta = int(input("Ingrese una opcion: "))
    match respuesta:
        case 1:
            mostrar_lista_temas()
        case 2:
            mostrar_lista_temas_views()
        case 3:
            buscar_temas_mas_views()  
        case 4:
            buscar_temas_menos_views()
        case 5:
            calcular_promedio()
        case 6: 
            
            seguir = False


    # respuesta = int(input("""1. Mostrar temas
    #                     2. Mostrar temas con vistas
    #                     3. Mostrar temas mas vistos
    #                     4. Mostrar temas menos vistos
    #                     5. Mostrar el promedio de reproducciones
    #                     6. Salir\nElija una opcion: """))













