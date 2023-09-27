from data_stark import lista_personajes

def stark_normalizar_datos(lista_recibida: list, claves: list):
    ''' 
    Normaliza los valores asociados a las claves especificadas en los diccionarios de la lista.
    Args:
    lista_recibida (list): Una lista de diccionarios que se desea normalizar.
    claves (list): Una lista de cadenas que representan las claves cuyos valores se deben normalizar.
    Returns:
    list: La lista de diccionarios con los valores normalizados (si es necesario).
    '''
    bandera_normalizados = False
    
    if len(lista_recibida) > 0:
        for heroe in lista_recibida:
            for clave in claves:
                if clave in heroe and type(heroe[clave]) != float:
                    heroe[clave] = float(heroe[clave])
                    bandera_normalizados = True
        
        if bandera_normalizados:
            print("Datos normalizados")
        else:
            print("Error, lista vacía")
    return lista_recibida




def obtener_dato(dic_heroe:dict, clave:str): #1.1
    '''
    Esta función realiza una comprobación para asegurarse de que el diccionario
    sea válido, es decir, que sea un diccionario y que contenga una clave llamada "nombre".
    En caso de que esto se cumpla retorna True, caso opuesto, devolvera False.
    Args:
    dic_heroe (dict): Un diccionario que representa la información de un héroe.
    clave (str): La clave que se desea comprobar si está presente en el diccionario del héroe.
    Returns:
    bool: True si la clave está presente en el diccionario del héroe y el diccionario es válido;
    de lo contrario, False.
    '''
    if isinstance(dic_heroe, dict) and dic_heroe.get("nombre") is not None:
        if clave in dic_heroe:
            return True
        else:
            return False
    else: 
        return False
    


def obtener_nombre(dic_heroe: dict): #1.2
    '''
    Esta función verifica si un diccionario de héroe contiene la clave "nombre" utilizando la función
    obtener_dato. Si la clave "nombre" está presente, devuelve el nombre del héroe. Si la clave no está presente, devuelve "Error".
    Args:
    dic_heroe (dict): Un diccionario que representa la información de un héroe.
    Returns:
    str: El nombre del héroe en un formato de cadena, o "Error" si
    la clave "nombre" no está presente en el diccionario del héroe.

    '''
    if obtener_dato(dic_heroe, "nombre"):
        nombre = dic_heroe["nombre"]
        return f"Nombre: {nombre}"
    else:
        return "Error"


def obtener_nombre_y_dato(dic_heroe: dict, clave:str): #2
    '''
    Esta función verifica si un diccionario de héroe contiene la clave "nombre" utilizando la función
    obtener_dato y si la clave especificada está presente en el diccionario. Si ambas condiciones se cumplen,
    devuelve una cadena que combina el nombre del héroe y el valor asociado a la clave especificada en un formato
    de cadena.
    Args:
    dic_heroe (dict): Un diccionario que representa la información de un héroe.
    clave (str): La clave cuyo valor se desea obtener y combinar con el nombre del héroe.
    Returns:
    str: Una cadena de texto que contiene el nombre del héroe y el valor de la clave especifica.
    Si el diccionario no contiene la clave "nombre" o la clave especificada,
    o si el diccionario no es válido, la función devuelve False.
    '''
    if dic_heroe == 0:
        return False
    if obtener_dato(dic_heroe, "nombre") and clave in dic_heroe:
        nombre = obtener_nombre(dic_heroe)
        key = dic_heroe[clave]
        return f"{nombre} | {clave}: {key}"
    else:
        return False


def obtener_maximo(lista_recibida:list, clave:str): #3.1
    '''
    Esta función toma una lista de diccionarios y una clave específica. La función verifica si la lista es válida 
    y si el valor asociado a la clave en el
    primer diccionario de la lista es de tipo entero o flotante. Luego, busca y devuelve el valor máximo de la clave
    especificada en la lista de diccionarios.
    Args:
    lista_recibida (list): Una lista de diccionarios que representan objetos (héroes).
    clave (str): La clave cuyo valor máximo se desea encontrar en la lista.
    Returns:
    float: El valor máximo de la clave especificada en la lista de diccionarios. 
    Si la lista es inválida o si los valores no son numéricos en el primer diccionario, la función devuelve False.
    '''
    if lista_recibida == 0:
        return False
    if not isinstance(lista_recibida[0][clave], (int, float)):
        return False
    if(type(lista_recibida) == type(list())):
        dic_max = lista_recibida[0]
        flag_mayor = True

        for heroe in lista_recibida:
            if flag_mayor == True or float(heroe[clave]) > float(dic_max[clave]):
                flag_mayor = False
                dic_max = heroe
                clave_max = heroe[clave]
        return clave_max


