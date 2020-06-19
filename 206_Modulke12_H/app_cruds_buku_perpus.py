import mysql.connector
import os

db = mysql.connector.connect(
    host ='localhost',
    user='root',
    passwd='',
    database='perpustakaan'
)

def insert_buku(db):
    id_buku = input("Masukkan ID Buku: ")
    judul = input("Masukkan Judul Buku: ")
    pengarang = input("Masukkan Nama Pengarang: ")
    penerbit = input ("Masukkan Nama Penerbit: ")
    genre = input("Masukkan Genre Buku: ")
    val = (id_buku, judul, pengarang, penerbit, genre)
    cursor=db.cursor()
    sql="insert into buku(id_buku, judul, pengarang, penerbit, genre) values(%s, %s, %s, %s, %s)"
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil dsimpan".format(cursor.rowcount))

def show_buku(db):
    cursor=db.cursor()
    sql="select*from buku"
    cursor.execute(sql)
    results=cursor.fetchall()

    if cursor.rowcount < 0:
        print("Tidak ada data")
    else:
        for data in results:
            print(data)

def update_buku(db):
    cursor = db.cursor()
    show_buku(db)
    id_buku = input("Pilih ID Buku> ")
    judul = input("Judul baru: ")
    pengarang = input("Nama Pengarang: ")
    penerbit = input ("Nama Penerbit: ")
    genre = input("Genre Buku: ")

    sql="update buku set  judul=%s, pengarang=%s, penerbit=%s, genre=%s where id_buku=%s"
    val=(judul, pengarang, penerbit, genre, id_buku)
    cursor.execute(sql, val)
    db.commit()

    print("{} data diubah".format(cursor.rowcount))

def delete_buku(db):
    cursor=db.cursor()
    show_buku(db)
    id_buku=input("Pilih ID Buku> ")
    sql = "delete from buku where id_buku=%s"
    val=(id_buku, )
    cursor.execute(sql, val)
    db.commit()

    print("{} data dihapus".format(cursor.rowcount))
    
def show_buku_menu(db):
    print("---DATABASE BUKU---")
    print("1. Tambahkan Data")
    print("2. Tampilkan Data")
    print("3. Update Data")
    print("4. Hapus Data")
    print("0. Keluar")
    menu= input("Pilih menu> ")

    os.system("clear")
    if menu=="1":
        insert_buku(db)
    elif menu=="2":
        show_buku(db)
    elif menu=="3":
        update_buku(db)
    elif menu=="4":
        delete_buku(db)
    elif menu=="0":
        exit()
    else:
        print("Pilih menu yang tersedia")

if __name__ == "__main__":
    while(True):
        show_buku_menu(db)
