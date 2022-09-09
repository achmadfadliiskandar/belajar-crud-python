import mysql.connector

db = mysql.connector.connect(
host="localhost",
user="root",
password="",
database="datadiripy"
)

cursor = db.cursor()
sql = "SELECT * FROM warga"
cursor.execute(sql)

results = cursor.fetchall()

for data in results:
    print(data)