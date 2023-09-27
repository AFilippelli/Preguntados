#ayuda para integrador 01


#listar los superheroes agrupados por color de ojos

def listar_agrupados(lista:list, clave:str):
    lista_agrupados = []
    for heroe in lista:
        color = heroe[clave]
        lista_agrupados.append(color)

    lista_colores_filtrada = set(lista_agrupados)

    for color in lista_colores_filtrada:
        print (color)
        for heroe in lista:
            if heroe [clave] == color:
                print (f"\t{heroe['nombre']}")

#es una funcion generica porque le doy varios usos solo especificando en el parametro que clave es

#STRINGS

#STRING: TIPO DE DATO INMUTABLE
mi_cadena = "hola"
print(id(mi_cadena))

mi_cadena = "chau"
print(id(mi_cadena)) 

mi_cadena = "      hola mundo     "
mi_cadena = mi_cadena.strip()
#el metodo strip se encarga de quitar espacios a la izquierda o a la derecha de mi cadena
print(mi_cadena)

#otro metodo es el metodo upper q sirve para pasar todo a mayusculas
mi_cadena = mi_cadena.upper()
print(mi_cadena)
#si quiero en minusculas, utilizo lower de la misma forma
#si quiero pasar a mayuscula la primer letra de la palabra utilizo .capitalize()

#otro metodo es el replace(), lo que hace es reemplazar un pedacito de esa cadena por otra cadena, por ejemplo:
mi_cadena = mi_cadena.replace('mundo', 'zzz')
print (mi_cadena)

#otro metodo es split() sirve para cortar un pedacito de esa cadena
mi_cadena = "python, java, javaScript, c#"
lista_split = mi_cadena.split(",")# "," ->caracter delimitador (no puede ser un caracter que este usando como valor dentro de la cadena, por ejemplo #)
for lenguaje in lista_split:
    print (lenguaje.strip())#como muestra espaciado el resultado, usamos el strit

#el metodo join sirve para unir cadenas, por ejemplo
separador = "/"
dia = "10"
mes = "9"
año = "2005"
fecha = separador.join([dia, mes, año])

print (fecha) #muestra una cadena separada por /

#metodo: zfill sirve para rellenar con 0 hacia la izquierda
cadena = "123"
cadena = cadena.zfill(21) #18 0 hacia la izquierda porque ya hay 3 numeros
print (cadena)

#metodo isalpha, devuelve true si es alfabetica y true si no lo es 
mi_cadena = "hola mundo"
print(mi_cadena.isalpha()) #devuelve false porque el espacio no es un alpha, es un simbolo
#si quiero saber si es alpha numerico entonces uso isalnum()

#metodo len: sirve para decirme el largo de la cadena 
cadena = "hola mundo"
print (len(cadena))

#count: cuenta la cantidad de veces que aparece la subcadena que indico dentro de la cadena
mi_cadena = "holalala"
print(mi_cadena.count("la")) #se uede usar para numeros tambien

#SLICE, no es un metodo pero es una forma de recorrer una cadena 
cadena = "hola mundo"
print (cadena[5:10]) #printeo desde el caracter 5 al 10, osea el mundo, porque se comienza desde 0
#si yo no pongo nada y pongo [:5] va a tomar del 0 al 5
