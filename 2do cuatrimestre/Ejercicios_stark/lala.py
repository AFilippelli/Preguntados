from data_stark import lista_personajes
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
'''
def imprimir_datos_superheroe(personaje):
    for clave, valor in personaje.items():
        print(f"{clave}: {valor}")
    print()

def mostrar_datos_heroes():

    for heroe in lista_personajes:
        imprimir_datos_superheroe(heroe)

mostrar_datos_heroes()



