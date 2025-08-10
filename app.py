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

# RUTA PARA OBTENER TODOS LOS CAMIONES
@app.route('/camiones', methods=['GET'])
def obtener_camiones():
    lista_camiones = [camion.to_dict() for camion in camiones_del_taller.values()]
    return jsonify(lista_camiones)

# RUTA PARA REGISTRAR UN NUEVO CAMIÓN
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

# --- NUEVAS RUTAS AÑADIDAS HOY ---

# RUTA PARA OBTENER UN SOLO CAMIÓN POR PLACA
@app.route('/camiones/<string:placa>', methods=['GET'])
def obtener_camion_por_placa(placa):
    camion = camiones_del_taller.get(placa)
    if camion:
        return jsonify(camion.to_dict())
    return jsonify({"error": f"No se encontró un camión con la placa {placa}"}), 404

# RUTA PARA ELIMINAR UN CAMIÓN
@app.route('/camiones/<string:placa>', methods=['DELETE'])
def eliminar_camion(placa):
    if placa not in camiones_del_taller:
        return jsonify({"error": f"No se encontró un camión con la placa {placa}"}), 404

    del camiones_del_taller[placa]
    guardar_inventario(camiones_del_taller)

    return jsonify({"mensaje": f"Camión con placa {placa} eliminado exitosamente"}), 200

# RUTA PARA ACTUALIZAR UN CAMIÓN
@app.route('/camiones/<string:placa>', methods=['PUT'])
def actualizar_camion(placa):
    datos_actualizados = request.get_json()
    if not datos_actualizados:
        return jsonify({"error": "No se recibieron datos para actualizar"}), 400
    
    if placa not in camiones_del_taller:
        return jsonify({"error": f"No se encontró un camión con la placa {placa}"}), 404

    camion = camiones_del_taller[placa]
    
    # Actualizamos solo los datos que se reciban en el JSON
    camion.marca = datos_actualizados.get('marca', camion.marca)
    camion.modelo = datos_actualizados.get('modelo', camion.modelo)
    camion.anio = datos_actualizados.get('anio', camion.anio)
    camion.propietario = datos_actualizados.get('propietario', camion.propietario)
    camion.chofer = datos_actualizados.get('chofer', camion.chofer)
    camion.kilometraje = datos_actualizados.get('kilometraje', camion.kilometraje)
    
    guardar_inventario(camiones_del_taller)

    return jsonify({"mensaje": f"Camión con placa {placa} actualizado exitosamente"}), 200


if __name__ == '__main__':
    app.run(debug=True)
