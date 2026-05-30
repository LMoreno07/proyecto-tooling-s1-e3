# API de Tareas - Proyecto Tooling

## Integrantes
- Moreno, luis
- Torrealba, Yolbert
- Tovar, Isaías

## Instalación y ejecución

```bash
# Clonar repositorio
git clone https://github.com/LMoreno07/proyecto-tooling-s1-e3.git
cd proyecto_api

# Crear entorno virtual
python -m venv venv

# Activar entorno
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar servidor
python main.py

## Uso de la API

### Tareas precargadas
Al iniciar la aplicación, ya hay una tarea en memoria:

```json
{
  "titulo": "Tarea de ejemplo",
}
```

### Crear tarea (POST)

POST `/tareas/`

Headers:
- `Content-Type: application/json`

Body:

```json
{
  "titulo": "Mi tarea nueva",
}
```

Campos admitidos:
- `titulo` (obligatorio)

Respuesta exitosa:

```json
{
  "titulo": "Mi tarea nueva",
}
```

Errores posibles:
- 400 Bad Request: cuando falta `titulo` o el campo está vacío.

### Ejemplo de payload disponible desde la API

GET `/tareas/ejemplo`

Devuelve un ejemplo del cuerpo JSON que debes enviar en el POST:

```json
{
  "titulo": "Mi tarea nueva",
}
```
