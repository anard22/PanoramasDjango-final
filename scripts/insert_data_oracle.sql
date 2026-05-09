-- =========================================
-- Script de datos de prueba (Oracle)
-- Proyecto: Panoramas Web
-- =========================================

INSERT INTO USUARIO (username, password, email)
VALUES ('admin', 'admin123', 'admin@test.cl');

INSERT INTO PERFIL (rut, telefono, direccion, usuario_id)
VALUES ('11.111.111-1', '987654321', 'Av. Principal 123', 1);

INSERT INTO CATEGORIA (nombre)
VALUES ('Eventos culturales');

INSERT INTO CATEGORIA (nombre)
VALUES ('Panoramas familiares');

INSERT INTO PANORAMA (titulo, descripcion, fecha, lugar, creador_id, categoria_id)
VALUES (
    'Feria Cultural',
    'Evento cultural en la plaza central',
    TO_DATE('2026-05-10', 'YYYY-MM-DD'),
    'Plaza Central',
    1,
    1
);