
def test_listar_tareas(client):
    response = client.get("/tareas")
    
    assert response.status_code == 200

def test_crear_tarea_exitosa(client):
    response = client.post("/tareas", json={ "titulo": "Tarea de prueba" })

    assert response.status_code == 201
