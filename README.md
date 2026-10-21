
# Inventario Escolar

Proyecto académico ficticio desarrollado para el módulo
Despliegue de aplicaciones web y móviles de la Universidad
Virtual del Estado de Guanajuato (UVEG).

## Objetivo

Simular la preparación, optimización, empaquetado,
versionamiento y despliegue de una aplicación web
para la gestión de inventarios.

## Tecnologías utilizadas

- HTML5
- CSS3
- JavaScript
- Python
- Flask (backend ilustrativo)
- MySQL (integración propuesta)
- Git y GitHub
- Nginx (servidor web por configurar)

## Estructura del proyecto

- public/: interfaz web
- public/css/: hojas de estilo
- public/js/: archivos JavaScript
- public/img/: recursos gráficos
- app.py: backend Flask ilustrativo
- schema.sql: estructura de base de datos
- requirements.txt: dependencias de Python
- nginx.conf: configuración de ejemplo

## Ejecución local

1. Abrir CMD en la carpeta public.
2. Ejecutar: python -m http.server 8000
3. Abrir http://localhost:8000

## Optimización

El proyecto incluye archivos CSS y JavaScript
minificados para reducir su tamaño.

## Empaquetado

Se organizó el contenido público de la aplicación
en una carpeta de distribución y se generó un
archivo ZIP utilizando el Explorador de Windows.

El paquete fue extraído y probado en el puerto
8001 mediante un servidor HTTP local de Python.

## Control de versiones

Se utilizará Git para registrar los cambios
del proyecto y GitHub para almacenar el repositorio.

## Alcance académico

La interfaz utiliza datos de ejemplo y no está
conectada al backend Flask.

La integración con MySQL y las pruebas de seguridad
se abordarán durante el Reto 3.

No se requiere un servidor de producción.
