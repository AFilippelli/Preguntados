def sumar_numeros (primer_numero:int, segundo_numero:int) ->int: #Implementacion de la funcion
    suma = primer_numero + segundo_numero

    return suma


def restar_numeros (primer_numero:int, segundo_numero:int) ->float: #Implementacion de la funcion
    resta = primer_numero - segundo_numero

    return resta

def multiplicar_numeros(primer_numero:int, segundo_numero:int) ->None:
    multiplicacion = primer_numero * segundo_numero
    
    return multiplicacion

def dividir_numeros(primer_numero:int, segundo_numero:int) -> float:
    division = None
    if segundo_numero != 0: #si el segundo numero es 0, la división no se ejecuta
        division = primer_numero / segundo_numero

    return division
bandera_ingreso = False
while True:
    opcion = int(input("1.Ingresar numeros\n2. Restar\n3. Multiplicar\n4. Dividir \n5. Sumar\n6. Salir\nIngrese una opcion: "))
    match opcion:
        case 1:
            x = int(input("Ingrese un numero: "))
            y = int(input("Ingrese un numero: "))
            bandera_ingreso = True
        case 2:
            if bandera_ingreso == True:
                resultado = restar_numeros(x, y)
                print(f"El resultado de la resta es: {resultado}")
            else:
                print("No ingresó numeros, vaya a la opcion 1 e ingrese operandos.")
        case 3:
            resultado = multiplicar_numeros(x, y)
            print(f"El resultado de la multiplicacion es: {resultado}")
        case 4:
            resultado = dividir_numeros(x, y)
            if(resultado != None):
                print(f"El resultado de la division es es: {resultado}")
            else:
                print("Error, no se puede dividir por cero")
        case 5:
            resultado = sumar_numeros(x, y)
            print(f"El resultado de la suma es: {resultado}")
        case 6:
            break




