print("----- LISTA DE VENTAS ORIGINAL -----")
ventas = [
    {"fecha": "2024-01-05", "producto": "Cocacola", "cantidad": 10, "precio": 15.0},
    {"fecha": "2024-01-06", "producto": "Pepsi", "cantidad": 5, "precio": 20.0},
    {"fecha": "2024-01-06", "producto": "Fanta", "cantidad": 8, "precio": 15.0},
    {"fecha": "2024-01-07", "producto": "Sprite", "cantidad": 12, "precio": 10.0},
    {"fecha": "2024-01-07", "producto": "7up", "cantidad": 7, "precio": 20.0},
]

for venta in ventas:
    print(venta)

# =========================
# INGRESOS TOTALES
# =========================
ingresos_totales = 0
for venta in ventas:
    ingresos_totales += venta["cantidad"] * venta["precio"]

print("\n----- INGRESOS TOTALES -----")
print(f"Total generado: {ingresos_totales}")

# =========================
# PRODUCTO MÁS VENDIDO
# =========================
ventas_por_producto = {}

for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]

    if producto in ventas_por_producto:
        ventas_por_producto[producto] += cantidad
    else:
        ventas_por_producto[producto] = cantidad

producto_mas_vendido = max(ventas_por_producto, key=ventas_por_producto.get)
cantidad_mas_vendida = ventas_por_producto[producto_mas_vendido]

print("\n----- PRODUCTO MÁS VENDIDO -----")
print(f"{producto_mas_vendido} con {cantidad_mas_vendida} unidades")

# =========================
# PRECIO PROMEDIO
# =========================
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

print("\n----- PRECIO PROMEDIO POR PRODUCTO -----")
for producto, precio_promedio in precio_promedio_por_producto.items():
    print(f"{producto}: {precio_promedio:.2f}")

# =========================
# INGRESOS POR DÍA
# =========================
ingresos_por_dia = {}

for venta in ventas:
    fecha = venta["fecha"]
    ingresos = venta["cantidad"] * venta["precio"]

    if fecha in ingresos_por_dia:
        ingresos_por_dia[fecha] += ingresos
    else:
        ingresos_por_dia[fecha] = ingresos

print("\n----- INGRESOS POR DÍA -----")
for fecha, ingresos in ingresos_por_dia.items():
    print(f"{fecha}: {ingresos}")

# =========================
# RESUMEN FINAL
# =========================
resumen_ventas = {}

for producto in ventas_por_producto:
    resumen_ventas[producto] = {
        "cantidad_total": ventas_por_producto[producto],
        "ingresos_totales": precios_por_producto[producto][0],
        "precio_promedio": precio_promedio_por_producto[producto],
    }

print("\n----- RESUMEN DE VENTAS -----")
for producto, datos in resumen_ventas.items():
    print(f"{producto}: {datos}")
