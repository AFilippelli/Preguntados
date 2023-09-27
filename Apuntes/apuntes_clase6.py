def potenciar(base, exponente):
    return base**exponente


b = 2
e = 3
#en vez de llamar a la funcion y pasarle en orden los parametros, podemos
#forzar que, en este caso, el parametro exponente tome el valor e
resultado = potenciar(exponente=e, base=b)

print(resultado)