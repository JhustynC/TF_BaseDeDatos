DROP TABLE IF EXISTS transaccion CASCADE;
DROP TABLE IF EXISTS agente CASCADE;
DROP TABLE IF EXISTS vendedor CASCADE;
DROP TABLE IF EXISTS comprador CASCADE;
DROP TABLE IF EXISTS elemento_inmueble_material CASCADE;
DROP TABLE IF EXISTS tipo_inmueble CASCADE;
DROP TABLE IF EXISTS inmueble CASCADE;
DROP TABLE IF EXISTS elemento CASCADE;
DROP TABLE IF EXISTS material CASCADE;
DROP TABLE IF EXISTS calificacion CASCADE;
DROP TABLE IF EXISTS provincia CASCADE;
DROP TABLE IF EXISTS ciudad CASCADE;
DROP TABLE IF EXISTS parroquia CASCADE;


CREATE TABLE ciudad(
    id VARCHAR(2) PRIMARY KEY,
    nombre TEXT NOT NULL
);

CREATE TABLE parroquia(
    id VARCHAR(3) PRIMARY KEY,
    nombre TEXT NOT NULL,
    id_ciudad VARCHAR(2) NOT NULL,
    FOREIGN KEY (id_ciudad) REFERENCES ciudad(id)
);

CREATE TABLE agente (
    cedula VARCHAR(10) PRIMARY KEY, 
    nombre TEXT NOT NULL, 
    apellido TEXT NOT NULL, 
    telefono VARCHAR(10), 
    correo TEXT NOT NULL, 
    fecha_ingreso DATE NOT NULL
);

CREATE TABLE comprador (
    cedula VARCHAR(10) PRIMARY KEY, 
    nombre TEXT NOT NULL, 
    apellido TEXT NOT NULL, 
    telefono VARCHAR(10), 
    correo TEXT NOT NULL,
    fecha_ingreso DATE NOT NULL
);
   
CREATE TABLE vendedor (
    cedula VARCHAR(10) PRIMARY KEY, 
    nombre TEXT NOT NULL, 
    apellido TEXT NOT NULL, 
    telefono VARCHAR(10), 
    correo TEXT NOT NULL,
    fecha_ingreso DATE NOT NULL
);
   
CREATE TABLE tipo_inmueble (
    id VARCHAR(2) PRIMARY KEY, 
    nombre TEXT NOT NULL
);
   
CREATE TABLE material (
    id VARCHAR(3) PRIMARY KEY, 
    nombre TEXT NOT NULL
);
   
CREATE TABLE inmueble (
    clave_castral VARCHAR(10) PRIMARY KEY, 
    numero_pisos INTEGER NOT NULL, 
    agno_construccion DATE NOT NULL, 
    estado VARCHAR(8) NOT NULL, 
    precio_deseado_vendedor FLOAT NOT NULL, 
    fecha_registro DATE NOT NULL, 
    fecha_venta DATE, 
    m2_habitables FLOAT NOT NULL, 
    m2_terreno FLOAT NOT NULL, 
    ce_vendedor VARCHAR(10) NOT NULL,
    id_tipo VARCHAR(2) NOT NULL,
    id_parroquia VARCHAR(3) NOT NULL, 
    FOREIGN KEY (ce_vendedor) REFERENCES vendedor(cedula), 
    FOREIGN KEY (id_parroquia) REFERENCES parroquia(id),
    FOREIGN KEY (id_tipo) REFERENCES tipo_inmueble(id)
);
   
CREATE TABLE elemento (
    id VARCHAR(3) PRIMARY KEY, 
    nombre TEXT NOT NULL 
);
   
CREATE TABLE elemento_inmueble_material (
    id_inmueble VARCHAR(10) NOT NULL, 
    id_elemento VARCHAR(3) NOT NULL, 
    id_material VARCHAR(3) NOT NULL,
    UNIQUE(id_inmueble, id_elemento),
    FOREIGN KEY (id_inmueble) REFERENCES inmueble(clave_castral), 
    FOREIGN KEY (id_elemento) REFERENCES elemento(id)
);

CREATE TABLE calificacion(
    id INTEGER PRIMARY KEY,
    nombre VARCHAR(10) NOT NULL
);
   
CREATE TABLE transaccion (
    id SERIAL PRIMARY KEY,
    precio_deseado_vendedor FLOAT, 
    precio_venta FLOAT, 
    fecha_inicio DATE NOT NULL, 
    fecha_final DATE, 
    estado BOOLEAN NOT NULL, 
    comision FLOAT,
    ce_agente VARCHAR(10) NOT NULL,
    ce_comprador VARCHAR(10) ,
    id_calificacion INTEGER,
    comentario_comprador TEXT,
    id_inmueble VARCHAR(10) NOT NULL,
    comentario_duegno_inmueble TEXT,
    FOREIGN KEY (ce_agente) REFERENCES agente(cedula),
    FOREIGN KEY (ce_comprador) REFERENCES comprador(cedula),
    FOREIGN KEY (id_calificacion) REFERENCES calificacion(id), 
    FOREIGN KEY (id_inmueble) REFERENCES inmueble(clave_castral)
);
