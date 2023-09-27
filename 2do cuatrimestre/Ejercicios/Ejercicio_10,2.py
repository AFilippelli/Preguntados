'''
Ejercicio 10:
Pedir al usuario que ingrese los datos de 5 alumnos y guardarlos en sus
respectivas listas. Validar el ingreso de datos según su criterio.
Datos:
nombre, sexo (f/m), nota (validar).
Una vez cargados los datos:
Mostrar el nombre del hombre con nota más baja
Mostrar el promedio de notas de las mujeres
Ejemplo:
nombres = ["Juan","Pedro","Sol","Paco","Ana"]
sexo = ["m","m","f","m","f"]
nota = [6,8,10,8,5]
'''

bandera_menor_nota = True
valoracion_nueva = 0
contador = 0

for i in range(5):

    nombres = []
    sexos = []
    notas = []

    nombre = input('Ingrese su nombre: ')
    
    sexo = input('Ingresar su sexo: ')
    while len(sexo) > 1 and sexo != 'f' and sexo != 'm':
        sexo = input('Ingresar su sexo: ')
    
    nota = int(input('Ingresar su nota: '))
    while nota < 1 or nota > 10:
        nota = int(input('Ingresar su nota: '))
    
    nombres = [nombre]
    sexos = [sexo]
    notas = [nota]

    for i in range(len(notas)):

        nombre_nuevo = nombres[i]
        valoracion = notas[i]
        sexo_nuevo = sexos[i]
        
        if bandera_menor_nota == True or sexo_nuevo == 'm' and valoracion < menor:
            bandera_menor_nota = False
            menor = valoracion
            nombre_menor = nombre_nuevo
        
        if sexo_nuevo == 'f':
            valoracion_nueva += valoracion
            contador += 1 

promedio_mujeres = valoracion_nueva / contador

print(f'Hombre con menor nota: {nombre_menor}')
print(f'Promedio de nota de mujeres: {promedio_mujeres}')