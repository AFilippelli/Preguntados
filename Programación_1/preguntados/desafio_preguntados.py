ANCHO_VENTANA = 800
ALTO_VENTANA = 600
COLOR_ROJO = (255,0,0)
COLOR_AZUL = (0,0,128)
COLOR_BLANCO = (255,255,255)
COLOR_GRIS = (128,128,128)
COLOR_NEGRO = (0,0,0)
import pygame
from data_preguntados import lista_preguntados
lista_preguntas = []
lista_opcion_a = []
lista_opcion_b = []
lista_opcion_c = []
lista_correcta = []
posicion = 0
score = 0
errores = 0
pregunta = ""
opcion_a = ""
opcion_b = ""
opcion_c = ""
correcta = ""
posicion_imagen = [10,10]
bandera_reinicio = False


for lista in lista_preguntados:
    lista_preguntas.append(lista['pregunta'])
    lista_opcion_a.append(lista['a'])
    lista_opcion_b.append(lista['b'])
    lista_opcion_c.append(lista['c'])
    lista_correcta.append(lista['correcta'])

print(lista_preguntas)
print(lista_opcion_a)
print(lista_opcion_b)
print(lista_opcion_c)
print(lista_correcta)

pygame.init()
#creo la pantalla en una variable y le agrego el largo y ancho
pantalla = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA)) #va entre 2 parentesis

#Para crear un titulo:
pygame.display.set_caption("Preguntados")

imagen = pygame.image.load("preguntados.png")  #cargamos una imagen y la asignamos a una variable con el nombre "imagen"
imagen = pygame.transform.scale(imagen,(200,200))  #si queremos cambiarle el tamaño a la imagen seleccionada, hay que hacer lo siguiente

