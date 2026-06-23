import app.models.tarea as db


class TareaService:

    @staticmethod
    def listar_todas():
        return db.tareas

    @staticmethod
    def crear_tarea(titulo):
        nueva_tarea = {"id": db.CONTADOR_ID, "titulo": titulo, "completada": False}
        db.tareas.append(nueva_tarea)
        db.CONTADOR_ID += 1
        return nueva_tarea

    @staticmethod
    def eliminar_tarea(id_tarea):
        for i, tarea in enumerate(db.tareas):
            if tarea["id"] == id_tarea:
                del db.tareas[i]
                return True
        return False
