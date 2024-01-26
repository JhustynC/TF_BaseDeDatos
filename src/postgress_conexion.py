import psycopg2

try:
    conection  = psycopg2.connect()
except Exception as e:
    print(e)
    
    
