# Lista de productos
menu = [
    ["Hamburguesa", "Comida Rapida", 25000],
    ["Pizza", "Comida Rapida", 30000],
    ["Ensalada", "Saludable", 18000],
    ["Jugo Natural", "Bebida", 12000],
    ["Carne Asada", "Plato Fuerte", 45000],
    ["Pasta", "Plato Fuerte", 28000]
]

# Función para calcular precio final
def calcular_precio_final(nombre, categoria, precio_base, categoria_objetivo, umbral):
    if categoria == categoria_objetivo and precio_base >= umbral:
        descuento = precio_base * 0.15
        precio_final = precio_base - descuento
    else:
        precio_final = precio_base
    return precio_final

# Parámetros de promoción
categoria_objetivo = "Plato Fuerte"
umbral = 25000

# Mostrar menú con promoción
print("------ MENÚ CON PROMOCIÓN ------")

for producto in menu:
    nombre = producto[0]
    categoria = producto[1]
    precio_base = producto[2]

    precio_final = calcular_precio_final(
        nombre, categoria, precio_base, categoria_objetivo, umbral
    )

    print(f"Producto: {nombre}")
    print(f"Categoría: {categoria}")
    print(f"Precio Base: {precio_base}")
    print(f"Precio Final: {precio_final}")
    print("-----------------------------")