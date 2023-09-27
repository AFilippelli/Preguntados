'''
Ejercicio Integrador 01
La división de higiene está trabajando en un control de stock para productos sanitarios.
Debemos realizar la carga de 5 (cinco) productos de prevención de contagio, de cada una debe
obtener los siguientes datos:
1. El tipo (validar "barbijo", "jabón" o "alcohol")
2. El precio: (validar entre 100 y 300)
3. La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las 1000
unidades)
4. La marca y el Fabricante.
Se debe informar lo siguiente:
A. Del más caro de los barbijos, la cantidad de unidades y el fabricante.
B. Del ítem con más unidades, el fabricante.
C. Cuántas unidades de jabones hay en total.
'''
acumulador_alcohol = 0
acumulador_jabon = 0
acumulador_barbijo = 0
contador_jabon = 0
flag_barbijo = True




for i in range(5):
    tipo = input("Ingrese tipo (barbijo/jabon/alcohol)")
    while tipo != "barbijo" and tipo != "jabon" and tipo != "alcohol":
        tipo = input("Error, ingrese tipo correctamente")
    precio = int(input("Ingrese precio (entre 100 y 300)"))
    while precio < 100 and precio > 300:
        precio = int(input("Error, ingrese precio correctamente"))
    cantidad_unidades = int(input("Ingrese cantidad de unidades (1-1000)"))
    while cantidad_unidades < 1 and cantidad_unidades > 1000:
        cantidad_unidades = int(input("Error, Ingrese cantidad valida"))
    marca = input("Ingrese marca")
    fabricante = input("Ingrese fabricante")

    match tipo:
        case "barbijo":
            acumulador_barbijo += cantidad_unidades
            fabricante_barbijo = fabricante
            if flag_barbijo == True or precio > precio_barbijo_caro:
                flag_barbijo = False
                precio_barbijo_caro = precio
                cantidad_barbijo_caro = cantidad_unidades
                fabricante_barbijo_caro = fabricante
        case "alcohol":
            acumulador_alcohol += cantidad_unidades
        case "jabon":
            acumulador_jabon += cantidad_unidades
            contador_jabon = contador_jabon + 1
            
    if acumulador_alcohol > acumulador_barbijo and acumulador_alcohol > acumulador_jabon:
        tipo_mas_unidades = "alcohol"
    elif acumulador_barbijo > acumulador_jabon and acumulador_barbijo >= acumulador_alcohol:
        tipo_mas_unidades = "barbijo"
    else:
        tipo_mas_unidades = "jabon"
    
print(f'''cantidad y fabricante del barbijo mas caro: {cantidad_barbijo_caro}, {fabricante_barbijo_caro}\n
    Fabricante del tipo con mas unidades: {tipo_mas_unidades}\n
    Unidades de jabon en total: {acumulador_jabon}''')














