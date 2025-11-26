import mysql.connector
from mysql.connector import Error

# --- CONFIGURACIÓN DE LA CONEXIÓN ---
# NOTA: Para solo listar las bases de datos, a menudo no necesitas especificar una 'database',
# pero si tu usuario lo requiere, puedes usar cualquier base de datos existente (ej: 'mysql').
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = ""
# ------------------------------------

def mostrar_bases_de_datos():
    """
    Establece la conexión y ejecuta SHOW DATABASES.
    """
    conexion = None
    try:
        # 1. ESTABLECER LA CONEXIÓN
        print("Intentando conectar a MySQL...")
        conexion = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD
            # No especificamos 'database' aquí
        )

        if conexion.is_connected():
            print("✅ Conexión a MySQL exitosa.")

            # 2. CREAR UN CURSOR
            cursor = conexion.cursor()

            # 3. EJECUTAR EL COMANDO SQL
            print("\nEjecutando: SHOW DATABASES...")
            consulta_sql = "SHOW DATABASES"
            cursor.execute(consulta_sql)

            # 4. OBTENER Y MOSTRAR RESULTADOS
            # fetchall() devuelve una lista de tuplas, donde cada tupla tiene un solo elemento (el nombre de la DB)
            bases_de_datos = cursor.fetchall()

            print("\n--- Bases de Datos Disponibles ---")
            for db in bases_de_datos:
                # db[0] es el nombre de la base de datos
                print(f"| {db[0]}")
            print("-----------------------------------")


    except Error as e:
        # Manejo de errores de conexión
        print(f"❌ Error al conectar o consultar MySQL: {e}")

    finally:
        # 5. CERRAR CONEXIÓN
        if conexion is not None and conexion.is_connected():
            cursor.close()
            conexion.close()
            print("\n🔌 Conexión a MySQL cerrada.")

# Ejecutar la función
mostrar_bases_de_datos()