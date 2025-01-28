diccionario = {
    "nombre" : 'Braulio',
    "apellido" : 'Moreno',
    "foollowers en instagram" : 940, 
}

claves = diccionario.get("nombre")#Devuleve algo sin parar de correr todo el codigo 

#nos devuelve un objeto dict_item
claves = diccionario.keys()

#obteniendo un elemento con get() (si no encuentra nada el programa continùa)
valor_de_kasdks = diccionario.get("kasdks")
print("hola papa, el programa continua")

#eliminando todo del diccionario
#diccionario.clear()

#eliminando un elemento del diccionario
diccionario.pop("foollowers en instagram")

#obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()

print(diccionario_iterable) 