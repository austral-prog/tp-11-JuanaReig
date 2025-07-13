def read_file_to_dict(filename):
    ventas = {}
    with open(filename, 'r') as archivo:
        linea = archivo.readline().strip()
        registros = linea.split(';')
        for registro in registros:
            if registro == '':
                continue
            producto, monto = registro.split(':')
            monto = float(monto)
            if producto not in ventas:
                ventas[producto] = []
            ventas[producto].append(monto)
    return ventas
    
def process_dict(diccionario):
    for producto in diccionario:
        montos = diccionario[producto]
        total = sum(montos)
        promedio = total / len(montos)
        print(f"{producto}: ventas totales ${total:.2f}, promedio ${promedio:.2f}")

