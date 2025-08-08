# app.py
from flask import Flask, jsonify, request
from camion import Camion, Reparacion
from data_manager import cargar_inventario, guardar_inventario

app = Flask(__name__)

# Cargamos el inventario una sola vez al iniciar la app
camiones_del_taller = cargar_inventario()

@app.route('/')
def index():
    return '¡Bienvenido a la API de gestión del taller!'

@app.route('/camiones', methods=['GET'])
def obtener_camiones():
    lista_camiones = [camion.to_dict() for camion in camiones_del_taller.values()]
    return jsonify(lista_camiones)

@app.route('/camiones', methods=['POST'])
def registrar_camion():
    datos_camion = request.get_json()
    if not datos_camion:
        return jsonify({"error": "No se recibieron datos"}), 400

    marca = datos_camion.get('marca')
    modelo = datos_camion.get('modelo')
    anio = datos_camion.get('anio')
    propietario = datos_camion.get('propietario')
    chofer = datos_camion.get('chofer')
    placa = datos_camion.get('placa')
    kilometraje = datos_camion.get('kilometraje')

    if not all([marca, modelo, anio, propietario, chofer, placa, kilometraje]):
        return jsonify({"error": "Faltan datos obligatorios"}), 400

    if placa in camiones_del_taller:
        return jsonify({"error": f"El camión con la placa {placa} ya existe"}), 409

    nuevo_camion = Camion(marca, modelo, anio, propietario, chofer, placa, kilometraje)
    camiones_del_taller[placa] = nuevo_camion
    guardar_inventario(camiones_del_taller)

    return jsonify({"mensaje": f"Camión {placa} registrado exitosamente"}), 201

if __name__ == '__main__':
    app.run(debug=True)