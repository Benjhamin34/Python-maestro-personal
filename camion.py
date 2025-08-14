from datetime import datetime

class Reparacion:
    """Clase para representar una reparación de un camión."""
    def __init__(self, descripcion, costo, fecha=None):
        self.descripcion = descripcion
        self.costo = costo
        self.fecha = fecha if fecha else datetime.now().isoformat()
    
    def to_dict(self):
        """Convierte el objeto Reparacion a un diccionario para su serialización."""
        return {
            'descripcion': self.descripcion,
            'costo': self.costo,
            'fecha': self.fecha
        }

class Camion:
    """Clase para representar un camión del taller."""
    def __init__(self, marca, modelo, anio, propietario, chofer, placa, kilometraje, reparaciones=None):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.propietario = propietario
        self.chofer = chofer
        self.placa = placa
        self.kilometraje = kilometraje
        # Solución: Se asigna la lista de objetos Reparacion directamente, sin volver a convertirlos.
        self.reparaciones = reparaciones if reparaciones is not None else []

    def to_dict(self):
        """Convierte el objeto Camion a un diccionario para su serialización."""
        return {
            'marca': self.marca,
            'modelo': self.modelo,
            'anio': self.anio,
            'propietario': self.propietario,
            'chofer': self.chofer,
            'placa': self.placa,
            'kilometraje': self.kilometraje,
            'reparaciones': [rep.to_dict() for rep in self.reparaciones]
        }
