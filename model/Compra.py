from model.Conectar import Conectar

class CompraDB():
    consulta = ""
    conectar = Conectar()
    
    def filtro_compra(self, num_pisos='', tiempo_construccion='', metros_terreno='', ciudad='', parroquia='', precio_min='',precio_max='', tipo_imb=''):
        
        consulta = "SELECT t.id_inmueble\nFROM transaccion t\nJOIN inmueble i ON t.id_inmueble = i.clave_castral"
        
        if ciudad or parroquia or tiempo_construccion:
            consulta += '\nJOIN parroquia p ON i.id_parroquia = p.id\nJOIN ciudad c ON p.id_ciudad = c.id'
        
        if tipo_imb:
            consulta += '\nJOIN tipo_inmueble ti on i.id_tipo = ti.id'
        
        filtros = ''
        
        if num_pisos or tiempo_construccion or metros_terreno or ciudad or parroquia or precio_min or precio_max or tipo_imb: 
            filtros += '\nWHERE'
           
            if num_pisos:
                filtros += f"AND i.numero_pisos = {num_pisos}" 
            if metros_terreno:
                filtros += f"AND i.m2_terreno = {metros_terreno}"
            if ciudad:
                filtros += f"AND c.nombre = '{ciudad}'"
            if parroquia:
                filtros += f"AND p.nombre = '{parroquia}'"
            if precio_min:
                filtros += f"AND i.precio_deseado_vendedor >= {precio_min}"
            if precio_max:
                filtros += f"AND i.precio_deseado_vendedor <= {precio_max}"
            if tipo_imb:
                filtros += f"AND ti.nombre = '{tipo_imb}'"
            filtros += "AND t.estado = false"
        else:
            filtros += "\nWHERE t.estado = false"
            
        consulta += filtros.replace('WHEREAND','WHERE')
        consulta = consulta.replace('AND', ' AND')
        print(consulta)
        return(consulta)
        

# c = CompraDB()
# c.filtro_compra(num_pisos=12,tipo_imb='Hola')