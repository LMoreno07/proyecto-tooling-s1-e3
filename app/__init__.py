from flask import Flask
from app.controllers.tareas import tarea_bp


def create_app():
    app = Flask(__name__)

    # Ruta raíz 'http://127.0.0.1:5000'
    @app.route("/")
    def index():
        return {
            "mensaje": "Bienvenido a nuestra API. Ve a /tareas/ para ver los endpoints."
        }, 200

    # Registrar blueprints (rutas)
    app.register_blueprint(tarea_bp)

    return app