def obtener_minimo(lista_recibida:list, clave:str): #3.2
    '''
    Esta función toma una lista de diccionarios y una clave específica. La función verifica si la lista es válida y
    si el valor asociado a la clave en el primer diccionario de la lista es de tipo entero o flotante. Luego, busca
    y devuelve el valor mínimo de la clave especificada en la lista de diccionarios.
    Args:
    lista_recibida (list): Una lista de diccionarios que representan objetos (héroes).
    clave (str): La clave cuyo valor mínimo se desea encontrar en la lista.
    Returns:
    float: El valor mínimo de la clave especificada en la lista de diccionarios.
    Si la lista es inválida o si los valores no son numéricos en el primer diccionario, la función devuelve False.
    '''
    if lista_recibida == 0:
        return False
    if not isinstance(lista_recibida[0][clave], (int, float)):
        return False
    if(type(lista_recibida) == type(list())):
        dic_min = lista_recibida[0]
        flag_menor = True

        for heroe in lista_recibida:
            if flag_menor == True or float(heroe[clave]) < float(dic_min[clave]):
                flag_menor = False
                dic_min = heroe
                clave_min = heroe[clave]
        return clave_min


def obtener_dato_cantidad(lista:list, valor:int, clave:str, genero:str):
    '''
    Esta función toma una lista de diccionarios, un valor (1 para máximo, 2 para mínimo),
    una clave específica y un género específico. Dependiendo del valor proporcionado,
    la función utiliza las funciones obtener_maximo o obtener_minimo para encontrar
    el valor máximo o mínimo de la clave en la lista de un género especificado y luego
    crea una nueva lista de héroes que tienen ese valor en la clave especificada.
    Args:
    lista (list): Una lista de diccionarios que representan objetos (héroes).
    valor (int): Un valor entero que indica si se debe buscar el máximo (1) o mínimo (2).
    clave (str): La clave cuyo valor máximo o mínimo se desea encontrar en la lista.
    genero (str): El género específico que se desea buscar.
    Returns:
    list: Una lista de diccionarios que representan héroes con el valor máximo o mínimo
    de la clave especificada en el género especificado.
    Si el valor no es válido (ni 1 ni 2), la función devuelve una lista vacía.
    '''
    personajes_genero = [heroe for heroe in lista if heroe.get('genero') == genero]

    if valor == 1:
        mayor_dato = obtener_maximo(personajes_genero, clave)
        lista_max_min = []
        for heroe in personajes_genero:
            if heroe.get(clave) == mayor_dato:
                lista_max_min.append(heroe)
        return lista_max_min

    elif valor == 2:
        minimo_dato = obtener_minimo(personajes_genero, clave)
        lista_max_min = []
        for heroe in personajes_genero:
            if heroe.get(clave) == minimo_dato:
                lista_max_min.append(heroe)
        return lista_max_min


def stark_imprimir_heroes(lista:list): #3.4
    '''
    Esta función toma una lista de héroes y la imprime en la consola. Si la lista está vacía, la función no imprime nada.
    Args:
    lista (list): Una lista de diccionarios que representan objetos (héroes).

    '''
    if len(lista) == 0:
        return False
    print(lista)


#mas_fuerte = obtener_maximo(lista_personajes, "fuerza")
#lista_mas_pesados = obtener_dato_cantidad(lista_personajes, 1, "fuerza")


def sumar_dato_heroe(lista:list, clave:str): #4.1
    '''
    Esta función toma una lista de diccionarios que representan héroes y una clave específica. Luego, itera a través de
    los diccionarios en la lista y suma los valores asociados a esa clave.
    Args:
    lista (list): Una lista de diccionarios que representan objetos (héroes).
    clave (str): La clave cuyos valores se desean sumar en la lista.
    Returns:
    int: La suma de los valores de la clave especificada en la lista de diccionarios. Si la clave no es una cadena
    o no se encuentra en algún diccionario de la lista, la función devuelve 0.
    '''
    if type(clave) == type(str()):
        suma_dato = 0
        for heroe in lista:
            personaje = heroe[clave]
            if personaje == heroe[clave]:
                suma_dato += personaje
        return suma_dato


def dividir(dividendo:int,divisor:int): #4.2
    '''
    Esta función toma dos números enteros, y realiza una división entera entre ellos. Devuelve
    el resultado de la división como un número entero. Si el divisor es igual a cero, la función devuelve False.
    Args:
    dividendo (int): El número que se dividirá.
    divisor (int): El número por el cual se realizará la división.
    Returns:
    int: El resultado de la división entera de `dividendo` entre `divisor`. Si `divisor` es igual a cero, la función
    devuelve False.
    '''
    if divisor == 0:
        return False
    resultado = dividendo // divisor
    return resultado


def calcular_promedio(lista:list, clave:str): #4.3
    '''
    Esta función toma una lista de diccionarios que representan héroes y una clave específica. Luego, utiliza la función
    `sumar_dato_heroe` para obtener la suma de los valores de la clave en la lista y la longitud de la lista para
    calcular el promedio. El promedio se devuelve como un número flotante. Si la lista está vacía, la función devuelve 0.
    Args:
    lista (list): Una lista de diccionarios que representan objetos (héroes).
    clave (str): La clave cuyos valores se desean promediar en la lista.
    Returns:
    float: El promedio de los valores de la clave especificada en la lista de diccionarios. Si la lista está vacía,
    la función devuelve 0.
    '''
    suma_dato = sumar_dato_heroe(lista, clave)
    cantidad_heroes = len(lista)

    if cantidad_heroes > 0:
        promedio = dividir(suma_dato, cantidad_heroes)
        return promedio
    else:
        return 0


