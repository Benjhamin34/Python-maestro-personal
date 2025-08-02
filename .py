print("1. Agregar producto")
print("2. Eliminar producto")
print("3. Ver inventario")
print("4. Salir")

opcion = int(input("Seleccione una opción: "))
inventario = {}
#Iniciar un bucle para el menu

while opcion != 4:

    if opcion == 1:
        producto = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad del producto: "))
#Guardar el producto y la cantidad en el inventario
        inventario[producto] = cantidad
        print(f"Producto '{producto}' agregado al inventario.")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Ver inventario")
        print("4. Salir")
        opcion = int(input("Seleccione una opción: "))
    elif opcion == 2:
        producto = input("Ingrese el nombre del producto a eliminar: ")
        
        if producto in inventario:
            del inventario[producto]
            print(f"Producto '{producto}' eliminado del inventario.")
        else:
            print(f"Producto '{producto}' no encontrado en el inventario.")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Ver inventario")
        print("4. Salir")
        opcion = int(input("Seleccione una opción: "))
    elif opcion == 3:
        #Mostrar el inventario
        print("Inventario actual:", inventario)

        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Ver inventario")
        print("4. Salir")
        opcion = int(input("Seleccione una opción: "))

