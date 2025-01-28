# Creando una lista con list()
lista = list([34, 56, 23, True, False])
print("Lista inicial:", lista)

# Devuelve la cantidad de elementos de la lista
cantidad_elementos = len(lista)
print("Cantidad de elementos en la lista:", cantidad_elementos)

# Agregando un elemento a la lista
lista.append(65)
print("Lista después de agregar 65:", lista)

# Agregando un elemento a la lista en un índice específico
lista.insert(2, "TOMA MAMA")
print("Lista después de insertar 'TOMA MAMA' en el índice 2:", lista)

# Agregando varios elementos a la lista
lista.extend([False, 2030])
print("Lista después de extender con [False, 2030]:", lista)

# Eliminando un elemento de la lista (por su índice)
lista.pop(3)  # -1 para eliminar el último, -2 para eliminar el anteúltimo, etc.
print("Lista después de hacer pop en el índice 3:", lista)

# Removiendo un elemento de la lista por su valor
lista.remove("TOMA MAMA")
print("Lista después de remover 'TOMA MAMA':", lista)

# Verificando si un elemento está en la lista antes de hacer algo
if 100 in lista:
    print("El número 100 se encuentra en la lista.")
else:
    print("El número 100 no está en la lista, pero lo voy a agregar.")
    lista.append(100)
print("Lista después de verificar/agregar 100:", lista)

# Ordenando la lista de forma ascendente (funciona si no hay mezclas raras de tipos)
try:
    lista.sort()
    print("Lista ordenada de forma ascendente:", lista)
except TypeError:
    print("Error al intentar ordenar la lista: contiene tipos incompatibles.")

# Invirtiendo los elementos de la lista
lista.reverse()
print("Lista después de invertir los elementos:", lista)

# Verificando si un elemento se encuentra en la lista
try:
    elemento_encontrado = lista.index(56)
    print("El elemento 56 se encuentra en el índice:", elemento_encontrado)
except ValueError:
    print("El elemento 56 no está en la lista.")

# Contando cuántas veces aparece un elemento específico
cantidad_falsos = lista.count(False)
print("Cantidad de veces que aparece 'False' en la lista:", cantidad_falsos)

# Clonando la lista para no afectar la original si se modifica
lista_clonada = lista.copy()
print("Lista clonada para pruebas futuras:", lista_clonada)

# Eliminando todos los elementos de la lista
lista.clear()
print("Lista después de usar clear():", lista)
