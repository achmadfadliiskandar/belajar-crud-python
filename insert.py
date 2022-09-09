import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "datadiripy"
)

nama = input("masukan nama : ")
alamat = input("masukan alamat : ")
umur = input("masukan umur anda : ")
value = (nama,alamat,umur)
cursor = db.cursor()
sql = "INSERT INTO warga (nama,alamat,umur) VALUES (%s,%s,%s)"
cursor.execute(sql,value)
db.commit()
print("{} data berhasil disimpan".format(cursor.rowcount))
