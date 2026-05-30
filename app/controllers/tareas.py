from flask import Blueprint, request, jsonify
from app.services.tarea_service import TareaService

tarea_bp = Blueprint("tareas", __name__, url_prefix="/tareas")


# Ruta http://127.0.0.1:5000/tareas
@tarea_bp.route("/", methods=["GET"])  # GET /tareas/
def listar_tareas():
    tareas = TareaService.listar_todas()
    return jsonify(tareas), 200


@tarea_bp.route("/ejemplo", methods=["GET"])  # GET /tareas/ejemplo
def ejemplo_tarea():
    ejemplo = {
        "titulo": "Mi tarea nueva",
    }
    return jsonify(ejemplo), 200


@tarea_bp.route("/", methods=["POST"])  # POST /tareas/
def crear_tarea():
    ejemplo_json = {
        "titulo": "Mi tarea nueva",
    }

    if not request.is_json:
        return jsonify({
            "error": "El body debe ser JSON.",
            "ejemplo": ejemplo_json
        }), 400

    data = request.get_json(silent=True)
    if not data:
        return jsonify({
            "error": "No se recibió JSON válido.",
            "ejemplo": ejemplo_json
        }), 400

    # Validación simple
    if "titulo" not in data:
        return jsonify({"error": "El campo 'titulo' es requerido", "ejemplo": ejemplo_json}), 400

    if not isinstance(data["titulo"], str) or len(data["titulo"].strip()) == 0:
        return jsonify({"error": "El 'titulo' debe ser un texto no vacío", "ejemplo": ejemplo_json}), 400

    nueva_tarea = TareaService.crear_tarea(data)
    return jsonify(nueva_tarea), 201


@tarea_bp.route("/<int:tarea_id>", methods=["DELETE"])  # DELETE /tareas/1
def eliminar_tarea(tarea_id):
    if TareaService.eliminar_tarea(tarea_id):
        return jsonify({"mensaje": f"Tarea {tarea_id} eliminada"}), 200
    return jsonify({"error": f"Tarea {tarea_id} no encontrada"}), 404
