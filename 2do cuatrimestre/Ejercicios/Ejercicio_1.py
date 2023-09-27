'''Ejercicio 1:
Pedir el nombre y el sueldo, incrementarle un 10% e informar el aumento de su
sueldo para esa persona.
'''

nombre = input("ingrese su nombre: ")


sueldo = float(input("ingrese su sueldo: "))
while sueldo <= 0:
    sueldo = float(input("ingrese su sueldo: "))

sueldo+= sueldo * 0.10

print (f"su nombre es: {nombre}")
print(f"su sueldo con aumento de 10% es: {sueldo}")


