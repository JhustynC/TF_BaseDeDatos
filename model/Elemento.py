from Conectar import Conectar

class Elemento:
    consulta = ""
    conectar = Conectar()
    def ingresar(self, nombre):
        self.consulta = self.consulta + f"INSERT INTO elemento(nombre) VALUES('{nombre}')" 
       
    def eliminar(self, id):
        self.consulta = self.consulta + f"DELETE FROM elemento WHERE nombre = '{id}'" 

    def editar(self, id, nombre):
        self.consulta = self.consulta + f"UPDATE elemento SET nombre ='{nombre}' WHERE id = '{id}'" # SQL actual

    def listar(self):
        self.cosulta = self.consulta + f"SELECT * FROM elemento"

    def enviar_consultar(self):
        self.conectar.ingresar_sentencia(self.consulta)
        self.consulta =""
