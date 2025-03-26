def calcular_precio_venta(ingredientes, costos_fijos, margen_ganancia):
    """
    Calcula el precio de venta de una hamburguesa.
    :param ingredientes: Diccionario con los costos de ingredientes.
    :param costos_fijos: Costo fijo por hamburguesa.
    :param margen_ganancia: Porcentaje de utilidad sobre el costo total (ej. 30 para 30%).
    :return: Precio de venta de la hamburguesa.
    """
    costo_ingredientes = sum(ingredientes.values())
    costo_total = costo_ingredientes + costos_fijos
    precio_venta = costo_total * (1 + margen_ganancia / 100)
    
    return round(precio_venta, 2)

# Definir costos de ingredientes por unidad basados en precios de la canasta básica mexicana hasta marzo de 2025
ingredientes = {
    "pan": 2.00,       # Precio estimado por pieza
    "carne": 25.00,    # Precio estimado por porción
    "queso": 5.00,     # Precio estimado por rebanada
    "mayonesa": 0.50,  # Precio estimado por porción
    "ketchup": 0.50,   # Precio estimado por porción
    "mostaza": 0.50    # Precio estimado por porción
}

# Otros costos fijos por hamburguesa
costo_empaque = 5.00       # Precio estimado
salario_empleados = 300.00   # Costo prorrateado por unidad
alquiler = 5000.00            # Costo prorrateado por unidad
costos_fijos = costo_empaque + salario_empleados + alquiler

# Margen de ganancia deseado en porcentaje
margen_ganancia = 30  # 30%

# Calcular precio de venta
precio_venta = calcular_precio_venta(ingredientes, costos_fijos, margen_ganancia)
print(f"El precio de venta de la hamburguesa es: ${precio_venta}")
