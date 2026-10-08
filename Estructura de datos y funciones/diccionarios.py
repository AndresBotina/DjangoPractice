# 4.1. Todos los Métodos de Diccionarios
# Demostración de los 10 métodos integrados en diccionarios para la
# administración de perfiles.

def demostrar_metodos_diccionarios():
    perfil = {"id": 101, "usuario": "mgarcia", "rol": "admin"}
    print("Perfil inicial:", perfil)

    # 1. get(key, default): lectura segura sin lanzar KeyError
    email = perfil.get("email", "sin_correo@dominio.com")
    print("1. get('email'):", email)

    # 2. setdefault(key, default): retorna el valor o lo asigna si no existe
    estado = perfil.setdefault("activo", True)
    print("2. setdefault('activo'):", estado, "->", perfil)

    # 3. update(dict2): actualiza y añade pares clave-valor
    perfil.update({"rol": "superadmin", "ciudad": "Bogotá"})
    print("3. update:", perfil)

    # 4. keys(): obtiene todas las claves
    lista_claves = list(perfil.keys())
    print("4. keys:", lista_claves)

    # 5. values(): obtiene todos los valores
    lista_valores = list(perfil.values())
    print("5. values:", lista_valores)

    # 6. items(): obtiene los pares (clave, valor)
    lista_pares = list(perfil.items())
    print("6. items:", lista_pares)

    # 7. copy(): crea una copia superficial
    respaldo = perfil.copy()
    print("7. copy:", respaldo)

    # 8. pop(key): elimina la clave y devuelve su valor
    rol_eliminado = perfil.pop("rol")
    print("8. pop('rol'):", rol_eliminado, "->", perfil)

    # 9. popitem(): elimina y devuelve el último par (clave, valor)
    ultimo_par = perfil.popitem()
    print("9. popitem:", ultimo_par, "->", perfil)

    # 10. clear(): elimina todas las parejas clave-valor
    perfil.clear()
    print("10. clear:", perfil)

    return respaldo


respaldo = demostrar_metodos_diccionarios()
print("Copia de respaldo devuelta:", respaldo)
