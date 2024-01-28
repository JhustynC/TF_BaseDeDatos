from Conectar import Conectar

class Material:
    consulta = ""
    conectar = Conectar()
    def ingresar(self, nombre):
        self.consulta = self.consulta + f"INSERT INTO material(nombre) VALUES('{nombre}')" 
       
    def eliminar(self, id):
        self.consulta = self.consulta + f"DELETE FROM material WHERE nombre = '{id}'" 

    def editar(self, id, nombre):
        self.consulta = self.consulta + f"UPDATE material SET nombre ='{nombre}' WHERE id = '{id}'" # SQL actual

    def listar(self):
        self.cosulta = self.consulta + f"SELECT * FROM material"

    def enviar_consultar(self):
        self.conectar.ingresar_sentencia(self.consulta)
        self.consulta =""
