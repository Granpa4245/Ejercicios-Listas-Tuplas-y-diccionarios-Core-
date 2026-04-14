

y = int(input("Ingrese un número del 1 al 6 para ejecutar: "))    

# Carga de Datos
ventas = [
    {"fecha": "2024-01-05", "producto": "Cocacola", "cantidad": 10, "precio": 15.0},
    {"fecha": "2024-01-06", "producto": "Pepsi", "cantidad": 5, "precio": 20.0},
    {"fecha": "2024-01-06", "producto": "Fanta", "cantidad": 8, "precio": 15.0},
    {"fecha": "2024-01-07", "producto": "Sprite", "cantidad": 12, "precio": 10.0},
    {"fecha": "2024-01-07", "producto": "7up", "cantidad": 7, "precio": 20.0},
]

# Cálculo de Ingresos Totales
ingresos_totales = 0
for venta in ventas:
    ingresos_totales += venta["cantidad"] * venta["precio"]
print(f"Ingresos Totales: {ingresos_totales}")

# Análisis del Producto Más Vendido
ventas_por_producto = {}
for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    if producto in ventas_por_producto:
        ventas_por_producto[producto] += cantidad
    else:
        ventas_por_producto[producto] = cantidad

# Identificar el producto más vendido
producto_mas_vendido = max(ventas_por_producto, key=ventas_por_producto.get)
cantidad_mas_vendida = ventas_por_producto[producto_mas_vendido]
print(f"Producto más vendido: {producto_mas_vendido} con {cantidad_mas_vendida} unidades vendidas")

# Promedio de Precio por Producto
precios_por_producto = {}
for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    precio = venta["precio"]
    if producto in precios_por_producto:
        precios_por_producto[producto] = (
            precios_por_producto[producto][0] + precio * cantidad,
            precios_por_producto[producto][1] + cantidad,
        )
    else:
        precios_por_producto[producto] = (precio * cantidad, cantidad)
precio_promedio_por_producto = {
    producto: total_precio / total_cantidad
    for producto, (total_precio, total_cantidad) in precios_por_producto.items()
}
print("Precio promedio por producto:")
for producto, precio_promedio in precio_promedio_por_producto.items():
    print(f"{producto}: {precio_promedio}")

# Ventas por Día
ingresos_por_dia = {}
for venta in ventas:
    fecha = venta["fecha"]
    cantidad = venta["cantidad"]
    precio = venta["precio"]
    if fecha in ingresos_por_dia:
        ingresos_por_dia[fecha] += cantidad * precio
    else:
        ingresos_por_dia[fecha] = cantidad * precio

print("Ingresos por día:")
for fecha, ingresos in ingresos_por_dia.items():
    print(f"{fecha}: {ingresos}")

# Representación de Datos
resumen_ventas = {}
for producto in ventas_por_producto:
    cantidad_total = ventas_por_producto[producto]
    ingresos_totales = precios_por_producto[producto][0]
    precio_promedio = precio_promedio_por_producto[producto]
    resumen_ventas[producto] = {
        "cantidad_total": cantidad_total,
        "ingresos_totales": ingresos_totales,
        "precio_promedio": precio_promedio,
    }
print("Resumen de ventas por producto:")
for producto, resumen in resumen_ventas.items():
    print(f"{producto}: {resumen}")



if y == 1:
    print("Lista de ventas original:")
    for venta in ventas:
        print(venta)
elif y == 2:
    print(f"Ingresos Totales: {ingresos_totales}")
elif y == 3:
    print(f"Producto más vendido: {producto_mas_vendido} con {cantidad_mas_vendida} unidades vendidas")
elif y == 4:
    print("Precio promedio por producto:")
    for producto, precio_promedio in precio_promedio_por_producto.items():
        print(f"{producto}: {precio_promedio}")
elif y == 5:
    print("Ingresos por día:")
    for fecha, ingresos in ingresos_por_dia.items():
        print(f"{fecha}: {ingresos}")
elif y == 6:
    print("Resumen de ventas por producto:")
    for producto, resumen in resumen_ventas.items():
        print(f"{producto}: {resumen}")
else:
    print("Número no válido. Por favor, ingrese un número del 1 al 6.")