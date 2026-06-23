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

# Ejecutar pruebas unitarias
pytest

## Comandos para Linter y Formatters

Para mantener la calidad y el estilo del código, este proyecto utiliza herramientas de tooling industrial. 
Asegúrate de tener el entorno virtual activado antes de ejecutarlas.

### Formateador de Código (Black)
Black ajusta automáticamente el estilo del código (saltos de línea, espacios, comillas).

# Verificar los cambios que haría Black sin aplicarlos
black --check .

# Formatear todo el código del proyecto automáticamente
black .

# Analizar el código permitiendo hasta 100 caracteres por línea
flake8 --max-line-length=100 .

# Ejecutar Pylint sobre el módulo principal y la aplicación

### Crear tarea (POST)

POST `/tareas/`

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

Comandos de flake8
| Comando                        | Qué hace                            |
|--------------------------------|-------------------------------------|
| `flake8 archivo.py`            | Analiza un archivo                  |
| `flake8 carpeta/`              | Analiza toda una carpeta            |
| `flake8 --max-line-length=100` | Cambia límite de longitud de línea  |
| `flake8 --ignore=E501,W503`    | Ignora ciertos errores/advertencias |


Errores comunes que verás de flake8
| Código | Significado                                | Ejemplo malo                           | Ejemplo bueno            |
|--------|--------------------------------------------|----------------------------------------|--------------------------|
| E501   | Línea muy larga (>79 caracteres)           | `x = "texto muy muy muy muy largo..."` | Dividir en varias líneas |
| W291   | Espacio en blanco al final de línea        | `"hola "`                              | `"hola"`                 |
| E302   | Faltan 2 líneas en blanco antes de función | `def a(): pass`                        | `\n\ndef a(): pass`      |
| F401   | Módulo importado pero no usado             | `import os` (si no se usa)             | Eliminar el import       |
| E225   | Falta espacio alrededor de operador        | `x=5`                                  | `x = 5`                  |


Comandos de Black
| Comando                    | Qué hace                                     |
|----------------------------|----------------------------------------------|
| `black archivo.py`         | Formatea el archivo (LO MODIFICA)            |
| `black carpeta/`           | Formatea toda la carpeta                     |
| `black --check archivo.py` | Solo verifica, NO modifica (útil para CI)    |
| `black --diff archivo.py`  | Muestra los cambios que haría sin aplicarlos |


REGLAS PRINCIPALES DE BLACK (lo que cambia automáticamente):

| Regla                    | Cómo lo dejas tú   | Cómo lo deja Black                            |
|--------------------------|--------------------|-----------------------------------------------|
| Comillas                 | Puedes usar ' o "  | Siempre usa " (dobles)                        |
| Espacios después de coma | `[1,2,3]`          | `[1, 2, 3]`                                   |
| Operadores               | `x=5+3`            | `x = 5 + 3`                                   |
| Longitud de línea        | Lo que sea         | Máximo 88 caracteres (ajusta automáticamente) |
| Funciones vacías         | `def algo(): pass` | `def algo():\n    pass` (con indentación)     |
pylint --rcfile=.pylintrc app/ main.py 



