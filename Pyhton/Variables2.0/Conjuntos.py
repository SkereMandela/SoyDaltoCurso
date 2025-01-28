# Creando un conjunto
conjunto = set(["Dato 1"])
print("Conjunto inicial:", conjunto)

# Metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato 1", "dato 2"])
conjunto2 = {conjunto1, "dato 3"}
print("Conjunto que contiene un frozenset y otro elemento:", conjunto2)

# Teoría de conjuntos
conjunto1 = {1, 3, 5, 7}
conjunto2 = {1, 3, 7}

# Verificando si conjunto1 es subconjunto de conjunto2
resultado = conjunto1.issubset(conjunto2)
print("¿conjunto1 es un subconjunto de conjunto2?", resultado)

conjunto3 = {1, 3, 5, 7}
conjunto4 = {2, 4, 7, 8}


print("----------------")
# Verificando si conjunto3 es subconjunto de conjunto4
resultado1_1 = conjunto3.issubset(conjunto4)
print("¿conjunto3 es un subconjunto de conjunto4?", resultado1_1)
print("----------------")


print("----------------")
# Alternativa para verificar si es subconjunto
resultado1_2 = conjunto1 <= conjunto2
print("¿conjunto1 <= conjunto2?", resultado1_2)
print("----------------")



print("----------------")
# Verificando si conjunto3 es un superconjunto de conjunto4
resultado2_1 = conjunto3.issuperset(conjunto4)
print("¿conjunto3 es un superconjunto de conjunto4?", resultado2_1)
print("----------------")


print("----------------")
# Alternativa para verificar si es un superconjunto
resultado2_2 = conjunto1 > conjunto2
print("¿conjunto1 > conjunto2?", resultado2_2)
print("----------------")



print("----------------")
# Verificar si conjunto2 y conjunto1 no tienen elementos en común
resultado = conjunto2.isdisjoint(conjunto1)
print("¿conjunto2 y conjunto1 no tienen elementos en común?", resultado)
