 '''
Adrian Filippelli - Clase 3 - 1B
Es la gala final de Gran Hermano y la producción nos pide un programa para contar
los votos de los televidentes y saber cuál será el participante que ganará el juego.
Los participantes finalistas son: Nacho, Julieta y Marcos.
El televidente debe ingresar:
● Nombre del votante
● Edad del votante (debe ser mayor a 13)
● Género del votante (masculino, femenino, otro)
● El nombre del participante a quien le dará el voto positivo.
No se sabe cuántos votos entrarán durante la gala.
Se debe informar al usuario:
A. El promedio de edad de las votantes de género femenino
B. Cantidad de personas de género masculino entre 25 y 40 años que votaron a
Nacho o Julieta.
C. Nombre del votante más joven que votó a Nacho.
D. Nombre de cada participante y porcentaje de los votos qué recibió.
E. El nombre del participante que ganó el reality (El que tiene más votos)
'''

contador_f = 0
contador_m_nacho_julieta = 0
bandera_edad = 0
contador_julieta = 0
contador_nacho = 0
contador_marcos = 0
cont_votos_totales = 0
promedio_edad_f = 0
nombre_menor = ''
respuesta = "si"

while respuesta == "si":
    nombre_votante = input('Ingrese su nombre y apellido: ')

    edad = int(input('Ingrese su edad: '))
    while edad < 13 or edad > 99:
        edad = int(input('Error!! Reingrese una edad valida: '))
    
    genero = input('Ingrese su genero: "masculino", " femenino" u "otro": ')
    while genero != 'masculino' and genero != 'femenino' and genero != 'otro':
        genero = input('Error!! Reingrese su genero: "masculino", " femenino" u "otro": ')

    participante = input('Ingrese nombre del participante que votara: "julieta", "marcos" o "nacho": ')
    while participante != 'julieta' and participante != 'marcos' and participante != 'nacho':
        participante = input('Error!! Reingrese nombre del participante que votara: "julieta", "marcos" o "nacho": ')

    if genero == 'femenino':
        contador_f += 1
        promedio_edad_f = edad / contador_f
    elif genero == 'masculino' and (edad < 40 and edad > 25) and (participante == 'julieta' or participante == 'nacho'):
        contador_m_nacho_julieta += 1
    
    if participante == 'nacho':
        if bandera_edad == 0:
            bandera_edad = 1
            edad_menor = edad
            nombre_menor = nombre_votante
        elif edad < edad_menor:
            edad_menor = edad
            nombre_menor = nombre_votante

    match participante:
        case 'julieta':
            contador_julieta = contador_julieta + 1
        case 'nacho':
            contador_nacho = contador_nacho + 1
        case _:
            contador_marcos = contador_marcos + 1

    if contador_julieta > contador_marcos and contador_julieta > contador_nacho:
        ganador = 'julieta'
    elif contador_nacho > contador_marcos:
        ganador = 'nacho'
    else: 
        ganador = 'marcos'

    cont_votos_totales = cont_votos_totales + 1

    respuesta = input('Desea continuar? si/no')
    

promedio_j = contador_julieta * 100 / cont_votos_totales
promedio_m = contador_marcos * 100 / cont_votos_totales
promedio_n = contador_nacho * 100 / cont_votos_totales

print (f'El promedio de edad de las votantes de género femenino: {promedio_edad_f}')
print (f'Cantidad de personas de género masculino entre 25 y 40 años que votaron a Nacho o Julieta: {contador_m_nacho_julieta}')
print (f'Nombre del votante más joven que votó a Nacho: {nombre_menor}')
print (f'Porcentaje de los votos qué recibió Julieta: {promedio_j}')
print (f'Porcentaje de los votos qué recibió Marcos: {promedio_m}')
print (f'Porcentaje de los votos qué recibió Nacho: {promedio_n}')
print (f'El nombre del participante que ganó el reality: {ganador}')