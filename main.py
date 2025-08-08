# main.py
import json
from camion import Camion, Reparacion
from data_manager import cargar_inventario, guardar_inventario, calcular_costo_total

# --- Funciones de Reportes (estas deben estar definidas antes de ser llamadas) ---
def generar_reporte_reparaciones_pendientes(camiones):
    print("\n--- Reporte de Reparaciones Pendientes ---")
    encontrado = False
    for camion in camiones.values():
        reparaciones_pendientes = [rep for rep in camion.reparaciones if rep.estado.lower() == 'pendiente']
        if reparaciones_pendientes:
            encontrado = True
            print(f"Camión Placa: {camion.placa}, Propietario: {camion.propietario}")
            for rep in reparaciones_pendientes:
                print(f"  - {rep.descripcion} (Costo: ${rep.costo})")
            print("-" * 40)
    if not encontrado:
        print("No hay reparaciones pendientes en el inventario.")
    print("-----------------------------------------")

def generar_reporte_costo_total_reparaciones(camiones):
    print("\n--- Reporte de Costo Total de Reparaciones por Camión ---")
    encontrado = False
    for camion in camiones.values():
        if camion.reparaciones:
            encontrado = True
            costo_total = sum(rep.costo for rep in camion.reparaciones)
            print(f"Camión Placa: {camion.placa}, Propietario: {camion.propietario}")
            print(f"  - Costo Total de Reparaciones: ${costo_total}")
            print("-" * 40)
    if not encontrado:
        print("No hay camiones con reparaciones registradas.")
    print("-------------------------------------------------------")

# --- Funciones para cada opción del menú ---
def mostrar_menu():
    print("\n--- Menú Principal ---")
    print("1. Registrar Camion")
    print("2. Eliminar Camion")
    print("3. Ver inventario")
    print("4. Actualizar inventario")
    print("5. Registrar Reparación")
    print("6. Actualizar Reparación")
    print("7. Buscar Camión")
    print("8. Generar Reportes")
    print("9. Salir")

def registrar_camion(inventario):
    print("\n--- Registrar Nuevo Camión ---")
    marca = input("Ingrese la marca del camion: ")
    modelo = input("Ingrese el modelo del camion: ")
    anio = int(input("Ingrese el año del camion: "))
    propietario = input("Ingrese el nombre del propietario: ")
    chofer = input("Ingrese el nombre del chofer: ")
    placa = input("Ingrese la placa del camion: ")
    kilometraje = int(input("Ingrese el kilometraje del camion: "))
    
    nuevo_camion = Camion(marca, modelo, anio, propietario, chofer, placa, kilometraje)
    inventario[placa] = nuevo_camion
    print(f"Camion {placa} registrado exitosamente.")

def eliminar_camion(inventario):
    print("\n--- Eliminar Camión ---")
    placa = input("Ingrese la placa del camion a eliminar: ")
    if placa in inventario:
        del inventario[placa]
        print(f"Camion {placa} eliminado exitosamente.")
    else:
        print(f"No se encontró un camion con la placa {placa}.")

def ver_inventario(inventario):
    print("\n--- Inventario de Camiones ---")
    if not inventario:
        print("No hay camiones registrados.")
    else:
        for camion_obj in inventario.values():
            camion_obj.mostrar_info()
            print("-" * 40)

def actualizar_camion(inventario):
    print("\n--- Actualizar Inventario ---")
    placa = input("Ingrese la placa del camion a actualizar: ")
    if placa in inventario:
        camion_actual = inventario[placa]
        print("Ingrese los nuevos datos del camion (deje en blanco para no cambiar):")
        marca = input(f"Marca ({camion_actual.marca}): ") or camion_actual.marca
        modelo = input(f"Modelo ({camion_actual.modelo}): ") or camion_actual.modelo
        anio_input = input(f"Año ({camion_actual.anio}): ")
        anio = int(anio_input) if anio_input else camion_actual.anio
        propietario = input(f"Propietario ({camion_actual.propietario}): ") or camion_actual.propietario
        chofer = input(f"Chofer ({camion_actual.chofer}): ") or camion_actual.chofer
        kilometraje_input = input(f"Kilometraje ({camion_actual.kilometraje} Km): ")
        kilometraje = int(kilometraje_input) if kilometraje_input else camion_actual.kilometraje
        
        camion_actual.marca = marca
        camion_actual.modelo = modelo
        camion_actual.anio = anio
        camion_actual.propietario = propietario
        camion_actual.chofer = chofer
        camion_actual.kilometraje = kilometraje
        
        print(f"Camion {placa} actualizado exitosamente.")
    else:
        print(f"No se encontró un camion con la placa {placa}.")

