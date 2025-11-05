import mysql.connector
conexion1=mysql.connector.connect(host="localhost",
                                  user="root",
                                  passwd="",
                                  database="tallercenec")

cursor1=conexion1.cursor()


sql="insert into clientes(nif, nombre, apellidos) values (%s, %s,%s)"


datos=("01214596P", "Enrique", "Palomino Puentes")
cursor1.execute(sql, datos)

datos=("159643656L", "Sandra", "Suarez Silvia")
cursor1.execute(sql, datos)

datos=("789965412F", "Carmen", "Tejada Pinilla")
cursor1.execute(sql, datos)

conexion1.commit()
conexion1.close()
