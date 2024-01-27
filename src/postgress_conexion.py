import psycopg2
import os 
from dotenv import load_dotenv

load_dotenv()

conection = None
try:
    conection  = psycopg2.connect(
        host = os.getenv('DATABASE_HOST'),
        user = os.getenv('DATABASE_USER'),
        password = os.getenv('DATABASE_PASSWORD'),
        database = os.getenv('DATABASE_NAME'),
    )
    
    # Crear un objeto cursor
    cursor = conection.cursor()
    
    print('Coneccion realizada')
    
except Exception as e:
    print(e)
    

#cursor.close()
#conection.close()