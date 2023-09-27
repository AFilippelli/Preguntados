def mostrar_menu():
    print("1-Tema mas visto\n2-Tema menos visto\n3-Tema mas largo\n4-Salir\n")
    opcion = input("Opcion: ")
    return opcion

def mostrar_tema(tema: dict):
    print("Tema - titulo: {0} vistas {1}".format(tema["title"], tema["views"]))


def tema_maximo_minimo(lista_recibida: list, clave: str, tipo:str)->dict:
    #funcion tema_maximo_minimo: busca el valor maximo o minimo de una key y lo retorna
    if(type(lista_recibida) == type(list()) and type(clave) == type(str())):#validamos que lo que se pasa por 
        dic_min_max = lista_recibida[0]                                     #parametro sea del tipo pedido
        for lista in lista_recibida:
            if (tipo == "maximo") and (lista[clave] > dic_min_max[clave]):
                    dic_min_max = lista
            if(tipo == "minimo") and (lista[clave] < dic_min_max[clave]):
                    dic_min_max = lista
    else:
        dic_min_max = -1 #si no se pasa por parametro lo solicitado, devolvera error
    return dic_min_max


def tema_menos_visto(lista_externa: list)->dict:
    dic_minimo = lista_externa[0]
    for lista in lista_externa:
        if(lista["views"] < dic_minimo["views"]):
            dic_minimo = lista
    return dic_minimo







