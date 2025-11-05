

conn = mariadb.connect(
    host="localhost", port=3306,
    user="root", password="",
    database="taller"
)
cur = conn.cursor()
cur.execute("SELECT VERSION()")
print("MariaDB:", cur.fetchone()[0])
conn.close()

