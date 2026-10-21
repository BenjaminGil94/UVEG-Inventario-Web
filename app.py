"""Backend ilustrativo. Requiere instalar dependencias y configurar MySQL."""
import os
from flask import Flask, jsonify
import mysql.connector
app = Flask(__name__)
@app.get('/api/health')
def health():
    return jsonify(status='ok')
@app.get('/api/productos')
def productos():
    conexion=mysql.connector.connect(host=os.getenv('DB_HOST','localhost'),user=os.environ['DB_USER'],password=os.environ['DB_PASSWORD'],database='inventario_escolar')
    try:
        cursor=conexion.cursor(dictionary=True)
        cursor.execute('SELECT id,nombre,existencias FROM productos ORDER BY id')
        return jsonify(cursor.fetchall())
    finally:
        conexion.close()
if __name__=='__main__':app.run(debug=False)
