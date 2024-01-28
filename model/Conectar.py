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

    print(os.getenv('DATABASE_PASSWORD'))
    def __init__(self):
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
            except:
                self.resultado = []
            print("Filas afectadas:", count)
        except Exception as e:
            print("Error al ingresar:", e)

    def resultdo_consulta(self, sentencia):
        try:
            self.cursor = self.connection.cursor()
            self.cursor.execute(sentencia) # se ejecuta
            self.connection.commit() #
            #count = self.cursor.rowcount
            #print(count, "Registro insertado correctamente")
        except Exception as e:
            print("Error al en filtrar:", e)

        
