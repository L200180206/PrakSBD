import tkinter as tk
import tkinter.messagebox
from tkinter import*
import mysql.connector
from delete_buku_db import delete_buku

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="perpustakaan"
    )

c=db.cursor()

class Buku:
    def __init__(self, master):
        self.master = master
        self.master.title("Database Buku")
        self.master.geometry('300x300')
        self.frame = Frame(self.master)
        self.frame.grid()

        title = Label(self.frame, text="Database Buku", font=('Times', 16, 'bold'))
        l_id= Label(self.frame, text="ID Buku", font=('Times', 12))
        l_judul = Label(self.frame, text="Judul", font=('Times', 12))
        l_pengarang = Label(self.frame, text="Pegarang", font=('Times', 12))
        l_penerbit = Label(self.frame, text="Penerbit", font=('Times', 12))
        l_genre = Label(self.frame, text="Penerbit", font=('Times', 12))
        
        title.grid(row=0, columnspan=4, pady=10)
        l_id.grid(row=1, column=0, sticky=W, padx=3)
        l_judul.grid(row=2, column=0, sticky=W, padx=3)
        l_pengarang.grid(row=3, column=0, sticky=W, padx=3)
        l_penerbit.grid(row=4, column=0, sticky=W, padx=3)
        l_genre.grid(row=5, column=0, sticky=W, padx=3)
        
        
        #Entry dan posisi
        self.e_id = Entry(self.frame, width=30)
        self.e_judul = Entry(self.frame, width=30)
        self.e_pengarang = Entry(self.frame, width=30)
        self.e_penerbit = Entry(self.frame, width=30)
        self.e_genre = Entry(self.frame, width=30)
        
        self.e_id.grid(row=1, column=1, sticky=W, padx=10)
        self.e_judul.grid(row=2, column=1, sticky=W, padx=10)
        self.e_pengarang.grid(row=3, column=1, sticky=W, padx=10)
        self.e_penerbit.grid(row=4, column=1, sticky=W, padx=10)
        self.e_genre.grid(row=5, column=1, sticky=W, padx=10)


        #Button dan posisi
        b_insert = Button(self.frame, text="Insert", command=self.insert_buku)
        b_update = Button(self.frame, text="Update", command=self.update_buku)
        b_show = Button(self.frame, text="Show", command=self.show_buku)
        b_delete = Button(self.frame, text="Delete", command=self.delete_buku)
        

        b_insert.grid(row=6, column=0, pady=10, ipadx=10)
        b_update.grid(row=6, column=1, pady=10, ipadx=10)
        b_show.grid(row=7, column=1, pady=10, ipadx=10)
        b_delete.grid(row=7, column=0, pady=10, ipadx=10)
        
    def insert_buku(self):
        cursor = db.cursor()
        sql =f"INSERT INTO buku (`id_buku`,`judul`,`pengarang`, `penerbit`, `genre`)VALUES('{self.e_id.get()}','{self.e_judul.get()}','{self.e_pengarang.get()}', '{self.e_penerbit.get()}', '{self.e_genre.get()}')"         
        cursor.execute(sql)
        db.commit()
        messagebox.showinfo("","Entry Data Berhasil")
        
    
    def update_buku(self):
        c = db.cursor()
        e1=self.e_judul.get()
        e2=self.e_pengarang.get()
        e3=self.e_penerbit.get()
        e4=self.e_genre.get()
        e5=self.e_id.get()
        sql =f"UPDATE buku SET judul=%s, pengarang=%s ,penerbit=%s, genre=%s where id_buku=%s"
        val = (e1,e2,e3,e4,e5)
        c.execute(sql,val)
        db.commit()
        messagebox.showinfo("","Update Data Berhasil")

    def show_buku(self):
        show = Tk()
        show.title("Data Buku")
        Label(show, text="ID Buku").grid(row=0, column=0, sticky=W)
        Label(show, text="Judul").grid(row=0, column=1, sticky=W)
        Label(show, text="Pengarang").grid(row=0, column=2, sticky=W)
        Label(show, text="Penerbit").grid(row=0, column=3, sticky=W)
        Label(show, text="Genre").grid(row=0, column=4, sticky=W)

        
        sql="select*from buku"
        c.execute(sql)
        Buku = c.fetchall()

        for i in range(len(Buku)):
            for j in range(len(Buku[i])):
                teks=Entry(show)
                teks.grid(row=i+1,column=j)
                teks.insert(END,Buku[i][j])

    def delete_buku(self):
        self.delete_buku=Toplevel(self.master)
        self.UI=delete_buku(self.delete_buku)
        
        
        
    
        
        
        
        
