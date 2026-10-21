# Documentación del despliegue web

## Proyecto
Inventario Escolar - UVEG

## 1. Preparación de la aplicación

Se organizó el proyecto en carpetas para separar los archivos HTML, CSS y JavaScript.

La aplicación permite consultar productos y sus existencias mediante una interfaz web.

## 2. Optimización

Se utilizaron los archivos `estilo.min.css` y `app.min.js` para la presentación y el funcionamiento de la interfaz.

## 3. Empaquetado

Durante el Reto 2 se creó un paquete ZIP mediante el Explorador de archivos de Windows.

El paquete se extrajo en una carpeta independiente para verificar su funcionamiento.

## 4. Pruebas locales iniciales

Se utilizó Python para ejecutar un servidor HTTP de pruebas.

- Primera prueba: http://localhost:8000
- Segunda prueba: http://localhost:8001

La interfaz se mostró correctamente en ambas pruebas.

## 5. Base de datos MySQL

Durante el Reto 3 se instaló y configuró MySQL 8.0.

Se creó la base de datos `inventario_escolar`, con las siguientes tablas:

- `productos`: almacena el identificador, nombre y existencias de cada producto.
- `movimientos`: permite registrar cambios de existencias y mantiene una relación mediante una clave foránea con la tabla `productos`.

Se registraron dos productos de prueba:

| Producto | Existencias |
|---|---:|
| Pan | 3 |
| Leche | 8 |

La estructura de la base de datos se documentó en el archivo `schema.sql`.

## 6. Backend con Flask

Se implementó un backend utilizando Python y Flask.

Las dependencias principales se encuentran en `requirements.txt`:

- Flask
- mysql-connector-python

El backend dispone de dos rutas:

- `/api/health`: comprueba que el servicio Flask responde.
- `/api/productos`: consulta los productos almacenados en MySQL y devuelve la información en formato JSON.

La conexión a la base de datos utiliza variables de entorno para el usuario y la contraseña.

## 7. Configuración de Nginx

Se configuró Nginx 1.30.6 para servir los archivos de la aplicación y redirigir las solicitudes de la API hacia Flask.

Se utilizó el puerto `8080` para HTTP y el puerto `8443` para HTTPS.

El servidor entrega los archivos estáticos desde la carpeta `public` y utiliza un proxy inverso para las solicitudes que comienzan con `/api/`.

## 8. Dominio local

Se configuró el archivo `hosts` de Windows para asociar el dominio `inventario.test` con la dirección local `127.0.0.1`.

La aplicación puede consultarse mediante:

- HTTP: http://inventario.test:8080/
- HTTPS: https://inventario.test:8443/

Este dominio funciona únicamente en el entorno local configurado.

## 9. Configuración HTTPS

Se generó un certificado SSL/TLS autofirmado para `inventario.test`.

Se configuró Nginx para utilizar el certificado y su clave privada mediante el puerto `8443`, habilitando TLS 1.2 y TLS 1.3.

Se comprobó la respuesta del servidor mediante `curl.exe -k`, obteniendo `HTTP/1.1 200 OK`.

También se verificó que la ruta `/api/productos` devuelve los registros de MySQL a través de HTTPS.

El navegador muestra una advertencia de seguridad porque el certificado es autofirmado y no está validado por una autoridad de certificación confiable. Esta configuración se utiliza exclusivamente para pruebas académicas locales.

## 10. Encabezados de seguridad

Se configuraron los siguientes encabezados en Nginx:

**Content-Security-Policy (CSP)**

Restringe la carga de recursos a los orígenes permitidos y limita la ejecución de contenido no autorizado.

**Strict-Transport-Security (HSTS)**

Se configuró el encabezado `Strict-Transport-Security` con `max-age=300`.

Se verificó mediante `curl.exe` que ambos encabezados están presentes en las respuestas HTTPS.

Debido al certificado autofirmado, no se garantiza que los navegadores apliquen la política HSTS.

## 11. Pruebas de compatibilidad y rendimiento

Se verificó el funcionamiento de la aplicación en Google Chrome y Microsoft Edge.

También se ejecutó Lighthouse, obteniendo los siguientes resultados en la prueba realizada:

| Indicador | Puntuación |
|---|---:|
| Rendimiento | 100 |
| Accesibilidad | 100 |
| Buenas prácticas | 100 |
| SEO | 90 |

Estas puntuaciones corresponden al entorno y a las condiciones de la prueba local.

## 12. Aviso de privacidad y términos

Se incorporaron las páginas:

- `privacidad.html`
- `terminos.html`

Ambas páginas fueron verificadas mediante HTTPS.

Su contenido explica el carácter académico de la aplicación y las limitaciones de su uso.

## 13. Versionamiento

Se utiliza Git para registrar los cambios del proyecto.

Repositorio remoto:

https://github.com/BenjaminGil94/UVEG-Inventario-Web

Los cambios del Reto 3 deberán incorporarse mediante un nuevo commit y enviarse al repositorio remoto.

Los archivos que contienen contraseñas, claves privadas y dependencias locales no deben incluirse en el repositorio.

## 14. Alcance y limitaciones

El proyecto corresponde a una simulación académica de despliegue web.

La aplicación se ejecuta en una computadora local y requiere que MySQL, Flask y Nginx estén disponibles y configurados.

No se ha implementado un servidor público ni un certificado emitido por una autoridad de certificación.

El objetivo es demostrar la integración de una interfaz web, un backend, una base de datos y un servidor web, así como la realización de pruebas básicas de compatibilidad, rendimiento y seguridad.