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
    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'AND table_type = 'BASE TABLE';")
    filas = cursor.fetchall()
    for fila in filas:
        print(fila)
    #cursor.execute("INSERT INTO ")
    print()
    
except Exception as e:
    print(e)

finally:
    if conection != None:
        cursor.close()
        conection.close()



# Ejecutar una consulta SQL más compleja con JOIN
consulta_sql = """
    SELECT clientes.nombre AS nombre_cliente, pedidos.fecha, productos.nombre AS nombre_producto
    FROM pedidos
    JOIN clientes ON pedidos.cliente_id = clientes.id
    JOIN detalles_pedido ON pedidos.id = detalles_pedido.pedido_id
    JOIN productos ON detalles_pedido.producto_id = productos.id
    WHERE clientes.nombre = %s;
"""


#cursor.close()
#conection.close()
    
#Prueba de cambio para conection 

#cursor.close()
#conection.close()