def mostrar_promedio_dato(lista:list, clave:str): #4.4
    '''
    Esta función toma una lista de diccionarios que representan héroes y una clave específica. Verifica si la lista
    no está vacía y si la clave es de tipo entero o flotante, lo que indicara si se puede calcular y mostrar el promedio
    de los valores de la clave.
    Args:
    lista (list): Una lista de diccionarios que representan objetos (héroes).
    clave (str): La clave cuyos valores se desean promediar en la lista.
    Returns:
    bool: True si la lista no está vacía y la clave es de tipo entero o flotante; False en otros casos.

    '''
    if len(lista) == 0:
        return False
    if type(clave) == type(int(), float()):
        return True


def imprimir_menu(): #5.1
    '''
    Esta función genera un menú de opciones como una cadena de texto.
    Returns:
    str: Una cadena de texto que representa el menú de opciones.
    '''
    menu = ('''         
            1. Normalizar Datos
            2. Imprimir cada superheroe de genero NB
            3. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
            4. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
            5. Recorrer la lista y determinar cuál es el superhéroe más débil de género M
            6. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
            7. Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB
            8. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
            9. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
            10. Listar todos los superhéroes agrupados por color de ojos.
            11. Listar todos los superhéroes agrupados por tipo de inteligencia
            12. Salir
            ''')
    return menu


def validar_entero(numero:str):
    '''
    Esta función toma una cadena de texto y verifica si esta cadena representa un número entero. Si es así,
    devuelve True; de lo contrario, devuelve False.
    Args:
    numero (str): La cadena de texto que se desea validar como número entero.
    Returns:
    bool: True si la cadena representa un número entero; False si no lo hace.
    '''
    if numero.isdigit():
        return True
    else:
        return False


def stark_menu_principal():
    print(imprimir_menu())
    opcion = input("ingrese una opcion: ")
    if validar_entero(opcion):
        return opcion
    else:
        return False


def stark_marvel_app (lista_personajes: list):
    '''
    esta funcion muestra el resultado de la opcion que el usuario elija
    Args:
    lista_personajes(list): Una lista de diccionarios que representan objetos (héroes)
    '''
    flag_normalizada = False
    opcion = -1
    while opcion != 11: 
        opcion = stark_menu_principal()
        if opcion == '1':
            flag_normalizada = True
            lista_claves = ["altura", "fuerza", "peso"]
            stark_normalizar_datos(lista_personajes, lista_claves)
        elif flag_normalizada:
            if opcion == "2":
                print("Nombres de superhéroes de género NB:")
                for heroe in lista_personajes:
                    if heroe.get('genero') == 'NB':
                        print(obtener_nombre(heroe))
            elif opcion == '3':
                heroes_mas_altos_femeninos = obtener_dato_cantidad(lista_personajes, 1, 'altura', 'F')
                if heroes_mas_altos_femeninos:
                    print("Superhéroes más altos del género femenino:")
                    for heroe in heroes_mas_altos_femeninos:
                        print(obtener_nombre(heroe))
            elif opcion == '4':
                heroes_mas_altos_masculinos = obtener_dato_cantidad(lista_personajes, 1, 'altura', 'M')
                if heroes_mas_altos_masculinos:
                    print("Superhéroes más altos del género masculino:")
                    for heroe in heroes_mas_altos_masculinos:
                        print(obtener_nombre(heroe))
            elif opcion == '5':
                heroes_mas_debil_masculino = obtener_dato_cantidad(lista_personajes, 2, 'fuerza', 'M')
                if heroes_mas_debil_masculino:
                    print("Superhéroes más debil del género masculino:")
                    for heroe in heroes_mas_debil_masculino:
                        print(obtener_nombre(heroe))
            elif opcion == '6':
                heroes_mas_debil_NB = obtener_dato_cantidad(lista_personajes, 2, 'fuerza', 'NB')
                if heroes_mas_debil_NB:
                    print("Superhéroes más debil del género no binario:")
                    for heroe in heroes_mas_debil_NB:
                        print(obtener_nombre(heroe))
            elif opcion == '7':
                genero_nb = 'NB'
                clave_fuerza = 'fuerza'
                heroes_nb = [heroe for heroe in lista_personajes if heroe['genero'] == genero_nb]
                fuerza_promedio_nb = calcular_promedio(heroes_nb, clave_fuerza)
                if fuerza_promedio_nb:
                    print(f"Fuerza promedio de superhéroes de género NB: {fuerza_promedio_nb}")
                else:
                    print("No se encontraron superhéroes de género NB para calcular la fuerza promedio.")
            elif opcion == '8':
                pass
            elif opcion == '9':
                pass
            elif opcion == '10':
                pass
            elif opcion == '11':
                pass
            elif opcion == '12':
                print ('fin')
                break
            else:
                print("opcion incorrecta, intente nuevamente")
        else:
            print("Error, ingrese 1 para normalizar los datos antes de continuar")



programa = (stark_marvel_app(lista_personajes))
print(programa)



