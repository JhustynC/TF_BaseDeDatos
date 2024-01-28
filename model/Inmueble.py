from model.Conectar import Conectar 

class InmuebleDB:
    consulta = ""
    conectar = Conectar()
    def ingresar(self, clave_castral, numero_pisos, agno_construccion, estado, precio_deseado_vendedor, fecha_registro, m2_habitables, m2_terreno, ce_vendedor):
        self.consulta = self.consulta + "INSERT INTO inmueble(clave_castral, numero_pisos, agno_construccion, estado, precio_deseado_vendedor, m2_habitables, m2_terreno, ce_vendedor, fecha_registro) "

        self.consulta = self.consulta + f"VALUES('{clave_castral}', '{numero_pisos}', '{agno_construccion}', '{estado}', '{precio_deseado_vendedor}', '{m2_habitables}', '{m2_terreno}', '{ce_vendedor}', DATE_CURRENT)"

    def eliminar(self, id):
        self.consulta = self.consulta + f"DELETE FROM elemento WHERE nombre = '{id}'" 

    def editar(self, id, nombre):
        self.consulta = self.consulta + f"UPDATE elemento SET nombre ='{nombre}' WHERE id = '{id}'" # SQL actual

    def listar(self):
        self.cosulta = self.consulta + f"SELECT * FROM elemento"
        pass

    """CREATE TABLE inmueble (
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
    FOREIGN KEY (id_vendedor) REFERENCES vendedor(cedula), 
    FOREIGN KEY (id_tipo) REFERENCES tipo_inmueble(id),
);"""