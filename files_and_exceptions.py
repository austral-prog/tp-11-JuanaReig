def read_file_to_dict(filename):
    ventas = {}
    try:
        with open(filename, 'r') as archivo:
            linea = archivo.readline().strip()
            registros = linea.split(';')

            for registro in registros:
                if registro == '':
                    continue  # saltea el último elemento vacío si termina en ;
                producto, monto = registro.split(':')
                monto = float(monto)
                if producto not in ventas:
                    ventas[producto] = []
                ventas[producto].append(monto)

    except FileNotFoundError:
        print(f"Error: el archivo '{filename}' no existe.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
    return {}

def process_dict(diccionario):
    for producto, montos in diccionario.items():
        total = sum(montos)
        promedio = total / len(montos)
        print(f"{producto}: ventas totales ${total:.2f}, promedio ${promedio:.2f}")    """Para cada producto, imprime el total de ventas y el promedio, en el orden natural del diccionario.

    :param data: dict - diccionario a procesar.
    :return: None
    """
    pass
