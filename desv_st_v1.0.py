# Solicitar al usuario que ingrese los datos (separados por espacios)
input_data = input("Ingresa los datos separados por espacios: ")

# Convertir la entrada en una lista de números
data = [float(x) for x in input_data.split()]

# Calcular la media
mean = sum(data) / len(data)

# Calcular las diferencias al cuadrado respecto a la media
squared_diff = [(x - mean) ** 2 for x in data]

# Calcular la varianza
variance = sum(squared_diff) / len(data)

# Calcular la desviación estándar (raíz cuadrada de la varianza)
std_dev = variance ** 0.5

# Imprimir el resultado
print("Desviación Estándar:", std_dev)