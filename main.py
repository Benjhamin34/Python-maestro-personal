import json
from camion import Camion

def mostrar_menu():
    print("1. Registrar Camion")
    print("2. Eliminar Camion")
    print("3. Ver inventario")
    print("4. Actualizar inventario")
    print("5. Salir")

Camiones_del_taller = {}
opcion = 0

try:
    with open('camiones.json', 'r') as archivo:
        datos_cargados = json.load(archivo)
        for placa, datos in datos_cargados.items():
            camion_obj = Camion(**datos)
            Camiones_del_taller[placa] = camion_obj
except FileNotFoundError:
    print("El archivo 'camiones.json' no fue encontrado.")
except json.JSONDecodeError:
    print("Error al leer el archivo JSON.")

while opcion != 5:
    try:
        mostrar_menu()
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue

    if opcion == 1:
        marca = input("Ingrese la marca del camion: ")
        modelo = input("Ingrese el modelo del camion: ")
        anio = int(input("Ingrese el año del camion: "))
        propietario = input("Ingrese el nombre del propietario: ")
        placa = input("Ingrese la placa del camion: ")
        kilometraje = int(input("Ingrese el kilometraje del camion: "))

        nuevo_camion = Camion(marca, modelo, anio, propietario, placa, kilometraje)
        Camiones_del_taller[placa] = nuevo_camion
        print(f"Camion {placa} registrado exitosamente.")
    elif opcion == 2:
        placa = input("Ingrese la placa del camion a eliminar: ")
        if placa in Camiones_del_taller:
            del Camiones_del_taller[placa]
            print(f"Camion {placa} eliminado exitosamente.")
        else:
            print(f"No se encontró un camion con la placa {placa}.")
    elif opcion == 3:
        if not Camiones_del_taller:
            print("No hay camiones registrados.")
        else:
            print("Inventario de camiones:")
            for camion_obj in Camiones_del_taller.values():
                camion_obj.mostrar_info()
                print("-" * 40)
    elif opcion == 4:
        placa = input("Ingrese la placa del camion a actualizar: ")
        if placa in Camiones_del_taller:
            camion_actual = Camiones_del_taller[placa]
            print("Ingrese los nuevos datos del camion (deje en blanco para no cambiar):")
            marca = input(f"Marca ({camion_actual.marca}): ") or camion_actual.marca
            modelo = input(f"Modelo ({camion_actual.modelo}): ") or camion_actual.modelo

            anio_input = input(f"Año ({camion_actual.anio}): ")
            anio = int(anio_input) if anio_input else camion_actual.anio

            propietario = input(f"Propietario ({camion_actual.propietario}): ") or camion_actual.propietario
            kilometraje_input = input(f"Kilometraje ({camion_actual.kilometraje} Km): ")
            kilometraje = int(kilometraje_input) if kilometraje_input else camion_actual.kilometraje

            camion_actual.marca = marca
            camion_actual.modelo = modelo
            camion_actual.anio = anio
            camion_actual.propietario = propietario
            camion_actual.kilometraje = kilometraje

            print(f"Camion {placa} actualizado exitosamente.")
        else:
            print(f"No se encontró un camion con la placa {placa}.")
    elif opcion != 5:
        print("Opción no válida. Por favor, intente de nuevo.")

datos_a_guardar = {placa: camion_obj.to_dict() for placa, camion_obj in Camiones_del_taller.items()}
with open('camiones.json', 'w') as archivo:
    json.dump(datos_a_guardar, archivo, indent=4)
    print("Inventario guardado en 'camiones.json'.")