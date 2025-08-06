class Camion:
    def __init__(self, marca, modelo, anio, propietario, placa, kilometraje):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.propietario = propietario
        self.placa = placa
        self.kilometraje = kilometraje

    def mostrar_info(self):
        print(f"Camión: {self.marca} {self.modelo} ({self.anio})")
        print(f"Propietario: {self.propietario}")
        print(f"Placa: {self.placa}")
        print(f"Kilometraje: {self.kilometraje} Km")

    def to_dict(self):
        return {
            "marca": self.marca,
            "modelo": self.modelo,
            "anio": self.anio,
            "propietario": self.propietario,
            "placa": self.placa,
            "kilometraje": self.kilometraje
        }