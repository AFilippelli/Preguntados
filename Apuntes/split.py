import re


print(re.split("[a-z ]+", "hola mundo 125c"))
print(re.split("[0-9 ]+", "hola mundo 125c"))
print(re.split("[hola|chau ] ", "hola mundo chau "))


texto = "uno 1 dos 2 tres 3 cuatro 44"
print(re.findall(" ", texto))
#print(re.findall("[0-9]", texto)) el + adelante del 9 sirve para que ademas de numeros 
#del 0-9 tambien tome numeros mayores a 10
print(re.findall("[0-9]+", texto))
print(re.findall("[a-zA-Z]", texto))

texto = "QUEVEDO || BZRP Music Session #52"

print(re.split("\|+ ", texto))

fecha = "2022-02-03 19:20:33"

print(re.findall("[0-9]{4}-[0-9]{2}-[0-9]{2}", fecha)) #['2022-02-03']
print(re.findall("[0-9]{4}", fecha)) #['2022']
print(re.findall("-([0-9]{2})-", fecha))#['02']
print(re.findall("-([0-9]{2}) ", fecha))#['03']
