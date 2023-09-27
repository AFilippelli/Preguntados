# Debemos desarrollar un algoritmo que permita computar los votos del Senado de
# Berlinberlín. Se deberá ingresar el nombre de cada senador y si está Presente o no en
# la sesión. Si el senador está presente, se deberá pedir el valor del voto
# El voto de los senadores berliberlineses puede ser Afirmativo, Negativo o Abstención
# (validar). El valor por defecto para los senadores ausentes será Abstención.
# Se deberá Informar:

# o Cantidad total de senadores.
# o Cantidad de senadores presentes.
# o Cantidad y porcentaje de votos afirmativos.
# o Cantidad y porcentaje de votos negativos.
# o Cantidad y porcentaje de abstenciones.
# o Generar una lista de senadores por cada tipo de voto y mostrarlas por
# pantalla.

#contadores
total_senadores = 0
senadores_presentes = 0
cantidad_positivos = 0
cantidad_negativos = 0
cantidad_abstenciones = 0

votos_afirmativos = []
votos_negativos = []
votos_abstenciones = []

while True:
    nombre_senador = input('ingrese el nombre del senador: ')
    while not nombre_senador.isalpha():
        nombre_senador = input('Error. ingrese el nombre del senador: ')

    presencia_senador = input('esta presente?: ')
    while presencia_senador != 'si' and presencia_senador != 'no':
        presencia_senador = input('Error. Diga si esta presente o no: ')

    if presencia_senador == 'si':
        senadores_presentes +=1
        voto_senador = input('indique el voto del senador: afirmativo, negativo o abstencion: ')
        while voto_senador.upper() not in ['AFIRMATIVO', 'NEGATIVO', 'ABSTENCION']: 
            voto_senador = input('Error. indique el voto del senador: afirmativo, negativo o abstencion: ')
    else:
        voto_senador = 'ABSTENCION'

    total_senadores += 1

    match voto_senador:
        case 'AFIRMATIVO':
            votos_afirmativos += 1
            votos_afirmativos.append(nombre_senador)
        case 'NEGATIVO':
            votos_negativos += 1
            votos_negativos.append(nombre_senador)
        case _:
            votos_abstenciones += 1
            votos_abstenciones.append(nombre_senador)

    continuar = input('desea continuar?: ')
    while continuar != 'no' and continuar != 'si':
        continuar = input('Error. Desea continuar?: ')
    
    if continuar == 'no':
        break

votos_afirmativos = len(votos_afirmativos)
votos_abstenciones = len(votos_abstenciones)
votos_negativos = len(votos_negativos)

porcentaje_afirmativos = votos_afirmativos *100 / total_senadores
porcentaje_negativos = votos_negativos *100 / total_senadores
porcentaje_abstenciones = votos_abstenciones *100 / total_senadores

print(f"cantidad de senadores: {total_senadores}\n"
    f'cantidad de senadores presentes: {senadores_presentes}\n'
    f'cantidad de votos afirmativos: {votos_afirmativos}, porcentaje: {porcentaje_afirmativos}\n'
    f'cantidad de negativos {votos_negativos}, porcentaje: {porcentaje_negativos}\n'
    f'cantidad de abstenciones {votos_abstenciones}, porcentaje: {porcentaje_abstenciones}\n')