#Definir un texto
fuente = pygame.font.SysFont("Arial", 25)
fuente_dos = pygame.font.SysFont("Arial", 40)
texto_pregunta = fuente_dos.render(str("Pregunta"), True, COLOR_NEGRO) #(el true es para que recorte bien las letras)
texto_reiniciar = fuente_dos.render(str("Reiniciar"), True, COLOR_NEGRO)
texto_score = fuente_dos.render(str("Score: "), True, COLOR_GRIS)
texto_puntaje = fuente.render(str(score),True, COLOR_GRIS)
texto_preguntas = fuente.render(str(pregunta), True, COLOR_GRIS)
texto_opcion_a = fuente.render(str(opcion_a), True, COLOR_GRIS)
texto_opcion_b = fuente.render(str(opcion_b), True, COLOR_GRIS)
texto_opcion_c = fuente.render(str(opcion_c), True, COLOR_GRIS)

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

            if posicion < len(lista_preguntas):
                if (posicion_click[0] > 300 and posicion_click[0] < 500) and (posicion_click[1] > 20 and posicion_click[1] < 120):
                    bandera_reinicio = False
                    pregunta = lista_preguntas[posicion]
                    opcion_a = lista_opcion_a[posicion]
                    opcion_b = lista_opcion_b[posicion]
                    opcion_c = lista_opcion_c[posicion]
                    correcta = lista_correcta[posicion]

                    texto_opcion_a = fuente.render(str(opcion_a), True, COLOR_GRIS)
                    texto_opcion_b = fuente.render(str(opcion_b), True, COLOR_GRIS)
                    texto_opcion_c = fuente.render(str(opcion_c), True, COLOR_GRIS)
                    errores = 0
                    posicion = posicion + 1
        
                if bandera_reinicio == False:
                    if errores == 2:
                        texto_opcion_a = fuente.render(str(''), True, COLOR_GRIS)
                        texto_opcion_b = fuente.render(str(''), True, COLOR_GRIS)
                        texto_opcion_c = fuente.render(str(''), True, COLOR_GRIS)

                    else:
                        if (posicion_click[0] > 10 and posicion_click[0] < 205) and (posicion_click[1] > 340 and posicion_click[1] < 390):  
                            if correcta == "a":  
                                score += 10
                                pregunta = lista_preguntas[posicion]
                                opcion_a = lista_opcion_a[posicion]
                                opcion_b = lista_opcion_b[posicion]
                                opcion_c = lista_opcion_c[posicion]
                                correcta = lista_correcta[posicion]
                                posicion = posicion + 1
                                texto_opcion_a = fuente.render(str(opcion_a), True, COLOR_GRIS)
                                texto_opcion_b = fuente.render(str(opcion_b), True, COLOR_GRIS)
                                texto_opcion_c = fuente.render(str(opcion_c), True, COLOR_GRIS)
                                errores = 0
                            else:
                                texto_opcion_a = fuente.render(str(''), True, COLOR_GRIS)
                                errores += 1

                        elif (posicion_click[0] > 220 and posicion_click[0] < 415) and (posicion_click[1] > 340 and posicion_click[1] < 390):
                            if correcta == "b":    
                                score += 10
                                pregunta = lista_preguntas[posicion]
                                opcion_a = lista_opcion_a[posicion]
                                opcion_b = lista_opcion_b[posicion]
                                opcion_c = lista_opcion_c[posicion]
                                correcta = lista_correcta[posicion]
                                posicion = posicion + 1
                                texto_opcion_a = fuente.render(str(opcion_a), True, COLOR_GRIS)
                                texto_opcion_b = fuente.render(str(opcion_b), True, COLOR_GRIS)
                                texto_opcion_c = fuente.render(str(opcion_c), True, COLOR_GRIS)
                                errores = 0
                            else:
                                texto_opcion_b = fuente.render(str(''), True, COLOR_GRIS)
                                errores += 1


                        elif(posicion_click[0] > 430 and posicion_click[0] < 640) and (posicion_click[1] > 340 and posicion_click[1] < 390):
                            if correcta == "c":    
                                score += 10
                                pregunta = lista_preguntas[posicion]
                                opcion_a = lista_opcion_a[posicion]
                                opcion_b = lista_opcion_b[posicion]
                                opcion_c = lista_opcion_c[posicion]
                                correcta = lista_correcta[posicion]
                                posicion = posicion + 1
                                texto_opcion_a = fuente.render(str(opcion_a), True, COLOR_GRIS)
                                texto_opcion_b = fuente.render(str(opcion_b), True, COLOR_GRIS)
                                texto_opcion_c = fuente.render(str(opcion_c), True, COLOR_GRIS)
                                errores = 0
                            else:
                                texto_opcion_c = fuente.render(str(''), True, COLOR_BLANCO)
                                errores += 1

            else:
                posicion = 0
                score = 0
                texto_opcion_a = fuente.render(str(''), True, COLOR_GRIS)
                texto_opcion_b = fuente.render(str(''), True, COLOR_GRIS)
                texto_opcion_c = fuente.render(str(''), True, COLOR_GRIS)
                bandera_reinicio = True
            
            if (posicion_click[0] > 300 and posicion_click[0] < 495) and (posicion_click[1] > 475 and posicion_click[1] < 575):
                    posicion = 0
                    score = 0
                    texto_opcion_a = fuente.render(str(''), True, COLOR_GRIS)
                    texto_opcion_b = fuente.render(str(''), True, COLOR_GRIS)
                    texto_opcion_c = fuente.render(str(''), True, COLOR_GRIS)
                    texto_puntaje = fuente.render(str(score), True, COLOR_GRIS)
                    bandera_reinicio = True

    print(bandera_reinicio)
    if bandera_reinicio == False:
        texto_preguntas = fuente.render(str(pregunta), True, COLOR_GRIS)
        texto_puntaje = fuente.render(str(score), True, COLOR_GRIS)
    else:
        texto_preguntas = fuente.render(str(''), True, COLOR_GRIS)


    #elijo el color rojo para el fondo de la pantalla
    pantalla.fill(COLOR_AZUL)
    pygame.draw.rect(pantalla,COLOR_BLANCO,(10,340,195,50))
    pygame.draw.rect(pantalla,COLOR_BLANCO,(220,340,195,50))
    pygame.draw.rect(pantalla,COLOR_BLANCO,(430,340,210,50))
    pygame.draw.rect(pantalla,COLOR_BLANCO,(300,20,200,100)) #LEFT, TOP, ANCHO Y ALTO
    pygame.draw.rect(pantalla,COLOR_BLANCO,(300,475,200,100)) #LEFT, TOP, ANCHO Y ALTO
    pantalla.blit(imagen,(posicion_imagen),) #fundimos la imagen en la superficie pantalla
    pantalla.blit(texto_pregunta,(320,45))
    pantalla.blit(texto_reiniciar,(320,500))
    pantalla.blit(texto_score,(320,150))
    pantalla.blit(texto_preguntas,(20,280))
    pantalla.blit(texto_opcion_a,(10,350))
    pantalla.blit(texto_opcion_b,(220,350))
    pantalla.blit(texto_opcion_c,(430,350))
    pantalla.blit(texto_puntaje,(320,195))
    pygame.display.flip() #para actualizar el contenido en pantalla

pygame.quit()