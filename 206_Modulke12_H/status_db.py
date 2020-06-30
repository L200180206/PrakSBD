import tkinter as tk
import tkinter.messagebox
from tkinter import*
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="perpustakaan"
    )

c=db.cursor()

class Status:
    def __init__(self, master):
        self.master = master
        self.master.geometry('450x250')
        self.frame = Frame(self.master)
        self.frame.grid()

        title = Label(self.frame, text="Pendataan Peminjaman dan Pengembalian Buku", font=('Times', 16, 'bold'))
        l_id_member = Label(self.frame, text="ID Member", font=('Times', 12))
        l_id_buku = Label(self.frame, text="ID Buku", font=('Times', 12))
        l_pinjam = Label(self.frame, text="Tanggal Pinjam", font=('Times', 12))
        l_kembali= Label(self.frame, text="Tanggal Kembali", font=('Times', 12))
        
        title.grid(row=0, columnspan=4, pady=10)
        l_id_member.grid(row=1, column=0, sticky=W, padx=3)
        l_id_buku.grid(row=2, column=0, sticky=W, padx=3)
        l_pinjam.grid(row=3, column=0, sticky=W, padx=3)
        l_kembali.grid(row=4, column=0, sticky=W, padx=3)
        
        
        #Entry dan posisi
        self.e_id_member = Entry(self.frame, width=30)
        self.e_id_buku = Entry(self.frame, width=30)
        self.e_pinjam= Entry(self.frame, width=30)
        self.e_kembali = Entry(self.frame, width=30)
        
        self.e_id_member.grid(row=1, column=1, sticky=W, padx=10)
        self.e_id_buku.grid(row=2, column=1, sticky=W, padx=10)
        self.e_pinjam.grid(row=3, column=1, sticky=W, padx=10)
        self.e_kembali.grid(row=4, column=1, sticky=W, padx=10)

        #Button dan posisi
        b_insert = Button(self.frame, text="Insert", command=self.insert_status)
        b_update = Button(self.frame, text="Update", command=self.update_status)
        b_show = Button(self.frame, text="Show", command=self.show_status)

        b_insert.grid(row=5, column=0, pady=10, ipadx=10)
        b_update.grid(row=5, column=1, pady=10, ipadx=10)
        b_show.grid(row=5, column=2, pady=10, ipadx=10)
        
    def insert_status(self):
        c = db.cursor()
        sql =f"INSERT INTO peminjaman_pengembalian (`id_memberFK`,`id_bukuFK`,`tanggal_pinjam`, `tanggal_kembali`)VALUES('{self.e_id_member.get()}','{self.e_id_buku.get()}','{self.e_pinjam.get()}', '{self.e_kembali.get()}')"         
        c.execute(sql)
        db.commit()
        messagebox.showinfo("","Entry Data Berhasil")
    
    def update_status(self):
        c = db.cursor()
        e1=self.e_id_member.get()
        e2=self.e_id_buku.get()
      
        sql =f"UPDATE peminjaman_pengembalian SET id_bukuFK=%s where id_memberFK=%s"
        val = (e1,e2)
        c.execute(sql,val)
        db.commit()
        messagebox.showinfo("","Update Data Berhasil")

    def show_status(self):
        status = Tk()
        status.title("Alur Perputaran Buku")
        Label(status, text="ID Member").grid(row=0, column=0, sticky=W)
        Label(status, text="ID Buku").grid(row=0, column=1, sticky=W)
        Label(status, text="Tanggal Pinjam").grid(row=0, column=2, sticky=W)
        Label(status, text="Tanggal Kembali").grid(row=0, column=3, sticky=W)
        
        
        sql="select*from peminjaman_pengembalian"
        c.execute(sql)
        Status = c.fetchall()

        for i in range(len(Status)):
            for j in range(len(Status[i])):
                teks=Entry(status)
                teks.grid(row=i+1,column=j)
                teks.insert(END,Status[i][j])
