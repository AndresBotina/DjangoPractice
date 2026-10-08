# 3.1. Todos los Métodos de Tuplas
# Dado su carácter inmutable, las tuplas poseen únicamente 2 métodos integrados.

def analizar_tupla_mediciones(datos):
    print("Tupla de mediciones:", datos)

    # 1. count(x): cuenta las apariciones del elemento
    cant_ceros = datos.count(0)
    print("1. count(0):", cant_ceros)

    # 2. index(x): devuelve el primer índice del elemento
    pos_maximo = datos.index(100)
    print("2. index(100):", pos_maximo)

    return cant_ceros, pos_maximo


mediciones = (0, 25, 40, 0, 100, 0)
resultado = analizar_tupla_mediciones(mediciones)
print("Resultado devuelto:", resultado)
