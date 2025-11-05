import mysql.connector

conexion1=mysql.connector.connect(host="localhost",
                                  user="root",
                                  passwd="",
                                  database="tallercenec")
cursor1=conexion1.cursor()
cursor1.execute("delete from clientes  where id=1")
cursor1.execute("update from clientes where email=ratonperz@hotmaul.com")
conexion1.commit()
cursor1.execute("select id, email from clientes")
for fila in cursor1:
    print(fila)
conexion1.close()