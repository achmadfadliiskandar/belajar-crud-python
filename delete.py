import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="datadiripy",
)

cursor = db.cursor()
id = input("masukan id anda : ")
sql = "DELETE FROM warga WHERE id=%s"
value = (id,)
cursor.execute(sql,value)
db.commit()
print("{} data berhasil dihapus".format(cursor.rowcount))