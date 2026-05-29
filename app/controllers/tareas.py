from flask import Blueprint, request, jsonify
from app.services.tarea_service import TareaService

tarea_bp = Blueprint("tareas", __name__, url_prefix="/tareas")


# Ruta http://127.0.0.1:5000/tareas
@tarea_bp.route("/", methods=["GET"])  # GET /tareas/
def listar_tareas():
    tareas = TareaService.listar_todas()
    return jsonify(tareas), 200


@tarea_bp.route("/", methods=["POST"])  # POST /tareas/
def crear_tarea():
    data = request.get_json()

    # Validación simple
    if not data or "titulo" not in data:
        return jsonify({"error": "El campo 'titulo' es requerido"}), 400

    if not isinstance(data["titulo"], str) or len(data["titulo"].strip()) == 0:
        return jsonify({"error": "El 'titulo' debe ser un texto no vacío"
                        }), 400

    nueva_tarea = TareaService.crear_tarea(data["titulo"].strip())
    return jsonify(nueva_tarea), 201


@tarea_bp.route("/<int:tarea_id>", methods=["DELETE"])  # DELETE /tareas/1
def eliminar_tarea(tarea_id):
    if TareaService.eliminar_tarea(tarea_id):
        return jsonify({"mensaje": f"Tarea {tarea_id} eliminada"}), 200
    return jsonify({"error": f"Tarea {tarea_id} no encontrada"}), 404
