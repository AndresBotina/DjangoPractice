# 2.1. Todos los Métodos de Listas
# Uso práctico de los 11 métodos propios de las listas dentro de una función
# de gestión de inventario.

def demostrar_metodos_listas():
    # Inicialización
    productos = ["laptop", "mouse"]
    print("Lista inicial:", productos)

    # 1. append(x): agrega al final
    productos.append("teclado")
    print("1. append:", productos)

    # 2. insert(i, x): inserta en la posición i
    productos.insert(1, "monitor")
    print("2. insert:", productos)

    # 3. extend(iterable): añade múltiples elementos
    productos.extend(["pantalla", "mouse"])
    print("3. extend:", productos)

    # 4. count(x): cuenta las apariciones del elemento
    cant_mouses = productos.count("mouse")
    print("4. count('mouse'):", cant_mouses)

    # 5. index(x): devuelve el primer índice del elemento
    pos_monitor = productos.index("monitor")
    print("5. index('monitor'):", pos_monitor)

    # 6. sort(): ordena la lista (orden alfabético)
    productos.sort()
    print("6. sort:", productos)

    # 7. reverse(): invierte el orden actual
    productos.reverse()
    print("7. reverse:", productos)

    # 8. copy(): crea una copia independiente
    copia_respaldo = productos.copy()
    print("8. copy:", copia_respaldo)

    # 9. pop([i]): extrae y devuelve el elemento en i (por defecto el último)
    ultimo_item = productos.pop()
    print("9. pop:", ultimo_item, "->", productos)

    # 10. remove(x): elimina la primera aparición de x
    productos.remove("mouse")
    print("10. remove('mouse'):", productos)

    # 11. clear(): vacía todos los elementos de la lista
    productos.clear()
    print("11. clear:", productos)

    return copia_respaldo


respaldo = demostrar_metodos_listas()
print("Copia de respaldo devuelta:", respaldo)
