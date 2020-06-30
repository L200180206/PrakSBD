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

class Member:
    def __init__(self, master):
        self.master = master
        self.master.title("Database Member")
        self.master.geometry('300x300')
        self.frame = Frame(self.master)
        self.frame.grid()

        title = Label(self.frame, text="Database Member", font=('Times', 16, 'bold'))
        l_id = Label(self.frame, text="ID Member", font=('Times', 12))
        l_nama = Label(self.frame, text="Nama", font=('Times', 12))
        l_nim = Label(self.frame, text="NIM", font=('Times', 12))
        l_alamat = Label(self.frame, text="Alamat", font=('Times', 12))
        
        title.grid(row=0, columnspan=4, pady=10)
        l_id.grid(row=1, column=0, sticky=W, padx=3)
        l_nama.grid(row=2, column=0, sticky=W, padx=3)
        l_nim.grid(row=3, column=0, sticky=W, padx=3)
        l_alamat.grid(row=4, column=0, sticky=W, padx=3)
        
        
        #Entry dan posisi
        self.e_id = Entry(self.frame, width=30)
        self.e_nama = Entry(self.frame, width=30)
        self.e_nim = Entry(self.frame, width=30)
        self.e_alamat = Entry(self.frame, width=30)
        
        self.e_id.grid(row=1, column=1, sticky=W, padx=10)
        self.e_nama.grid(row=2, column=1, sticky=W, padx=10)
        self.e_nim.grid(row=3, column=1, sticky=W, padx=10)
        self.e_alamat.grid(row=4, column=1, sticky=W, padx=10)

        #Button dan posisi
        b_insert = Button(self.frame, text="Insert", command=self.insert_member)
        b_update = Button(self.frame, text="Update", command=self.update_member)
        b_show = Button(self.frame, text="Show", command=self.show_member)

        b_insert.grid(row=5, column=0, pady=10, ipadx=10)
        b_update.grid(row=5, column=1, pady=10, ipadx=10)
        b_show.grid(row=7, column=1, pady=10, ipadx=10)
        
    def insert_member(self):
        c = db.cursor()
        sql =f"INSERT INTO member (`id_member`,`nama`,`nim`, `alamat`)VALUES('{self.e_id.get()}','{self.e_nama.get()}','{self.e_nim.get()}', '{self.e_alamat.get()}')"         
        c.execute(sql)
        db.commit()
        messagebox.showinfo("","Entry Data Berhasil")
    
    def update_member(self):
        c = db.cursor()
        e1=self.e_nama.get()
        e2=self.e_nim.get()
        e3=self.e_alamat.get()
        e4=self.e_id.get()
        sql =f"UPDATE member SET nama=%s, nim=%s ,alamat=%s where id_member=%s"
        val = (e1,e2,e3,e4)
        c.execute(sql,val)
        db.commit()
        messagebox.showinfo("","Update Data Berhasil")

    def show_member(self):
        show = Tk()
        show.title("Data Member")
        Label(show, text="ID Member").grid(row=0, column=0, sticky=W)
        Label(show, text="Nama").grid(row=0, column=1, sticky=W)
        Label(show, text="NIM").grid(row=0, column=2, sticky=W)
        Label(show, text="Alamat").grid(row=0, column=3, sticky=W)
        

        
        sql="select*from member"
        c.execute(sql)
        Member = c.fetchall()

        for i in range(len(Member)):
            for j in range(len(Member[i])):
                teks=Entry(show)
                teks.grid(row=i+1,column=j)
                teks.insert(END,Member[i][j])
