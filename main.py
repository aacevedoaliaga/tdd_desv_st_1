'''
Función pra calcular la deviación estandar
'''
def DESV(data):
    mean = sum(data) / len(data)
    squared_diff = [(x - mean) ** 2 for x in data]
    variance = sum(squared_diff) / len(data)
    std_dev = variance ** 0.5
    return mean, std_dev

if __name__ == '__main__':
    input_data = input("Ingresa los datos separados por espacios: ")
    data = [float(x) for x in input_data.split()]
    print("la media y la Desviación Estándar son:", DESV(data))