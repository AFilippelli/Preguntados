'''
Ejercicio 9:
Dadas las siguientes listas:
edades = [25,36,18,23,45]
nombre = ["Juan","Ana","Sol","Mario","Sonia"]
y considerando que la posición en la lista corresponde a la misma persona,
mostar el nombre de la persona más joven
'''

nombres = ["Juan","Ana","Sol","Mario","Sonia"]
edades = [25,36,18,23,45]

for i in range(0,len(nombres),1):
    nombre = nombres[i]
    edad = edades[i]
    if i == 0 or menor_edad > edad:
        nombre_mas_joven = nombre
        menor_edad = edad

print(nombre_mas_joven)