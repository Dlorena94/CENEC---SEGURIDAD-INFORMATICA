import mysql.connector

conexion1=mysql.connector.connect(host="localhost",
                                  user="root",
                                  passwd="",
                                  database="tallercenec")

cursor1=conexion1.cursor()

print("---Ingreso de Nuevo Cliente---")
nif= input("Ingrese NIF/DNI del cliente:")
nombre= input("Ingrese el Nombre del cliente:")
apellidos= input("Ingrese los Apellidos:")

sql = "INSERT INTO clientes (nif, nombre, apellidos) VALUES (%s, %s, %s)"
datos= (nif,nombre,apellidos)

cursor1.execute(sql, datos)

conexion1.commit()
conexion1.close()