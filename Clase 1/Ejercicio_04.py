'''
Adrian Filippelli - 1B - Ejercicio 4
La división de alimentos está trabajando en un pequeño software para cargar las
compras de ingredientes para la cocina de Industrias Wayne.
Realizar el algoritmo que permita ingresar los datos de una compra de ingredientes
para preparar comida al por mayor. En total, sabemos que se realizarán 15 compras
de ingredientes.
Se registra por cada compra:
1. PESO: (entre 10 y 1000 kilos)
2. PRECIO POR KILO: (mayor a 0 [cero]).
3. TIPO VARIEDAD: (vegetal, animal, mezcla).
Además tener en cuenta que si compro más de 1000 kilos en total tengo un 15% de
descuento sobre el precio bruto, o si compro más de 300 kilos en total, tengo un 25%
de descuento sobre el precio bruto.
Se desea saber:
A. El importe total a pagar, BRUTO sin descuento.
B. El importe total a pagar con descuento (Solo si corresponde).
C. Informar el tipo de alimento más caro.
D. El promedio de precio por kilo en total.
'''

precio_bruto = 0
acumulador_peso = 0
bandera_alimento = 0
acumulador_precio = 0

for i in range(15):

    peso = float(input('Ingrese un peso entre 10 y 1000 kg: '))
    while peso < 10 or peso > 1000:
        peso = float(input('Error!! Reingrese un peso entre 10 y 1000 kg: '))
    
    precio = float(input('Ingrese precio por kg: ')) 
    while precio < 1:
        precio = float(input('Error!! Reingrese precio por kg: '))

    variedad = input('Ingrese tipo de variedad: "vegetal", "animal" o "mezcla": ')
    while variedad != 'vegetal' and variedad != 'animal' and variedad != 'mezcla':
        variedad = input('Error! Reingrese tipo de variedad: "vegetal", "animal" o "mezcla": ')

    precio_bruto += precio * peso

    acumulador_precio += precio

    acumulador_peso += peso

    if bandera_alimento == 0:
        bandera_alimento = 1
        precio_caro = precio
        alimento_caro = variedad
    elif precio_caro < precio:
        precio_caro = precio
        alimento_caro = variedad

promedio_precio_kilo = acumulador_peso / acumulador_precio

if acumulador_peso > 300:
    precio_descuento = precio_bruto * 0.75
elif acumulador_peso > 100:
    precio_descuento = precio_bruto * 0.85
else:
    precio_descuento = precio_bruto

print(f'Precio bruto sin descuento: {precio_bruto}')
print(f'Precio bruto con descuento(si corresponde): {precio_descuento}')
print(f'Tipo de alimento mas caro: {alimento_caro}')
print(f'Promedio de precio por kilo: {promedio_precio_kilo}')