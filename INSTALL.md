# Instalación académica (no ejecutada)
1. Instalar Python 3, MySQL y Nginx.
2. Crear entorno virtual: `python -m venv .venv`.
3. Activar entorno e instalar: `pip install -r requirements.txt`.
4. Ejecutar `schema.sql` en MySQL.
5. Definir variables de entorno `DB_USER`, `DB_PASSWORD`, opcionalmente `DB_HOST`.
6. Ejecutar `python app.py` y visitar `http://127.0.0.1:5000/api/health`.
7. Ajustar ruta `root` de nginx.conf y habilitar el sitio en Nginx.
8. Probar la interfaz en Chrome y Edge; ejecutar Lighthouse y guardar resultados.
Las versiones de requirements.txt son intervalos compatibles, no versiones instaladas comprobadas.
