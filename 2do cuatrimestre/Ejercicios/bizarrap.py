from data import lista_bzrp
maximo = lista_bzrp[0]["views"]
nombre_maximo = lista_bzrp[0]["title"]

for e_lista in lista_bzrp:
    if e_lista["views"] > maximo:
        maximo = e_lista["views"]
        nombre_maximo = e_lista["title"]
print(nombre_maximo, maximo)
print()