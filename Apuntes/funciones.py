#clase del 20/04
#funciones

#como lo veniamos viendo sin recibir ni devolver
def sumar_numeros(): #siempre primero un verbo y despues un sustantivo. #Implementacion a la funcion 
    primer_numero = int(input('ingrese el primer numero: '))
    segundo_numero = int(input('ingrese el segundo numero: '))

    suma = primer_numero + segundo_numero

    print(f'La suma es: {suma}')

#no recibe, devuelve
def restar_numeros()-> int:#es lo que me devuelve(en este caso un entero) #implementacion de la funcion
    primer_numero = int(input('ingrese el primer numero: '))
    segundo_numero = int(input('ingrese el segundo numero: '))

    resta = primer_numero - segundo_numero

    return resta #llamo a la funcion aca con el retorno, no necesariamente tiene que mostrar el resultado cuando devuelva, podemos tomar ese algo y hacer lo que queramos

#con parametros formales sin return, no devolvia y recibia
def multiplicar_numeros (primer_numero:int, segundo_numero:int) -> None: #formales pq no van a cambiar, siempre van a ser primer num y segundo num
    multiplicacion = primer_numero * segundo_numero
    (f'el resultado de la  multiplicacion es: {multiplicacion}')

#FUNCION CON PARAMETROS QUE RETORNA
def dividir_numeros (primer_numero:int, segundo_numero:int)-> float:
    division = None #iniicializamos la variable en NONE no en 0 para que devuelva algo si no se cumple la condicion
    if segundo_numero != 0: #condicion por si es 0 el numero
        division = primer_numero / segundo_numero
    return division

print('hola. bienvenidos a mi programa')
sumar_numeros() #llamada a la funcion
print('gracias por sumar...')

resultado_resta = restar_numeros() #como la funcion va a retornar algo, tengo que tener una variable que haga ese retorno
print(f'El resultado de la resta es: {resultado_resta}')

multiplicar_numeros (5, 9) #como yo puse los parametros, tengo que pasar dos numeros que quiera multiplicar, el tema es que como 
#los pedi en los parametros formales, estos que son actuales deben decir el primer numero y el segundo. #es mas facil de esta forma 
#pq en vez de pedir los numeros ya se los digo yo
#ESTOS (5,9) SE LLAMAN ACTUALES pq yo puedo llamar a la funcion y hacer cambios en esos numeros

#EJEMPLO: PIDO NUM AL USUARIO
x = int(input('ingrese un numero: '))
y = int(input('ingrese otro numero: '))
#LLAMO A LA FUNCION Y MUESTRO ESE RESULTADO
multiplicar_numeros(x,y)

resultado_division = dividir_numeros(6,2)
print(f'El resultado de la division es: {resultado_division}')

resultado_division = dividir_numeros(x,y)
if (resultado_division != None):
    print(f'El resultado de la division es: {resultado_division}')
else:
    print('No se puede dividir por 0')


#ASI QUEDARIA BIEN
def sumar_numeros(primer_numero:int, segundo_numero:int)->int:
    suma = primer_numero + segundo_numero
    return suma

def restar_numeros(primer_numero:int, segundo_numero:int)->int:
    resta = primer_numero - segundo_numero
    return resta

def multiplicar_numeros(primer_numero:int, segundo_numero:int)->int:
    multiplicacion = primer_numero * segundo_numero
    return multiplicacion

def dividir_numeros (primer_numero:int, segundo_numero:int)-> float:
    division = None #iniicializamos la variable en NONE no en 0 para que devuelva algo si no se cumple la condicion
    if segundo_numero != 0: #condicion por si es 0 el numero
        division = primer_numero / segundo_numero
    return division


bandera_ingreso = 0 #genero bandera para q me iga si no puse numeros para hacer la operacion

while True:
    opcion = int(input('1. Ingresar numeros\n2. RestAR\n3. multiplicar \n4. dividir \n5. sumar \n6. salir\n Ingrese una opcion: '))
    match opcion:
        case 1:
            x = int(input('ingrese un numero: '))
            y = int(input('ingrese otro numero: '))
            bandera_ingreso = 1#cambio valor si es q entro al match
        case 2:
            if (bandera_ingreso == 1):
                resultado_resta = restar_numeros(x,y)
                print(f'El resultado de la resta es: {resultado_resta}')
            else:
                print('No hay numeros ingresados')
        case 3:
            resultado_multiplicacion = multiplicar_numeros(x,y)
            print(f'El resultado de la multiplicacion es: {resultado_multiplicacion}')
        case 4:
            resultado_division = dividir_numeros(x,y)
            if (resultado_division!= None):
                print(f'El resultado de la division es: {resultado_division}')
            else: 
                print('No se puede dividir por 0')
        case 5: 
            resultado_suma = sumar_numeros(x,y)
            print(f'El resultado de la suma es: {resultado_suma}')
        case _:
            break    