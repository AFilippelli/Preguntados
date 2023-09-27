
# La función deberá devolver a partir del parámetro recibido un nuevo string con
# las iniciales del nombre del personaje seguidos por un punto (.)

# La función deberá validar:


# Ejemplo de la salida de la función para Howard the Duck:
# H.D.

from data_stark_00 import lista_personajes
from os import system
system("cls")

def extraer_iniciales(nombre_heroe: str):
    if nombre_heroe.strip() == "":
        return "N/A"
    
    if "the" in nombre_heroe.lower():
        nombre_heroe = nombre_heroe.lower().replace("the", "")

    nombre_heroe = nombre_heroe.replace("-", " ")    

    iniciales = ""
    for palabra in nombre_heroe.split():
        iniciales += palabra[0].upper() + "."
    return iniciales

hola = extraer_iniciales("Howard the Duck")
print(hola)

# 1.2. Crear la función ‘definir_iniciales_nombre’ la cual recibirá como parámetro:
# ● heroe: un diccionario con los datos del personaje

# La función deberá agregar una nueva clave al diccionario recibido como
# parámetro. La clave se deberá llamar ‘iniciales’ y su valor será el obtenido de
# llamar a la función ‘extraer_iniciales’
# La función deberá validar:
# ● Que el diccionario contengan la clave ‘nombre’
# En caso de encontrar algún error retornar False, caso contrario retornar True

def definir_iniciales_nombre(heroe: dict):
    if not isinstance(heroe, dict) or "nombre" not in heroe:
        return False
    else:
        heroe["iniciales"] = extraer_iniciales(heroe["nombre"])
        return True

heroe = {'nombre': 'Spider-Man'}
resultado = definir_iniciales_nombre(heroe)
print(resultado)
print(heroe)        
