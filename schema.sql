CREATE DATABASE IF NOT EXISTS inventario_escolar CHARACTER SET utf8mb4;
USE inventario_escolar;
CREATE TABLE IF NOT EXISTS productos (id INT AUTO_INCREMENT PRIMARY KEY,nombre VARCHAR(120) NOT NULL,existencias INT NOT NULL DEFAULT 0,creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP, INDEX idx_producto_nombre(nombre));
CREATE TABLE IF NOT EXISTS movimientos (id INT AUTO_INCREMENT PRIMARY KEY,producto_id INT NOT NULL,cambio INT NOT NULL,fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP, INDEX idx_mov_producto(producto_id),FOREIGN KEY(producto_id) REFERENCES productos(id));
INSERT INTO productos(nombre,existencias) VALUES ('Pan',3),('Leche',8);
