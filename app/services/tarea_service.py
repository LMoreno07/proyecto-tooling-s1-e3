from app.models.tarea import tareas, CONTADOR_ID

class TareaService:
   
    @staticmethod
    def listar_todas():
        return tareas
   
    @staticmethod
    def crear_tarea(data):
        global CONTADOR_ID
        nueva_tarea = {
            "id": CONTADOR_ID,
            "titulo": data["titulo"].strip(),
            "completada": bool(data.get("completada", False)),
            "descripcion": data.get("descripcion", "").strip() if isinstance(data.get("descripcion", ""), str) else "",
            "prioridad": data.get("prioridad", "media").strip() if isinstance(data.get("prioridad", "media"), str) else "media"
        }
        tareas.append(nueva_tarea)
        CONTADOR_ID += 1
        return nueva_tarea
   
    @staticmethod
    def eliminar_tarea(id_tarea):
        global tareas
        for i, tarea in enumerate(tareas):
            if tarea["id"] == id_tarea:
                del tareas[i]
                return True
        return False