def registrar_reparacion(inventario):
    print("\n--- Registrar Reparación ---")
    placa = input("Ingrese la placa del camion para registrar la reparación: ")
    if placa in inventario:
        camion = inventario[placa]
        descripcion = input("Ingrese la descripción de la reparación: ")
        try:
            costo = float(input("Ingrese el costo de la reparación: "))
            nueva_reparacion = Reparacion(descripcion, costo)
            camion.reparaciones.append(nueva_reparacion)
            print(f"Reparación para el camión {placa} registrada exitosamente.")
        except ValueError:
            print("El costo ingresado no es un número válido.")
    else:
        print(f"No se encontró un camion con la placa {placa}.")

def actualizar_reparacion(inventario):
    print("\n--- Actualizar Reparación ---")
    placa = input("Ingrese la placa del camion para actualizar una reparación: ")
    if placa in inventario:
        camion = inventario[placa]
        camion.mostrar_info()
        try:
            indice = int(input("Ingrese el número de la reparación a actualizar: ")) - 1
            if 0 <= indice < len(camion.reparaciones):
                reparacion = camion.reparaciones[indice]
                print(f"Reparación seleccionada: {reparacion}")
                nuevo_estado = input(f"Ingrese el nuevo estado ({reparacion.estado}): ") or reparacion.estado
                reparacion.estado = nuevo_estado
                print("Reparación actualizada exitosamente.")
            else:
                print("Número de reparación no válido.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    else:
        print(f"No se encontró un camion con la placa {placa}.")

def buscar_camion(inventario):
    print("\n--- Buscar Camión ---")
    placa_busqueda = input("Ingrese la placa del camión que desea buscar: ")
    if placa_busqueda in inventario:
        print("\n--- Camión Encontrado ---")
        camion_encontrado = inventario[placa_busqueda]
        camion_encontrado.mostrar_info()
        print("-----------------------")
    else:
        print(f"No se encontró un camión con la placa {placa_busqueda}.")

def generar_reportes(inventario):
    print("\n--- Menú de Reportes ---")
    print("1. Ver reparaciones pendientes")
    print("2. Ver costo total de reparaciones por camión")
    print("3. Ver costo total de todas las reparaciones")
    opcion_reporte = input("Seleccione una opción de reporte: ")
    
    if opcion_reporte == '1':
        generar_reporte_reparaciones_pendientes(inventario)
    elif opcion_reporte == '2':
        generar_reporte_costo_total_reparaciones(inventario)
    elif opcion_reporte == '3':
        costo_total_general = calcular_costo_total(inventario)
        print(f"\n--- Costo Total General de Todas las Reparaciones ---")
        print(f"Costo Total: ${costo_total_general}")
        print("--------------------------------------------------")
    else:
        print("Opción de reporte no válida.")


# --- Lógica principal del programa ---
if __name__ == "__main__":
    Camiones_del_taller = cargar_inventario()
    opcion = 0
    
    while opcion != 9:
        try:
            mostrar_menu()
            opcion = int(input("Seleccione una opción: "))
            
            if opcion == 1:
                registrar_camion(Camiones_del_taller)
            elif opcion == 2:
                eliminar_camion(Camiones_del_taller)
            elif opcion == 3:
                ver_inventario(Camiones_del_taller)
            elif opcion == 4:
                actualizar_camion(Camiones_del_taller)
            elif opcion == 5:
                registrar_reparacion(Camiones_del_taller)
            elif opcion == 6:
                actualizar_reparacion(Camiones_del_taller)
            elif opcion == 7:
                buscar_camion(Camiones_del_taller)
            elif opcion == 8:
                generar_reportes(Camiones_del_taller)
            else:
                print("Opción no válida. Por favor, intente de nuevo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue
            
    guardar_inventario(Camiones_del_taller)