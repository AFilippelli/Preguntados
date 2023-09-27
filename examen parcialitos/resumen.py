'''


/////////////////REGLAS DE ESTILO/////////////////////////
Python es un lenguaje orientado a objetos
Tiene determinadas reglas de estilo que son muy importantes para la legibilida
del codigo.
PEP, "Python Enhancement Proposal, es un documento que proporciona informacion
a la comunidd de python o describe una nueva caracteristica.

PEP8 es un conjunto de recomendaciones cuyo objetivo es ayudar a escribir codigo 
mas legible y abarca desde como nombrar variables al numero maximo de caracteres que
una linea debe tener.

IDENTADO. Python no usa {} para designar bloques de codigo como otros lenguajes de
programacion, sino que usa bloques identados para indicar que un determinado bloque
de codigo pertenece a por ejemplo un if
EJ:(condicion_a and condicion_b):
    print("Hola Mundo")

    def mi_funcion(primer_parametro, segundo_parametro, tercer_parametro)
        print("Hola mundo")

(se recomienda limitar el tamaño de cada linea a 79 caracteres)  

Lineas en blanco: el uso de espacios en blanco mejora la legibilidad del codigo, y es
por esto que PEP8 indica donde debemos usar espacios y donde no.
EJ.
x = 5 correcto    x=5 incorrecto

SNAKE_CASE:
Para nombrar funciones, variables, metodos y Modulos se utiliza snake_case
EJ. def buscar_info()
    mi_variable
    mi_metodo
    mi_modulo

ENCODING:
los archivos se codifican por defecto en ASCII para python 2 y en UTF-8 para 
Python 3

VARIABLES. En python las variables son "etiquetas" que permiten hacer referencia a
los datos que se guardan en "cajas" llamadas objetos.
Para cada dato que aparece en un programa python crea un objeto que lo contiene.
Cada objeto tiene: 
-un identificador unico
-un tipo de dato
-un valor

Para asignar un valor a una variable se utiliza el operador de igualdad =.
////////////////////////////////////////////////////////////////////////////////////

//////////////////TIPOS DE DATOS////////////////////////
Entero: int
Permite representar numeros enteros
EJ: numero = 23
    print(numero)       #23
    print(type(numero)) #<class 'int'>

Flotante:float
Permite representar un numero positivo o negativo con decimales
EJ: numero = 3.14
    print(numero)       #3.14
    print(type(numero)) #<class 'float'>

Booleano: True, False
Es un tipo de dato que permite almacenar valores True o False

Cadena de caracteres: str
los strings son un tipo de dato que permite almacenar secuencias de caracteres
entre comillas.

Casting.
Hacer un casting significa convertir un tipo de dato a otro. en python es posible
convertir a string con str(), a entero con int() y a flotante con float()
///////////////////////////////////////////////////////////////////////

///////////////////////Colecciones/////////////////////////////////////////
Listas: list
Son uno de los tipos mas versatiles de lenguaje, ya que permiten almacenar un
conjunto arbitrario de datos.
EJ. lista = [1, "Hola", 3.67]
    print(type(lista))   # <class 'list'>
    print(lista[1])      # Hola

Tuplas: tuple
Las tuplas son muy similares a las listas, pero son inmutables, lo que significa que no
pueden ser modificadas una vez declaradas   

Diccionarios: dict
Un diccionario es una colección de elementos, donde cada uno tiene una clave (key)
y un valor (value)
diccionario = {'nombre' : 'Juan', 'edad' : 21}
print(diccionario['nombre'])  # Juan
print(diccionario['edad'])    # 21

Conjuntos: set
El set nos muestra la cadena que nosotros queramos sin elementos duplicados.
Un set se puede crear haciendo uso de { } 
s = {2, 4, 7, 1, 8, 1}
print(s)     # {1, 2, 4, 7, 8}
Un set también se puede crear haciendo uso de la palabra reservada set la cual 
permite transformar cualquier objeto iterable en un set.
lista = [1, 3, 6, 3, 2, 1]
s = set(lista)
print(s)       # {1, 2, 3, 6}
///////////////////////////////////////////////////////////////////////////////

//////////////FUNCIONES////////////////////////////////////////////
Una funcion es un bloque de codigo que realiza una tarea especifica.
Las funciones sirven para descomponer una tarea específica en un bloque de código
que se puede llamar varias veces desde cualquier parte del programa.
Para declarar una función en Python, utilizamos la palabra reservada "def" seguida
del nombre de la función y los parámetros entre paréntesis

Los parámetros son una característica clave de las funciones: son variables que se pasan
a la función cuando se llama. Por lo tanto, los parámetros son la forma en que se 
proporcionan datos de entrada a una función.

/////////////////////////////////////////////////////////////////////////////

////////////////////////STRINGS///////////////////////////////////////
Metodos de string.
Un método es una función especial, que existe
para un tipo de dato en particular.

Para trabajar con cadenas de texto en Python, se
emplean una serie de métodos a las variables del
tipo str.

Metodo: Strip.
El método strip eliminará todos los caracteres
vacíos que pueda contener la variable
EJ. cadena = " Hola Mundo "
    cadena = cadena.strip()
    print(cadena) # Hola Mundo

Metodo: Lower.
El método lower convertirá a las letras en
minúsculas.
EJ. cadena = "Hola Mundo"
    cadena = cadena.lower()
    print(cadena) # hola mundo 

Metodo: upper
El método upper convertirá a las letras en
mayúsculas.
EJ. cadena = "Hola Mundo"
    cadena = cadena.upper()
    print(cadena) # HOLA MUNDO

Metodo: capitalize
El método upper convertirá a las letras en
mayúsculas.
EJ. Método: capitalize
    cadena = "Hola Mundo"
    cadena = cadena.capitalize()
    print(cadena) #Hola Mundo 

Metodo: replace
El metodo replace remplazara un conjunto de  caracteres por otro
EJ. cadena = "Hola Mundo"
    cadena = cadena.replace("la","@")
    print(cadena) # Ho@ Mundo  

Metodo: split.
El metodo split divide una cadena en subcadenas y las devuelve almacenadas en una lista.
Ej. cadena = "Python,Java,C"
    print(cadena.split(","))    #['Python', 'Java', 'C'] 

Metodo: join
El metodo join devuelve la primera cadena unida a cada uno de los elementos de la lista
que se le pasa como parámetro.
Ej. cadena = +
    cadena = cadena.join(["A","B","C"])
    print(cadena) #A+B+C

Metodo: zfill
El metodo zfill rellena la cadena con ceros a la izquierda hasta llegar a la longitud
pasada como parametro.
Ej. cadena = "314"
    print(cadena.zfill(6)) #000314

Metodo: isalpha
El metodo isalpha devuelve True si todos los caracteres son alfabeticos, False de lo
contrario.
Ej. cadena = "Hola Mundo"
    print(cadena.isalpha()) #False -> por el espacio

    cadena = "HolaMundo"
    print(cadena.isalpha()) #True

Metodo: isalnum
El metodo isalnum devuelve True si todos los caracteres son alfanumericos, False
de lo contrario.
Ej. cadena = "Hola Mundo 123"
    print(cadena.isalnum()) #False -> por el espacio

    cadena = "HolaMundo123"
    print(cadena.isalnum())
    #True

Metodo: count
El metodo count permite contar las veces que otra cadena se encuentra dentro de la primera
Ej. cadena = "Hola Mundo Hola"
    print(cadena.count("la))  #2

Metodo: format
En este metodo las llaves son reemplazadas con valores de las variables pasadas
Ej. nombre_usuario = "JUAN"
    edad_usuario = 35
    cadena = "Nombre: {1}, Edad: {0}"
    print(cadena.format(edad_usuario,nombre_usuario))  #Nombre: JUAN, Edad: 35

F-strings
Ej. nombre_usuario = "JUAN"
    edad_usuario = 35
    cadena = f"Nombre: {nombre_usuario}, Edad: {edad_usuario}"
    print(cadena) #Nombre: JUAN, Edad: 35

Longitud: len
El metodo len indica la longitud de la cadena de texto dentro de la variable
en ese momento
Ej. cadena = "Hola Mundo"
    print(len(cadena)) #10

Slice    
Cuando se crea una slice (rebanada), el primer numero es donde comienza (inclusivo), y
el segundo numero de indice es donde termina (exclusivo)
Ej. cadena = "Hola Mundo"
    print(cadena[5:10]) #Mundo
    print(cadena[5:])  #Mundo
    print(cadena[:5])  #Hola
//////////////////////////////////////////////////////////////////////////////////////

/////////////////////////EXPRESIONES REGULARES////////////////////////////////.
Las expresionhes regulares RegEx, son una serie de simbolos que nos permitiran definir
patrones de busqueda en cadenas de texto.
Modulo re
El modulo re cuenta con un conjunto de metodos que permiten comprobar si una determinada
cadena coincide con una expresion regular dada.

split()
retorna una lista que contiene la cadena dividida por el numero de ocurrencias del patron.
import re
texto = 'uno 1 dos 2 tres 3 cuatro'
print(re.split('', texto))  #['uno', '1', 'dos', '2', 'tres', '3', 'cuatro']
print(re.split('[0-9]+', texto))  #['uno ', ' dos ', ' tres ', ' cuatro']
print(re.split('[a-z]+', texto)) #['', '1', '2', '3', '']

findall()
Retorna una lista que contiene todas las coincidencias del pattern (<<patron>>)
import re
texto = 'uno 1 dos 2 tres 3 cuatro'
print(re.findall(' ', texto))  #[' ', ' ', ' ', ' ', ' ', ' ', ' ']
print(re.findall('[0-9]+', texto))  #['1', '2', '3']
print(re.findall('[a-z ]+', texto))  #[' uno ', ' dos ', ' tres ', ' cuatro']
//////////////////////////////////////////////////////////////////////////////////

///////////////////////////////ARCHIVOS///////////////////////////////////////
Los archivos de texto contienen caracteres legibles, es posible no solo leer dicho
contenido sino tambien modificarlo usando un editor de texto.

Los archivos binarios son archivos que no se pueden interpretar en forma de texto: una
imagen, un sonido o incluso un archivo comprimido
r    Abre un archivo de texto sólo para lectura

rb   Abre un archivo binario sólo para lectura

r+   Abre un archivo de texto para escritura y lectura

w    Abre un archivo de texto sólo para escritura (si existe lo sobreescribe)

wb   Abre un archivo sólo para escritura (si existe lo sobreescribe)

w+   Abre un archivo de texto para escritura y lectura (si existe lo sobreescribe)

a    Abre un archivo para anexar información

Abrir un archivo: open
Para abrir un archivo se utiliza la funcion open
    archivo = open(nombre_archivo, modo)
archivo objeto file, el cual será utilizado para llamar a otros
métodos asociados con el archivo.

nombre_archivo string que contiene el nombre del archivo
al que queremos acceder.

modo string que contiene el modo de apertura del archivo.

Cerrar un archivo: close
Para cerrar un archivo se utiliza la funcion close
    archivo.close()
archivo objeto file que fue obtenido con el metodo open

El objeto: file
Una vez que un archivo esta abierto y se obtiene el objeto file, permite no solo
operar con el sino tambien obtener mucha informacion relacionada con ese archivo.

Leer un archivo: read
El metodo read permite extraer un string que contenga todos los caracteres del archivo
# Abrimos el archivo en modo lectura y escritura
archivo = open('archivo.txt', 'r+') 
texto = archivo.read()
print('El contenido del archivo es: ' + texto)
# Cerramos el archivo
archivo.close()

Leer un archivo: readlines
Permite obtener una lista con todas las lineas que contiene el archivo
archivo = open('archivo.txt', 'r+')
lista_lineas = archivo.readlines()
for linea in lista_lineas:
    print(linea, end="")
# Cerramos el archivo
archivo.close()

leer un archivo: file
Si solamente requerimos recorrer el archivo linea por linea, el objeto file
es iterable.
archivo = open('archivo.txt', 'r+')
for linea in archivo:
print(linea, end="")
# Cerramos el archivo
archivo.close()

Administrador de contexto: with
Podemos usar la sentencia with para abrir archivos en Python y dejar que el interprete
se encargue de cerrar el mismo
with open('archivo.txt', 'r+') as archivo:
for linea in archivo:
print(linea, end="")

CSV.
El CSV es un tipo de documento que representa los datos de forma parecida a una tabla, es
decir. organizando la informacion en filas y columnas.
Las columnas son separadas, por un signo de puntuacion (, ; .)u otro caracter y las
diferentes filas suelen separarse por un salto de linea.

JSON.
El nombre es un acronimo de las siglas en ingles de JavaScript Object Notation
JSON es un formato para el intercambio de datos basado en texto. Por lo que es
facil de leer tanto para una persona como para una maquina.

JSON (Escritura)
El paquete json permite traducir un diccionario a
formato JSON utilizando el método dump.

import json

data = {}
data['clientes'] = []
data['clientes'].append({ 'nombre': 'Juan', 'edad': 27})
data['clientes'].append({ 'nombre': 'Ana', 'edad': 26})

with open('data.json', 'w') as file:
    json.dump(data, file, indent=4, ensure_ascii=False )

La lectura es similar al proceso de escritura, se debe abrir un archivo y procesar
esté utilizando el metodo load 
import json
with open('data.json') as file:
data = json.load(file)
///////////////////////////////////////////////////////////////////////////////////////


///////////////////////////OPERADORES ARITMETICOS//////////////////////
+ suma
- resta
* multiplica
/ divide
% devuelve el resto de una division, ej 16/3 = 1
// divide con resultado solo de la parte entera
** potencia
////////////////////////////////////////////////////////////////////////

//////////////////////////ESTRUCTURAS DE CONTROL.///////////////////////
En muchas ocasiones se necesita que se cumpla determinada
condicion para que el programa pueda seguir ejecutandose.

Condicional: if, elif y else:
Estos permiten cambiar el flujo de ejecucion de un programa, haciendo que ciertos
bloqurs de codigo se ejecuten si y solo si se dan determinadas condiciones

Bucle: while.
El uso del while permite ejecutar una seccion de codigo mientras una condicion determinada
se cumpla.
Cuando se deje de cumplir, se saldrá del bucle y se continuará la ejecucion normal

Funcion: range.
El range() genera una secuencia de numeros que van desde cero hasta el numero que se 
pasa como parámetro.
Ej. lista_numeros = list(range(5))
    print(lista_numeros)  #[0,1,2,3,4]

Bucle: for.
En este tipo de bucle el numero de iteraciones está definido de antemano, mientras que
en un while no
En python el for permite recorrer los elementos de un objeto iterable.

Bucle: break.
La sentencia brek nos permite alterar el comportamiento de los bucles while y for.
Permite terminar con la ejecucion del bucle.

Bucle: continue.
La sentenci continue se salta todo el codigo restante en la itercion actual y vuelve
al principio en el caso de que aun queden iteraciones por completar
EJ. lista_numeros=[1,2,4,5,77,-1]
    for numero in lista_numeros:
        if(numero==5):
            continue
        print(numero,end=" ")  #Salida 1 2 4 77 -1

Seleccion: match
La sentencia match permite organizar bloques de codigo, de forma que se ejecuten
cuando se cumple cierta condicion o caso


REGLAS DE ESTILO Y STRINGS
tanto las reglas de estilo como los strings valoran la claridad en la escritura. En el
caso de las reglas de estilo, esto se logra mediante la elección adecuada de nombres y
el uso de comentarios informativos. En el manejo de strings, se busca utilizar métodos
y funciones que hagan que las operaciones sean más comprensibles y menos propensas a errores.

En resumen, tanto las reglas de estilo en Python como el manejo de strings comparten el
objetivo de hacer que el código sea legible y coherente. La consistencia en la forma en
que se escriben las instrucciones y se manipulan los strings ayuda a mejorar la calidad
del código y a facilitar su mantenimiento y comprensión a lo largo del tiempo.

FUNCIONES Y COLECCIONES
Cuando se combinan funciones y colecciones, se pueden lograr tareas complejas y eficientes.
Por ejemplo, una función puede recibir una lista como argumento, procesarla de cierta manera
y devolver un resultado específico. Esto permite encapsular la lógica de procesamiento en
la función y reutilizarla con diferentes listas.
las funciones y las colecciones en Python trabajan juntas para simplificar y optimizar el
desarrollo de programas. Las funciones permiten crear un bloque de codigo que realize una
tarea especifica, mientras que las colecciones proporcionan una forma conveniente de almacenar
y organizar datos. Al combinar ambas, se pueden realizar tareas complejas de manera más eficiente
y modular.

COLECCIONES Y REGLAS DE ESTILO
En cuanto a las reglas de estilo, estas establecen pautas para escribir código Python de manera
consistente y fácilmente comprensible. Por ejemplo, se recomienda utilizar nombres de variables
descriptivos y seguir una convención de nombramiento consistente. Esto es especialmente relevante
al trabajar con colecciones, ya que las variables que almacenan colecciones pueden tener un
impacto significativo en la claridad y comprensión del código.
las reglas de estilo en Python y el manejo de colecciones están relacionados porque ambos se
centran en la legibilidad y la estructura del código. Seguir las reglas de estilo en la declaración
de variables y el uso de espacios en blanco, junto con comentarios descriptivos, ayuda a mejorar la
comprensión del código que trabaja con colecciones. Esto facilita la colaboración, el mantenimiento
y la resolución de problemas en el desarrollo de proyectos que involucran colecciones en Python.

REGLAS DE ESTILO Y VALIDACION
Al relacionar las reglas de estilo y la validación de tipo de datos, se puede destacar que las
reglas de estilo sugieren el uso de comentarios descriptivos para documentar y explicar el código.
Esto puede ser especialmente útil al realizar validación de tipo, ya que los comentarios pueden
indicar claramente las expectativas sobre los tipos de datos en un contexto determinado.



REGLAS DE ESTILO, COLECCIONES, FUNCIONES

















'''