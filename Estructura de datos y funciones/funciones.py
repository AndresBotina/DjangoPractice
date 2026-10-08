# 5.1. Ejemplos Avanzados de Funciones
# A. Parámetros Nombrados y Valores Predeterminados

def calcular_factura(monto_base, impuesto=0.19, descuento=0.0):
    """
    Calcula el costo total aplicando un descuento previo e impuestos.
    """
    monto_descontado = monto_base * (1 - descuento)
    monto_total = monto_descontado * (1 + impuesto)
    return round(monto_total, 2)


# Llamadas con distintas configuraciones de argumentos
total_estandar = calcular_factura(100.0)                   # Impuesto 19%, desc 0% -> 119.0
total_promocion = calcular_factura(100.0, descuento=0.10)  # Impuesto 19%, desc 10% -> 107.1

print("Total estándar:", total_estandar)
print("Total promoción:", total_promocion)
