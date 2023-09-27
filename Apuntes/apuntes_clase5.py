def sumar_numeros(primer_numero:int, segundo_numero:int)->int: #->None significa que esta funcion no retorna nada
    suma = primer_numero + segundo_numero

    return suma

def restar_numeros(primer_numero:int, segundo_numero:int)->int: #-> int significa que con el return devuelve un valor entero
    resta = primer_numero - segundo_numero

    return resta    #esta funcion nos va a dar un resultado que podemos mostrar o 
                    #utilizarlo para agregarlo en otra parte del código

def multiplicar_numeros(primer_numero:int, segundo_numero:int):
    multiplicacion = primer_numero * segundo_numero
    
    return multiplicacion

def dividir_numeros(primer_numero:int, segundo_numero:int):
    division = None #si la division tiene como divisor 0, el valor que devolverá sera None
    if segundo_numero != 0:
        division = primer_numero / segundo_numero

    return division    

flag_ingreso = False #creamos una bandera que será True cuando la primera opcion
                    #que se pida sea la de ingresar numeros, porque si ingresamos
                    #a una opcion sin dos numeros que calcular, dará error
while True:
    opcion = int(input("1. Ingresar numeros\n2. Sumar\n3. Restar\n4. Multiplicar\n5. Dividir\n6. Salir\nIngrese opcion: "))
    match opcion:
        case 1:
            x = int(input("Ingrese un numero: "))
            y = int(input("Ingrese un numero: "))
            flag_ingreso = True #La bandera será verdadera al elegir la 1ra opcion
        case 2:
            if flag_ingreso == True:
                resultado = sumar_numeros(x,y)
                print(f"El resultado de la suma es: {resultado}")
            else:
                print("Error: no hay numeros ingresados")
        case 3:
            if flag_ingreso == True:
                resultado = restar_numeros(x,y)
                print(f"El resultado de la resta es: {resultado}")
            else:
                print("Error: no hay numeros ingresados")
        case 4:
            if flag_ingreso == True:
                resultado = multiplicar_numeros(x,y)
                print(f"El resultado de la multiplicacion es: {resultado}")
            else:
                print("Error: no hay numeros ingresados")    
        case 5:
            if flag_ingreso == True:
                resultado = dividir_numeros(x,y)    
                if(resultado != None):
                    print(f"El resultado de la division es: {resultado}")
                else:
                    print("Error, no se puede dividir por 0")
            else:
                print("Error: no hay numeros ingresados")            
        case 6:
            break                
            

