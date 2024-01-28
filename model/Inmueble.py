from model.Conectar import Conectar 

class InmuebleDB:
    consulta = ""
    conectar = Conectar()
    def ingresar(self, clave_castral, numero_pisos, agno_construccion, estado, precio_deseado_vendedor, m2_habitables, m2_terreno, id_parroquia):
        self.consulta = self.consulta + "INSERT INTO inmueble(clave_castral, numero_pisos, agno_construccion, estado, precio_deseado_vendedor, m2_habitables, m2_terreno, fecha_registro, id_parroquia) "

        self.consulta = self.consulta + f"VALUES('{clave_castral}', '{numero_pisos}', '{agno_construccion}', '{estado}', '{precio_deseado_vendedor}', '{m2_habitables}', '{m2_terreno}', DATE_CURRENT,'{id_parroquia}')"

    def eliminar(self, id):
        self.consulta = self.consulta + f"DELETE FROM inmueble WHERE nombre = '{id}'" 

    def editar(self, c_catastral, precio, ciudad, parroquia, numero_pisos, agnos_construccion):
        self.consulta = self.consulta + f"UPDATE inmueble SET  ='{precio}' WHERE clave_catrastal = '{c_catastral}'"

    def listar(self, precio_maximo, precio_minimo, ciudad, parroquia, numero_pisos, agnos_construccion, elemento, material):
        self.cosulta = self.consulta + f"SELECT * FROM elemento"
        #self.
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