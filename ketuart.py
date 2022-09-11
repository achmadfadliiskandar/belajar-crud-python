import mysql.connector
import os

db = mysql.connector.connect(
host="localhost",
user="root",
password="",
database="datadiripy"
)
# tambah data
def insert_data(db):
    nama = input("Masukan Nama Rt: ")
    alamat = input("Masukan Alamat Rt: ")
    kodert = input("Masukan Kode Rt: ")
    tahunjabatan = input("Masukan Tahun Jabatan: ")
    value = (nama,alamat,kodert,tahunjabatan)
    cursor = db.cursor()
    sql = "INSERT INTO ketuart (nama,alamat,kodert,tahunjabatan) VALUES (%s,%s,%s,%s)"
    cursor.execute(sql,value)
    db.commit()
    print("{} data berhasil disimpan".format(cursor.rowcount))

# lihat semua data ketua rt
def show_data(db):
    cursor = db.cursor()
    sql = "SELECT * FROM ketuart"
    cursor.execute(sql)
    result = cursor.fetchall()

    if cursor.rowcount < 0 :
        print("Tidak ada data")
    else:
        for data in result:
            print(data)

# update data
def update_data(db):
    cursor = db.cursor()
    show_data(db)
    id = input("masukan id ketua Rt: ")
    nama = input("Masukan Nama Rt Baru: ")
    alamat = input("Masukan Alamat Rt Baru: ")
    kodert = input("Masukan Kode Rt Baru: ")
    tahunjabatan = input("Masukan Tahun Jabatan Baru : ")
    sql = "UPDATE ketuart SET nama=%s,alamat=%s,kodert=%s,tahunjabatan=%s WHERE id=%s"
    value = (nama,alamat,kodert,tahunjabatan,id)
    cursor.execute(sql,value)
    db.commit()
    print("{} data berhasil diubah".format(cursor.rowcount))

    # delete data
def delete_data(db):
    cursor = db.cursor()
    show_data(db)
    id = input("Masukan Id Yang Ingin Dihapus: ")
    sql = "DELETE FROM ketuart WHERE id=%s"
    value = (id,)
    cursor.execute(sql,value)
    db.commit()
    print("{} data berhasil dihapus".format(cursor.rowcount))

        # search data melalui nama dan kodert
def search_data(db):
    cursor = db.cursor()
    keyword = input("Kata Kunci: ")
    sql = "SELECT * FROM ketuart WHERE nama LIKE %s OR kodert LIKE %s"
    value = ("%{}%".format(keyword),"%{}%".format(keyword))
    cursor.execute(sql,value)
    result = cursor.fetchall()

    if cursor.rowcount < 0 :
        print("tidak ada data")
    else:
        for data in result:
            print(data)

        # membuat menu aplikasi
def show_menu(db):
    print("===APLIKASI DATA KETUA RT===")
    print("1.TAMBAH DATA")
    print("2.TAMPILKAN DATA")
    print("3.UPDATE DATA")
    print("4.HAPUS DATA")
    print("5.CARI DATA")
    print("0.KELUAR")
    print("----------------")
    menu = input("Pilih Menu: ")
    # bersihkan menu
    os.system("clear")

    # memilih menu
    if menu == "1":
        insert_data(db)
    elif menu == "2":
        show_data(db)
    elif menu == "3":
        update_data(db)
    elif menu == "4":
        delete_data(db)
    elif menu == "5":
        search_data(db)
    elif menu == "0":
        exit()
    else:
        print("menu salah")

if __name__== "__main__":
    while(True):
        show_menu(db)