# data_manager.py
import json
from camion import Camion, Reparacion

def cargar_inventario(nombre_archivo="camiones.json"):
    """
    Carga el inventario de camiones desde un archivo JSON.
    """
    inventario = {}
    try:
        with open(nombre_archivo, 'r') as archivo:
            datos_cargados = json.load(archivo)
            for placa, datos in datos_cargados.items():
                reparaciones_dict = datos.pop('reparaciones', [])
                reparaciones_obj = [Reparacion(**rep) for rep in reparaciones_dict]
                
                if 'chofer' not in datos:
                    datos['chofer'] = 'Desconocido'
                
                camion_obj = Camion(**datos, reparaciones=reparaciones_obj)
                inventario[placa] = camion_obj
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no fue encontrado. Se creará uno nuevo.")
    except json.JSONDecodeError:
        print(f"Error al leer el archivo '{nombre_archivo}'. El archivo está corrupto.")
    return inventario

def guardar_inventario(inventario, nombre_archivo="camiones.json"):
    """
    Guarda el inventario de camiones en un archivo JSON.
    """
    datos_a_guardar = {placa: camion.to_dict() for placa, camion in inventario.items()}
    with open(nombre_archivo, 'w') as archivo:
        json.dump(datos_a_guardar, archivo, indent=4)
    print(f"Inventario guardado en '{nombre_archivo}'.")

def calcular_costo_total(inventario):
    """
    Calcula el costo total de todas las reparaciones en el inventario.
    """
    costo_total = sum(rep.costo for camion in inventario.values() for rep in camion.reparaciones)
    return costo_total