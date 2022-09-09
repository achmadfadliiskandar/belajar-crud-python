import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="datadiripy"
)

cursor = db.cursor()

sql = """CREATE TABLE warga (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(255),
    alamat VARCHAR(255),
    umur INTEGER (11)
)
"""

cursor.execute(sql)

print("Tabel Warga Berhasil Dibuat")