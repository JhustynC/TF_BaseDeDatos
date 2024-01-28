from model.Conectar import Conectar

class PersonaDB:
    consulta = ""
    conectar = Conectar()
    def ingresar(self, indice, cedula, nombre, apellido, telefono, correo):
        self.consulta = self.consulta + "INSERT INTO " # función sql
        """indice: 0 para vendedor, 1 para agente, 2 para comprador"""

        
        self.atributos = f"(cedula, nombre,apellido,telefono,correo, fecha_ingreso) VALUES('{cedula}','{nombre}','{apellido}','{telefono}','{correo}', CURRENT_DATE)"

        def vendedor():
            self.consulta = self.consulta + "vendedor " + self.atributos
        
        def agente():
            self.consulta = self.consulta + "agente " + self.atributos
        
        def comprador():
            self.consulta = self.consulta + "comprador " + self.atributos

        
        persona = [vendedor,agente,comprador]    
        return persona[indice]
    
    def eliminar(self, indice, cedula):
        self.consulta = self.consulta + "DELETE FROM " # SQL BORRAR 
        self.atributos = f"WHERE cedula = '{cedula}'"
        def vendedor():
            self.consulta += "vendedor "
            self.consulta = self.consulta + self.atributos   

        def agente():
            self.consulta += "agente "
            self.consulta = self.consulta + self.atributos   

        def comprador():
            self.consulta += "comprador "
            self.consulta = self.consulta + self.atributos   
              
        persona = [vendedor,agente,comprador]    
        return persona[indice]

    def editar(self, indice, cedula, nombre, apellido, telefono, correo):
        self.consulta = self.consulta + "UPDATE " # SQL actual

        self.atributos = f"SET nombre = '{nombre}',apellido = '{apellido}',telefono = '{telefono}',correo = '{correo}'  WHERE cedula = '{cedula}'"

        def vendedor():
            self.consulta = self.consulta + "vendedor "
            self.consulta = self.consulta + self.atributos   
        
        def agente():
            self.consulta = self.consulta + "agente "
            self.consulta = self.consulta + self.atributos   
        
        def comprador():
            self.consulta = self.consulta + "comprador "
            self.consulta = self.consulta + self.atributos   
  
        persona = [vendedor,agente,comprador]    
        return persona[indice]

    def listar(self, indice, cedula, nombre):
        #FROM agente WHERE cedula LIKE '%16%' AND nombre LIKE '%%';
        self.consulta = self.consulta + "SELECT * FROM "
        self.condiciones = f"WHERE cedula LIKE '%{cedula}%' AND nombre LIKE '%{nombre}%'"
        def vendedor():
            self.consulta = self.consulta + "vendedor " + self.condiciones
        
        def agente():
            self.consulta = self.consulta + "agente "  + self.condiciones
        
        def comprador():
            self.consulta = self.consulta + "comprador "  + self.condiciones
  
        persona = [vendedor,agente,comprador]    
        return persona[indice]
        

    def enviar_consultar(self):
        self.conectar.ingresar_sentencia(self.consulta)
        self.consulta =""

    def cerrar_conexion(self):
        if self.conectar.connection != None:
            self.conectar.cursor.close()
            self.conectar.connection.close()


#conectar2 = Conectar()


#persona = PersonaDB()
#persona.listar(0)()
#persona.ingresar(1,"0000001","jhustyn", "", "000", "j.@")()

#persona.enviar_consultar()

#persona.listar(1)()
#persona = PersonaDB()
#persona.eliminar(1, "0000001")()
#print(persona.consulta)

#persona.enviar_consultar()
#print("valores:", persona.conectar.resultado)
#for fila in persona.conectar.resultado:
#    print(fila)


