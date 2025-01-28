cadena1 = "Hola,Skerecito,Como,Estas"
cadena2 = "Bienvenido Ñerito"

resultado = dir(cadena1)
print("Resultado de dir(cadena1):", resultado)

mayusc = cadena1.upper()
print("Cadena en mayúsculas:", mayusc)

minusc = cadena1.lower()
print("Cadena en minúsculas:", minusc)

primer_letra_mayusc = cadena1.capitalize()
print("Primera letra en mayúscula:", primer_letra_mayusc)

busqueda_find = cadena1.find("D")
print("Resultado de find('D'):", busqueda_find)

busqueda_index = cadena1.index("H")
print("Resultado de index('H'):", busqueda_index)

es_numerico = cadena1.isnumeric()
print("¿Es numérico?:", es_numerico)

es_alfanumerico = cadena1.isalpha()
print("¿Es alfanumérico?:", es_alfanumerico)

contar_coincidencias = cadena1.count("la ma")
print("Cantidad de coincidencias con 'la ma':", contar_coincidencias)

contar_caracteres = len(cadena1)
print("Cantidad de caracteres:", contar_caracteres)

empieza_con = cadena1.startswith("H")
print("¿Empieza con 'H'?:", empieza_con)

termina_con = cadena1.endswith("H")
print("¿Termina con 'H'?:", termina_con)

cadena_nueva = cadena1.replace("Skerecito", "Mis temachers")
print("Cadena de Skerecitos remplazadas por Temachers:", cadena_nueva)

cadena_nueva2 = cadena1.replace(",", " ")
print("Cadena con comas reemplazadas por espacios:", cadena_nueva2)

cadena_separada = cadena1.split(",")
print("Cadena separada por comas:", cadena_separada)


