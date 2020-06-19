import mysql.connector
import os

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="perpustakaan"
)

def insert_status(db):
    id_memberFK =input("Masukkan ID Member: ")
    id_bukuFK = input("Masukkan ID Buku: ")
    tanggal_pinjam = input("Tanggal Pinjam: ")
    tanggal_kembali = input("Tanggal Kembali: ")
    cursor=db.cursor()
    sql= "insert into peminjaman_pengembalian(id_memberFK, id_bukuFK, tanggal_pinjam, tanggal_kembali) values (%s, %s,%s, %s)"
    val = (id_memberFK, id_bukuFK, tanggal_pinjam, tanggal_kembali)
    cursor.execute(sql, val)
    db.commit()

    print("{} data ditambahkan".format(cursor.rowcount))

def show_status(db):
    cursor=db.cursor()
    sql="select*from peminjaman_pengembalian"
    cursor.execute(sql)
    results=cursor.fetchall()

    if cursor.rowcount < 0:
        print("Tidak ada data")
    else:
        for data in results:
            print(data)

def update_status(db):
    cursor = db.cursor()
    show_status(db)
    id_memberFK = input("Pilih ID Member> ")
    id_bukuFK = input("ID buku baru: ")

    sql="update peminjaman_pengembalian set id_bukuFK=%s where id_memberFK=%s"
    val=(id_bukuFK, id_memberFK)
    cursor.execute(sql, val)
    db.commit()

    print("{} data diubah".format(cursor.rowcount))

def delete_status(db):
    cursor=db.cursor()
    show_status(db)
    id_member=input("Pilih ID Member> ")
    sql = "delete from peminjaman_pengembalian where id_memberFK=%s"
    val=(id_member, )
    cursor.execute(sql, val)
    db.commit()

    show_status
    (db)
    print("{} data dihapus".format(cursor.rowcount))



def show_menu(db):
    print("---DATABASE PEMINJAMAN DAN PENGEMBALIAN BUKU---")
    print("1. Tambahkan Status Buku")
    print("2. Tampilkan Status Buku")
    print("3. Update Status Buku")
    print("4. Hapus Status Buku")
    print("0. Keluar")
    menu=input("Pilih menu> ")

    os.system("clear")
    if menu=="1":
        insert_status(db)
    elif menu=="2":
        show_status(db)
    elif menu=="3":
        update_status(db)
    elif menu=="4":
        delete_status(db)
    elif menu=="0":
        exit()
    else:
        print("Pilih menu yang tersedia")

if __name__=="__main__":
    while(True):
        show_menu(db)
