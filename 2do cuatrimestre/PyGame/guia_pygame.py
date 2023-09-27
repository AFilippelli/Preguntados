ANCHO_VENTANA = 800
ALTO_VENTANA = 600
COLOR_ROJO = (255,0,0)
COLOR_BLANCO = (255,255,255)
COLOR_GRIS = (128,128,128)
import pygame
from data import lista_bzrp
#import constantes
titulo = ""
posicion = 0

posicion_imagen = [30,100]
lista_titulos = []

for e_lista in lista_bzrp:
    lista_titulos.append(e_lista["title"])

#print(lista_titulos)

pygame.init()
#creo la pantalla en una variable y le agrego el largo y ancho
pantalla = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA)) #va entre 2 parentesis

#Para crear un titulo:
pygame.display.set_caption("PyGame")

#cargamos una imagen y la asignamos a una variable con el nombre "imagen"
imagen = pygame.image.load("400.jpg")
#si queremos cambiarle el tamaño a la imagen seleccionada, hay que hacer lo siguiente
imagen = pygame.transform.scale(imagen,(200,200))
#Definir un texto
fuente = pygame.font.SysFont("Arial", 30)
texto_titulo = fuente.render(str(titulo), True, COLOR_GRIS) #(el true es para que recorte bien las letras)



flag_iniciar = True
while flag_iniciar:
    #guardamos en una lista todas las interacciones hechas por el jugador
    lista_eventos = pygame.event.get()
    #recorremos las interacciones del jugador
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_iniciar = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            #nos devuelve una tupla que debemos cambiar a lista para poder manipularla
            posicion_click = list(evento.pos)
            print(posicion_click)
            if (posicion_click[0] > 300 and posicion_click[0] < 500) and (posicion_click[1] > 20 and posicion_click[1] < 120):
                titulo = lista_titulos[posicion]
                texto_titulo = fuente.render(str(titulo), True, COLOR_GRIS)
                if posicion > len(lista_titulos):   #con cada click se imprime un titulo de
                    posicion = 0                    #una cancion, si la cantidad de clicks supera
                else:                               #la cantidad de canciones, la lista vuelve
                    posicion+= 1                    #a empezar


    #elijo el color rojo para el fondo de la pantalla
    pantalla.fill(COLOR_ROJO)
    pygame.draw.rect(pantalla,COLOR_BLANCO,(300,20,200,100)) #LEFT, TOP, ANCHO Y ALTO
    pantalla.blit(imagen,(posicion_imagen),) #fundimos la imagen en la superficie pantalla
    pantalla.blit(texto_titulo,(150,170))
    pygame.display.flip() #para actualizar el contenido en pantalla

pygame.quit()
    