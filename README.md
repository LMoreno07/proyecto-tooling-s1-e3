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
pylint --rcfile=.pylintrc app/ main.py 



