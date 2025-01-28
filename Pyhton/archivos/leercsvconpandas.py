import pandas as pd

# Usando la función read_csv para leer el archivo CSV
df = pd.read_csv("archivos\\datos.csv")
df2 = pd.read_csv("archivos\\datos.csv")

# Obteniendo los datos de la columna nombre
nombres = df["nombre"]

# Ordenando el dataframe por la edad de forma ascendente
df_orden_ascendente = df.sort_values("edad")

# Ordenándolo de forma descendente
df_orden_descendente = df.sort_values("edad", ascending=False)

# Concatenando los 2 dataframes
df_concatenado = pd.concat([df, df2])

# Accediendo a las primeras 3 filas con head()
primeras_filas = df.head(3)

# Accediendo a las últimas 3 filas con tail()
ultimas_filas = df.tail(3)

# Accediendo a la cantidad de filas y columnas con shape
filas_totales, columnas_totales = df.shape

# Obteniendo data estadística del dataframe:
df_info = df.describe()

# Accediendo a la edad de la fila 2
elemento_especifico_loc = df.loc[2, "edad"]

# Accediendo a la edad de la fila 2 con iloc
elemento_especifico_iloc = df.iloc[2, 2]

# Accediendo a todos los apellidos con loc
apellidos_loc = df.loc[:, "apellido"]

# Accediendo a todos los apellidos con iloc
apellidos = df.iloc[:, 1]

# Accediendo a la fila 3 con loc
fila_3_loc = df.loc[2, :]

# Accediendo a la fila 3 con iloc
fila_3_iloc = df.iloc[2, :]

# Accediendo a filas con edad mayor que 30 con loc
mayor_que_30 = df.loc[df["edad"] > 30, :]

# Obteniendo columnas específicas (nombre y edad)
nombres_edades = df[["nombre", "edad"]]

# Filtrando por nombres que empiecen con la letra 'A'
nombres_con_a = df[df["nombre"].str.startswith("A")]

# Eliminando la columna 'apellido' del dataframe
df_sin_apellido = df.drop(columns=["apellido"])

# Verificando si hay valores nulos
valores_nulos = df.isnull().sum()

# Reemplazando valores nulos en la columna 'edad' con la media
df["edad"].fillna(df["edad"].mean(), inplace=True)

# Imprimiendo resultados
print("Nombres:")
print(nombres)
print("\nDataFrame ordenado por edad (ascendente):")
print(df_orden_ascendente)
print("\nDataFrame ordenado por edad (descendente):")
print(df_orden_descendente)
print("\nPrimeras 3 filas:")
print(primeras_filas)
print("\nÚltimas 3 filas:")
print(ultimas_filas)
print(f"\nCantidad de filas: {filas_totales}, Cantidad de columnas: {columnas_totales}")
print("\nDescripción estadística del DataFrame:")
print(df_info)
print("\nEdad en la fila 2 (loc):", elemento_especifico_loc)
print("Edad en la fila 2 (iloc):", elemento_especifico_iloc)
print("\nApellidos:")
print(apellidos)
print("\nFila 3 (loc):")
print(fila_3_loc)
print("\nFila 3 (iloc):")
print(fila_3_iloc)
print("\nFilas con edad mayor que 30:")
print(mayor_que_30)
print("\nNombres y edades:")
print(nombres_edades)
print("\nNombres que empiezan con 'A':")
print(nombres_con_a)
print("\nDataFrame sin la columna 'apellido':")
print(df_sin_apellido)
print("\nValores nulos por columna:")
print(valores_nulos)

