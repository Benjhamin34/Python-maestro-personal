import json
def mostrar_menu():
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Ver inventario")
    print("4. Actualizar inventario")
    print("5. Salir")

inventario = {}
opcion = 0
try:
    with open("Inventario.json", "r") as archivo:
        inventario = json.load(archivo)
except FileNotFoundError:
    inventario = {}

while opcion != 5:
    mostrar_menu()
    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        opcion = 0

    if opcion == 1:
        producto = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad del producto: "))
        inventario[producto] = cantidad
        print(f"Producto '{producto}' agregado al inventario.")
    elif opcion == 2:
        producto = input("Ingrese el nombre del producto a eliminar: ")
        if producto in inventario:
            del inventario[producto]
            print(f"Producto '{producto}' eliminado del inventario.")
        else:
            print(f"Producto '{producto}' no encontrado en el inventario.")
    elif opcion == 3:
        print("Inventario actual:", inventario)
    elif opcion == 4:
        producto = input("Ingrese el nombre del producto a actualizar: ")
        if producto in inventario:
            nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
            inventario[producto] = nueva_cantidad
            print(f"Cantidad de '{producto}' actualizada a {nueva_cantidad}.")
        else:
            print(f"Producto '{producto}' no encontrado en el inventario.")
    elif opcion != 5:
        print("Opción no válida. Por favor, intente de nuevo.")


print("Gracias por usar el inventario. ¡Hasta luego!")
with open("inventario.json", "w") as archivo:
    json.dump(inventario, archivo)
print("Inventario guardado en 'inventario.json'.")