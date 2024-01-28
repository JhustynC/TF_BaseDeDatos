from model.Conectar import Conectar

class PersonaDB:
    consulta = ""
    conectar = Conectar()
    def ingresar(self, indice, cedula, nombre, apellido, telefono, correo):
        self.consulta = self.consulta + "INSERT INTO " # función sql
        """indice: 0 para vendedor, 1 para agente, 2 para comprador"""

        self.atributos = f"(cedula, nombre,apellido,telefono,correo, fecha_ingreso) VALUES('{cedula}','{nombre}','{apellido}','{telefono}','{correo}'"

        def vendedor():
            self.consulta = self.consulta + "vendedor " + self.atributos + ")"
        
        def agente():
            self.consulta = self.consulta + "agente " + self.atributos +  ", CURRENT_DATE)"
        
        def comprador():
            self.consulta = self.consulta + "comprador " + self.atributos + ")"

        
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

        self.atributos = f"SET nombre = '{nombre}', SET apellido = '{apellido}', SET telefono = '{telefono}', SET correo = '{correo}'  WHERE cedula = '{cedula}'"

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

    def listar(self, indice):
        self.consulta = self.consulta + "SELECT * FROM "
        def vendedor():
            self.consulta = self.consulta + "vendedor "
        
        def agente():
            self.consulta = self.consulta + "agente "
        
        def comprador():
            self.consulta = self.consulta + "comprador "
  
        persona = [vendedor,agente,comprador]    
        return persona[indice]
        

    def enviar_consultar(self):
        self.conectar.ingresar_sentencia(self.consulta)
        self.consulta =""

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


