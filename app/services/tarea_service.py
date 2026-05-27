from app.models.tarea import tareas, CONTADOR_ID

class TareaService:
   
    @staticmethod
    def listar_todas():
        return tareas
   
    @staticmethod
    def crear_tarea(titulo):
        global CONTADOR_ID
        nueva_tarea = {
            "id": CONTADOR_ID,
            "titulo": titulo,
            "completada": False
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