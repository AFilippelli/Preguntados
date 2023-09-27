from data import lista_bzrp
from funciones_optimizadas import *

dic_retornado_mas_visto = {}
dic_retornado_menos_visto = {}
dic_retornado_mas_largo = {}

while True:
    opcion = mostrar_menu()
    if(opcion == "1"):
        dic_retornado_mas_visto = tema_maximo_minimo(lista_bzrp, "views", "maximo")
        if(dic_retornado_mas_visto == -1):
            print("falló algo")
        else:
            mostrar_tema(dic_retornado_mas_visto)
    elif(opcion == "2"):
        dic_retornado_menos_visto = tema_maximo_minimo(lista_bzrp, "views", "minimo")
        mostrar_tema(dic_retornado_menos_visto)
    elif(opcion == "3"):
        dic_retornado_mas_largo = tema_maximo_minimo(lista_bzrp, "length", "maximo")
        mostrar_tema(dic_retornado_mas_largo)
    elif(opcion == "4"):
        break