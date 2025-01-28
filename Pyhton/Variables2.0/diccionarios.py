#no se puede crear ningun tipo de datos vacios sin usar las funciones que necesitamos
diccionaraio = dict(nombre = 'Braulio', apellido = 'Moreno', followers = 940)

print(diccionaraio)

#Duplas como claves

diccionario2 = {("Braulio", "El the best"): "jajas"}
print(diccionario2)

diccionario3 = {frozenset(["Braulio", "El the best"]): "jajas"}
print(diccionario3)

#Hace que cada letra itere el primer dato
diccionario4 = dict.fromkeys(["nombre", "apellido"])
print(diccionario4)

diccionario5 = dict.fromkeys(["nombre","apellido"],"No sé")
print(diccionario5)