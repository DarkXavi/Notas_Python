# CONEXION MYSQL
# DESCARGANDO EXTENSION MYSQL (Weijan Chen)
# USANDO LIBRERÍA mysql-conector-python
import mysql.connector

config = {
  "host" : "127.0.0.1",
  "port" : "3306",
  "database" : "netflixdb",
  "user" : "",
  "password": ""
}

connection = mysql.connector.connect(**config)
cursor = connection.cursor()

query = "SELECT * FROM actores WHERE actor_id = 10 "
cursor.execute(query)
result = cursor.fetchall()

for row in result:
  print(row)
  
cursor.close()
connection.close()


#########################################################
# CONEXION SQL SERVER
# DESCARGANDO EXTENSION SQL SERVER (Microsoft)
# pip install pypdbc
import pyodbc

def conectar_sql(server, database, username, password):
  try:
    conn = pyodbc.connect('DRIVER={SQL Server}; SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
    print("Conección Exitosa")
    return conn
  except pyodbc.Error as e:
    print("Ocurrio un error al conectar: ", e)
    
def ejecutar_consulta(conn, query):
 try:
   cursor = conn.cursor()
   cursor.execute(query)
   rows = cursor.fetchall()
   return rows
 except pyodbc.Error as e:
   print("Ocurrio un error al ejecutar la consulta: ", e)
   

def cerrar_conexion(conn):
 try:
   conn.close()
   print("Conexión cerrada")
 except pyodbc.Error as e:
   print("Ocurrio un error al cerrar la conexión: ", e)


def main():
  server = ''
  database = ''
  username = ''
  password = ''
  conn = conectar_sql(server, database, username, password)
  if conn:
    query = 'Select * from (nombre tabla)'
    rows = ejecutar_consulta(conn, query)
    if rows:
      for row in rows:
        print(row)
    cerrar_conexion(conn)
    
main()