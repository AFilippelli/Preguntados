from desafio_stark03 import *
from desafio_stark02 import mostrar_menu

mostrar_menu()

def stark_menu_marvel (lista_personajes: list):
    '''
    esta funcion muestra el resultado de la opcion que el usuario elija
    Args:
    lista_personajes(list): Una lista de diccionarios que representan objetos (héroes)
    '''
    flag_normalizada = False
    opcion = -1
    while opcion != 11:
        opcion = stark_menu_principal()
        if opcion == '1':
            flag_normalizada = True
            lista_claves = ["altura", "fuerza", "peso"]
            stark_normalizar_datos(lista_personajes, lista_claves)
        elif flag_normalizada:
            if opcion == "2":
                print("Dic del heroe mas alto: ")
                print(obtener_dato_cantidad(lista_personajes, 1, "altura"))
            elif opcion == '3':
                print("Dic del heroe mas pesado: ")
                print(obtener_dato_cantidad(lista_personajes,1, "peso"))
            elif opcion == '4':
                print("Dic del heroe mas fuerte: ")
                print(obtener_dato_cantidad(lista_personajes,1, "fuerza"))
            elif opcion == '5':
                print("Dic del heroe menos alto: ")
                print(obtener_dato_cantidad(lista_personajes,2, "altura"))
            elif opcion == '6':
                print("Dic del heroe menos pesado: ")
                print(obtener_dato_cantidad(lista_personajes,2,"peso"))
            elif opcion == '7':
                print("Dic del heroe menos fuerte: ")
                print(obtener_dato_cantidad(lista_personajes,2,"fuerza"))
            elif opcion == '8':
                print("El promedio de altura es: ")
                print(calcular_promedio(lista_personajes, "altura"))
            elif opcion == '9':
                print("El promedio de peso es: ")
                print(calcular_promedio(lista_personajes, "peso"))
            elif opcion == '10':
                print("El promedio de fuera es: ")
                print(calcular_promedio(lista_personajes, "fuerza"))
            elif opcion == '11':
                break
            else:
                print("opcion incorrecta, intente nuevamente")
        else:
            print("Error, ingrese 1 para normalizar los datos antes de continuar")



'''
menu = ["0. Normalizar datos",
        "1. Mostrar nombre de los no binarios", 
        "2. Mostrar superheroina mas alta",
        "3. Mostrar superheroe mas alto", 
        "4. Mostrar superheroe masculino mas debil",
        "5. Mostrar superheroe no binario mas debil", 
        "6. Mostrar fuerza promedio genero no binario",
        "7. Mostrar cantidad de tipos de color de ojos",
        "8. Mostrar cantidad de tipos de color de pelo",
        "9. Mostrar superheroes agrupados por color de ojos",
        "10. Mostrar superheroes agrupados por tipo de inteligencia",
        "11. Salir"
        ]

def mostrar_menu():
    for opcion in menu:
        print(opcion)

seguir = True
while seguir == True:
    flag_normalizada = False
    mostrar_menu()
    respuesta = input("Ingrese una opcion: ")
    while respuesta != "0" and "1" and respuesta != "2" and respuesta != "3" and respuesta != "4" and respuesta != "5" and respuesta != "6" and respuesta != "7" and respuesta != "8" and respuesta != "9" and respuesta != "10" and respuesta != "11":
        respuesta = stark_menu_principal()
        if respuesta == "0":
            flag_normalizada = True
            lista_claves = ["altura", "fuerza", "peso"]
            stark_normalizar_datos(lista_personajes, lista_claves)
        elif flag_normalizada:
            if respuesta == "1":
                mostrar_nombre_nb
            if respuesta == "2":
                dic_retornado_mas_alto = calcular_mas_alto(lista_personajes, 'altura', 'F') 
                mostrar_mas_alto(dic_retornado_mas_alto)
            elif respuesta == "3":
                dic_retornado_mas_alto = calcular_mas_alto(lista_personajes, 'altura', 'M')
                mostrar_mas_alto(dic_retornado_mas_alto)
            elif respuesta == "4":
                dic_retornado_mas_debil = calcular_mas_debil(lista_personajes, 'fuerza', 'M')
                mostrar_mas_debil(dic_retornado_mas_debil)
            elif respuesta == "5":
                dic_retornado_mas_debil = calcular_mas_debil(lista_personajes, 'fuerza', 'NB')
                mostrar_mas_debil(dic_retornado_mas_debil)
            elif respuesta == "6": 
                mostrar_fuerza_promedio_nb()
            elif respuesta == "7":
                calcular_ojos_color()
            elif respuesta == "8": 
                calcular_pelos_color()   
            elif respuesta == "9":
                lista_color_ojos()
            elif respuesta == "10":
                lista_tipo_inteligencia()  
            elif respuesta == "11":
                break
        else:
            print("Error, ingrese 1 para normalizar los datos antes de continuar")
'''