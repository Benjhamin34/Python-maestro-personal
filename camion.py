# Importaciones al principio del archivo
from datetime import datetime
class Camion:
    def __init__(self, marca, modelo, anio, propietario, chofer, placa, kilometraje, reparaciones=None):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.propietario = propietario
        self.chofer = chofer  # Nuevo atributo para el chofer
        self.placa = placa
        self.kilometraje = kilometraje
        self.reparaciones = reparaciones if reparaciones is not None else []

    def mostrar_info(self):
        print(f"Camión: {self.marca} {self.modelo} ({self.anio})")
        print(f"Propietario: {self.propietario}")
        print(f"Chofer: {self.chofer}")  # Mostramos la información del chofer
        print(f"Placa: {self.placa}")
        print(f"Kilometraje: {self.kilometraje} Km")
        if self.reparaciones:
            print("Reparaciones:")
            for i, rep in enumerate(self.reparaciones):
                print(f"  {i+1}. {rep}")
        else:
            print("No tiene reparaciones registradas.")

    def to_dict(self):
        return {
            "marca": self.marca,
            "modelo": self.modelo,
            "anio": self.anio,
            "propietario": self.propietario,
            "chofer": self.chofer,  # Guardamos el chofer en el diccionario
            "placa": self.placa,
            "kilometraje": self.kilometraje,
            "reparaciones": [rep.to_dict() for rep in self.reparaciones]
        }

class Reparacion:
    def __init__(self, descripcion, costo, estado="Pendiente", fecha=None):
        self.descripcion = descripcion
        self.costo = costo
        self.estado = estado
        self.fecha = fecha if fecha else datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "descripcion": self.descripcion,
            "costo": self.costo,
            "estado": self.estado,
            "fecha": self.fecha
        }

    def __repr__(self):
        return f"Reparación: {self.descripcion} - Costo: ${self.costo} - Estado: {self.estado} (Fecha: {self.fecha})"