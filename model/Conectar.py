import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()
# -*- coding: utf-8 -*-

class Conectar:
    sentencia = ""
    connection = None
    cursor = None
    resultado = None
    
    def conectar_(self):
        try:
            # Establecer la conexión a la base de datos
            self.connection  = psycopg2.connect(
                host = os.getenv('DATABASE_HOST'),
                user = os.getenv('DATABASE_USER'),
                port = os.getenv('DATABASE_PORT'),
                password = os.getenv('DATABASE_PASSWORD'), 
                database = os.getenv('NAME')
            )
        except Exception as e:
            print("Error al conectar al base:", e)

    def ingresar_sentencia(self, sentencia):
        try:
            self.cursor = self.connection.cursor()
            self.cursor.execute(sentencia) # se ejecuta
            count = self.cursor.rowcount
            self.connection.commit() #
            
            try: # en caso de que no regrese nada
                self.resultado = self.cursor.fetchall()
                print(self.resultado)
            except psycopg2.Error as e:
                print("Error al obtener resultados:", e)
            print("Filas afectadas:", count)
        except psycopg2.Error as e:
            print("Error al ejecutar la consulta:", e)

        finally:
            if self.cursor:
                self.cursor.close()

            if self.connection:
                self.connection.close()
            
        
