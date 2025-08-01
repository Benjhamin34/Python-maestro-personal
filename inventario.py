# 1. menu de opciones
print("1. Agregar producto")
print("2. Eliminar producto")
print("3. Ver inventario")
print("4. Salir")
opcion = input("Seleccione una opción: ")
while opcion != 4:
    productos = []
    if opcion == "1":
        producto = input("Agrege un producto: ")
        productos.append(producto)
        print(f"Producto '{producto}' agregado al inventario.")
    elif opcion == "2":
        producto = input("elimine un producto: ")
        if producto in productos:
            productos.remove(producto)
            print(f"Producto '{producto}' eliminado del inventario.")
    elif opcion == "3":
        print("Inventario actual:", productos)
    opcion = input("Seleccione una opción: ")