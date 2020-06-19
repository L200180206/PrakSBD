import mysql.connector
import os

db = mysql.connector.connect(
    host ='localhost',
    user='root',
    passwd='',
    database='perpustakaan'
)

def insert_member(db):
    id_member=input("Masukkan ID Member: ")
    nama=input("Masukkan Nama: ")
    nim=input("Masukkan NIM: ")
    alamat=input("Masukkan Alamat: ")
    cursor=db.cursor()
    sql= "insert into member(id_member, nama, nim, alamat) values (%s, %s, %s, %s)"
    val = (id_member, nama, nim, alamat)
    cursor.execute(sql, val)
    db.commit()

    print("{} data ditambahkan".format(cursor.rowcount))

def show_member(db):
    cursor=db.cursor()
    sql="select*from member"
    cursor.execute(sql)
    results=cursor.fetchall()

    if cursor.rowcount < 0:
        print("Tidak ada data")
    else:
        for data in results:
            print(data)

def update_member(db):
    cursor = db.cursor()
    show_member(db)
    id_member = input("Pilih ID Member> ")
    nama = input("Nama baru: ")
    nim = input("NIM baru: ")
    alamat = input ("Alamat baru: ")
    

    sql="update member set nama=%s, nim=%s, alamat=%s where id_member=%s"
    val=(nama, nim, alamat, id_member)
    cursor.execute(sql, val)
    db.commit()

    print("{} data diubah".format(cursor.rowcount))

def delete_member(db):
    cursor=db.cursor()
    show_member(db)
    id_member=input("Pilih ID Member> ")
    sql = "delete from member where id_member=%s"
    val=(id_member, )
    cursor.execute(sql, val)
    db.commit()

    print("{} data dihapus".format(cursor.rowcount))

def show_member_menu(db):
    print("---DATABASE MEMBER---")
    print("1. Tambahkan Data")
    print("2. Tampilkan Data")
    print("3. Update Data")
    print("4. Hapus Data")
    print("0. Keluar")
    menu= input("Pilih menu> ")

    os.system("clear")
    if menu=="1":
        insert_member(db)
    elif menu=="2":
        show_member(db)
    elif menu=="3":
        update_member(db)
    elif menu=="4":
        delete_member(db)
    elif menu=="0":
        exit()
    else:
        print("Pilih menu yang tersedia")

if __name__ == "__main__":
    while(True):
        show_member_menu(db)
