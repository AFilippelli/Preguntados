acumulador = 0

for x in range(5):
    numero = int(input(f"Ingrese el {x+1}º numero"))
    acumulador += numero

print(f"Acumulado: {acumulador}")    


color = "azul"
#match = switch
match color:
    case "azul":
        print("Es azul")
    case "rojo":
        print("Es rojo")
    case "amarillo":
        print("Es amarillo")
    case "verde":
        print("Es verde")
    case other:
        print("Es otro color")                 
