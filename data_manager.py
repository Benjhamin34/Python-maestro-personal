import json
from camion import Camion, Reparacion

# Nombre del archivo JSON para guardar los datos
INVENTARIO_FILE = 'camiones.json'

def cargar_inventario():
    """Carga los datos de los camiones y sus reparaciones desde el archivo JSON."""
    try:
        with open(INVENTARIO_FILE, 'r') as f:
            data = json.load(f)
            camiones = {}
            for placa, camion_data in data.items():
                # Obtenemos la lista de diccionarios de reparaciones del JSON
                reparaciones_dicts = camion_data.get('reparaciones', [])

                # Corregimos el error: creamos un diccionario temporal con solo los campos
                # que la clase Reparacion espera.
                reparaciones_obj = []
                for rep_dict in reparaciones_dicts:
                    reparaciones_obj.append(Reparacion(
                        descripcion=rep_dict.get('descripcion'),
                        costo=rep_dict.get('costo'),
                        fecha=rep_dict.get('fecha')
                    ))

                camiones[placa] = Camion(
                    marca=camion_data.get('marca'),
                    modelo=camion_data.get('modelo'),
                    anio=camion_data.get('anio'),
                    propietario=camion_data.get('propietario'),
                    chofer=camion_data.get('chofer'),
                    placa=placa,
                    kilometraje=camion_data.get('kilometraje'),
                    reparaciones=reparaciones_obj
                )
            return camiones
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error al cargar el inventario: {e}. Se iniciará con un inventario vacío.")
        return {}

def guardar_inventario(camiones):
    """Guarda el inventario de camiones en el archivo JSON."""
    with open(INVENTARIO_FILE, 'w') as f:
        # Serializamos los objetos Camion a diccionarios para poder guardarlos en JSON
        data_to_save = {placa: camion.to_dict() for placa, camion in camiones.items()}
        json.dump(data_to_save, f, indent=4)
