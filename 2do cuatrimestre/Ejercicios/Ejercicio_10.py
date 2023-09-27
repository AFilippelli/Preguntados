'''
Ejercicio 10:
Pedir al usuario que ingrese los datos de 5 alumnos y guardarlos en sus
respectivas listas. Validar el ingreso de datos según su criterio.
Datos:
nombre, sexo (f/m), nota (validar).
Una vez cargados los datos:
Mostrar el nombre del hombre con nota más baja
Mostrar el promedio de notas de las mujeres
'''

lista_alumnos = []
bandera_hombre_menor_nota = 0
contador = 0
nota_promedio = 0


for i in range(4):
    dic_alumnos = {}
    nombre = input("Ingrese nombre: ")
    sexo = input("Ingrese sexo m/f: ")
    while sexo != "m" and sexo != "f":
        sexo = input("Error, ingrese genero m/f: ")
    nota = int(input("Ingrese nota: "))
    while nota < 1 or nota > 10:
        nota = int(input("Error, ingrese nota valida"))

    dic_alumnos["nombre"] = nombre
    dic_alumnos["sexo"] = sexo
    dic_alumnos["nota"] = nota
    lista_alumnos.append(dic_alumnos)

print(lista_alumnos)

for i in range(len(nota)):
    nombre = dic_alumnos["nombre"]
    nota = dic_alumnos["nota"]
    sexo = dic_alumnos["sexo"]

    if bandera_hombre_menor_nota == True or sexo == "m" and nota < menor:
        bandera = False
        menor = nota
        nombre_menor = nombre

        if sexo == "f":
            nota_promedio += nota
            contador += 1

    nota_final = nota_promedio / contador

print(f"hombre con menor nota: {nombre_menor}")
print(f"promedio de nota de mujeres:{nota_final}")




'''    nota = int(dic_alumnos["nota"])
    if alumno["sexo"] == sexo == "m":
        continue
    if flag_menor_nota == True or nota < menor_nota:
        menor_nota = nota
        hombre_menor_nota = dic_alumnos["nota"]
        flag_menor = False

print(f" {hombre menor nota} es quien tiene la nota mas baja")
'''
