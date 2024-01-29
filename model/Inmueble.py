from model.Conectar import Conectar 

class InmuebleDB:
    consulta = ""
    conectar = Conectar()

    def enviar_consultar(self):
        self.conectar.ingresar_sentencia(self.consulta)
        self.consulta =""

    def ingresar(self, clave_castral, numero_pisos, agno_construccion, estado, precio_deseado_vendedor, m2_habitables, m2_terreno, id_parroquia, ce_vendedor, id_tipo_inmueble):
        self.consulta = self.consulta + "INSERT INTO inmueble(clave_castral, numero_pisos, agno_construccion, estado, precio_deseado_vendedor, m2_habitables, m2_terreno, fecha_registro, id_parroquia, ce_vendedor, id_tipo) "

        self.consulta = self.consulta + f"VALUES('{clave_castral}', {numero_pisos}, '{agno_construccion}-01-01', '{estado}', '{precio_deseado_vendedor}', '{m2_habitables}', '{m2_terreno}', CURRENT_DATE,'{id_parroquia}', {ce_vendedor}, '{id_tipo_inmueble}')"

    def eliminar(self, c_catastral):
        self.consulta = self.consulta + f"DELETE FROM inmueble WHERE nombre = '{c_catastral}'" 

    def editar(self, c_catastral, precio, parroquia, numero_pisos, agno_construccion):
        self.consulta = self.consulta + f"UPDATE inmueble SET  precio_deseado_vendedor ='{precio}', parroquia = '{parroquia}', numero_pisos = '{numero_pisos}', agno_construccion = '{agno_construccion}' WHERE clave_catrastal = '{c_catastral}'"

    def listar(self, precio_maximo, precio_minimo, ciudad, parroquia, numero_pisos, agnos_construccion, elementos:str, materiales:str):

        primer_filtro = False #* si ya se ocupa un primer filtro se pone en True, sirve para asignar los AND para cada filtro a partir del primero
        self.cosulta = self.consulta + f"SELECT * FROM inmueble AS i"
        unir_parroquia_ciudad = f" JOIN ciudad AS c ON c.id = i.id_ciudad JOIN parroquia AS p ON p.id"
        unir_elemento_material_inmueble = f" JOIN elemento_inmueble_material AS eim ON eim.id_inmueble = i.clave_catastral"
        unir_elemento = f" JOIN elemento AS e ON eim.id_elemento = e.id"
        unir_material = f" JOIN material AS m ON eim.id_material = m.id"
        filtro = " WHERE"
        filtro_precio_minimo = f" precio_deseado_vendedor >= {precio_minimo}"
        filtro_precio_maximo = f" precio_deseado_vendedor <= {precio_maximo}"
        filtro_elementos = f" e.nombre IN {elementos}"
        filtro_materiales = f" m.nombre IN {materiales}"
        filtro_ciudad = f" c.nombre = '{ciudad}'"
        filtro_parroquias = f" p.nombre = '{parroquia}'"
        filtro_numero_pisos = f" i.numero_pisos = '{numero_pisos}'"
        filtro_agnos_contrucion = f" i.agno_construccion <= '{agnos_construccion}'"
        
        #TODO: unen las sentencias según por el campo que se desee filtrar, ten encuenta que todos lo parámetros son cadenas de caracteres
        if(len(elementos)!=0 or len(materiales)!=0):
            self.consulta = self.consulta + unir_elemento_material_inmueble

        if(len(elementos)!=0):
            self.consulta = self.consulta + unir_elemento

        if(len(materiales)!=0):
            self.consulta = self.consulta + unir_material

        if(len(ciudad)!=0 or len(parroquia)!=0):
            self.consulta = self.consulta + unir_parroquia_ciudad

        #TODO: Se unos los filtros o sentencias que son parte  del WHERE
        #* Se unos los filtros o sentencias que son parte  del WHERE
        if(len(precio_maximo)!=0 or len(precio_minimo)!=0 or len(parroquia)!=0 or len(ciudad)!=0 or len(numero_pisos)!=0 or len(agnos_construccion)!=0):
            self.consulta = self.consulta + filtro    

        if(len(precio_maximo)!=0):
            self.consulta = self.consulta + filtro_precio_maximo
            primer_filtro = True

        if(len(precio_minimo)!=0):
            if(not primer_filtro):
                primer_filtro = True
            else:
                self.consulta = self.consulta + "AND"
            
            self.consulta + filtro_precio_minimo
        
        if(len(ciudad)!=0):
            if(not primer_filtro):
                primer_filtro = True
            else:
                self.consulta = self.consulta + "AND"

            self.consulta + filtro_ciudad

        if(len(parroquia)!=0):
            if(not primer_filtro):
                primer_filtro = True
            else:
                self.consulta = self.consulta + "AND" 

            self.consulta + filtro_parroquias

        if(len(numero_pisos)!=0):
            if(not primer_filtro):
                primer_filtro = True
            else:
                self.consulta = self.consulta + "AND"
            self.consulta = self.consulta + filtro_numero_pisos
            
        if(len(agnos_construccion)!=0):
            if(not primer_filtro):
                primer_filtro = True
            else:
                self.consulta = self.consulta + "AND" 

            self.consulta = self.consulta + filtro_agnos_contrucion

        if(len(elementos)!=0):
            if(not primer_filtro):
                primer_filtro = True
            else:
                self.consulta = self.consulta + "AND" 

            self.consulta = self.consulta + filtro_elementos

        if(len(materiales)!=0):
            if(not primer_filtro):
                primer_filtro = True
            else:
                self.consulta = self.consulta + "AND" 

            self.consulta = self.consulta + filtro_materiales
        