import psycopg2

#Algo

try:
    conection  = psycopg2.connect()
except Exception as e:
    print(e)