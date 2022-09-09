import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="datadiripy"
)

cursor = db.cursor()
id = input("masukan id db anda : ")
nama = input("masukan nama baru anda : ")
alamat = input("masukan alamat baru anda : ")
umur = input("masukan umur baru anda : ")

sql = "UPDATE warga SET nama=%s,alamat=%s,umur=%s WHERE id=%s"
value = (nama,alamat,umur,id)
cursor.execute(sql,value)
db.commit()
print("{} data berhasil diubah".format(cursor.rowcount))
exit()
