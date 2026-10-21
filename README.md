# Inventario Escolar

Proyecto académico desarrollado para el módulo **Despliegue de aplicaciones web y móviles** de la Universidad Virtual del Estado de Guanajuato (UVEG).

## Objetivo

Simular el despliegue de una aplicación web de inventario, integrando una interfaz de usuario, un backend, una base de datos relacional y un servidor web local.

El proyecto permite consultar productos y sus existencias almacenados en MySQL.

## Tecnologías utilizadas

- HTML5
- CSS3
- JavaScript
- Python 3
- Flask
- MySQL 8.0
- Nginx 1.30.6
- Git y GitHub
- SSL/TLS para HTTPS

## Estructura del proyecto

- `public/`: archivos públicos de la aplicación.
- `public/index.html`: página principal del inventario.
- `public/css/`: estilos CSS.
- `public/js/`: lógica JavaScript.
- `public/privacidad.html`: aviso de privacidad.
- `public/terminos.html`: términos de uso.
- `app.py`: backend desarrollado con Flask.
- `schema.sql`: estructura de la base de datos MySQL.
- `requirements.txt`: dependencias de Python.
- `nginx.conf`: archivo de configuración de referencia para Nginx.
- `DESPLIEGUE.md`: documentación del despliegue.
- `INSTALL.md`: instrucciones complementarias de instalación.

## Funcionamiento

La aplicación utiliza tres componentes principales:

1. **Frontend:** muestra los productos y sus existencias mediante HTML, CSS y JavaScript.
2. **Backend:** Flask proporciona una API que consulta los registros de MySQL.
3. **Servidor web:** Nginx entrega los archivos estáticos y funciona como proxy inverso hacia Flask.

El frontend consulta el endpoint `/api/productos` para obtener la información en formato JSON.

## Base de datos

Se utiliza la base de datos `inventario_escolar`, que contiene las tablas:

- `productos`
- `movimientos`

La tabla `movimientos` se relaciona con `productos` mediante una clave foránea.

Los productos utilizados durante las pruebas fueron:

| Producto | Existencias |
|---|---:|
| Pan | 3 |
| Leche | 8 |

## Ejecución local

### 1. Preparar MySQL

Instalar MySQL y crear la base de datos ejecutando el archivo `schema.sql`.

### 2. Instalar las dependencias de Python

Desde la carpeta principal del proyecto, ejecutar:

```bat
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configurar la conexión con MySQL

En CMD, definir el usuario y solicitar la contraseña:

```bat
set "DB_USER=root"
set /p "DB_PASSWORD=Contraseña de MySQL: "
```

Estas variables se utilizan para la conexión local. No se deben publicar contraseñas en el repositorio.

### 4. Ejecutar Flask

En la misma terminal:

```bat
python app.py
```

El backend utiliza el puerto `5000`.

### 5. Ejecutar Nginx

Configurar Nginx para utilizar la carpeta `public` como directorio raíz y redirigir `/api/` hacia Flask.

El archivo `nginx.conf` del proyecto sirve como referencia. La configuración activa de Nginx debe ajustarse a las rutas de instalación de cada computadora.

### 6. Configurar el dominio local

Agregar al archivo `hosts` de Windows:

```text
127.0.0.1 inventario.test
```

### 7. Abrir la aplicación

- HTTP: http://inventario.test:8080/
- HTTPS: https://inventario.test:8443/

La dirección HTTPS requiere un certificado local y la configuración correspondiente de Nginx.

El certificado utilizado en esta práctica es autofirmado, por lo que el navegador puede mostrar una advertencia de seguridad.

## API