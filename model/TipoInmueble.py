from Conectar import Conectar

class TipoInmueble:
    consulta = ""
    conectar = Conectar()
    def ingresar(self, nombre):
        self.consulta = self.consulta + f"INSERT INTO tipo_inmueble(nombre) VALUES('{nombre}')" 
       
    def eliminar(self, id):
        self.consulta = self.consulta + f"DELETE FROM tipo_inmueble WHERE nombre = '{id}'" 

    def editar(self, id, nombre):
        self.consulta = self.consulta + f"UPDATE tipo_inmueble SET nombre ='{nombre}' WHERE id = '{id}'" # SQL actual

    def listar(self):
        self.cosulta = self.consulta + f"SELECT * FROM tipo_inmueble"

    def enviar_consultar(self):
        self.conectar.ingresar_sentencia(self.consulta)
        self.consulta =""