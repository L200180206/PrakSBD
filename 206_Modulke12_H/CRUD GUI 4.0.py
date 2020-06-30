import tkinter as tk
import tkinter.messagebox
from tkinter import*
import mysql.connector
from member_db import Member
from buku_db import Buku
from status_db import Status


db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="perpustakaan"
    )

c=db.cursor()

root = tk.Tk()

def CRUD():
    UI=FPage(root)
    cursor=db.cursor()

class FPage:
    def __init__(self, master):
        self.master = master
        self.master.geometry("400x400")
        self.master.config(bg = 'white')
        self.frame = Frame(self.master, bg = 'white')
        self.frame.pack()
        
        title = Label(self.frame, text='SELAMAT DATANG', font=('Times', 18, 'bold'))
        title.pack()
        title2 = Label(self.frame, text='Pilih Menu', font=('Times', 14))
        title2.pack(pady=20)
        btnMember = Button(self.frame, text="Member", font=(18), command=self.Member)
        btnMember.pack(anchor=CENTER, pady=10, ipadx=9)
        btnBuku = Button(self.frame, text="Buku", font=(18), command=self.Buku)
        btnBuku.pack(anchor=CENTER, pady=10, ipadx=20)
        btnStatus = Button(self.frame, text="Status", font=(18), command=self.Status)
        btnStatus.pack(anchor=CENTER, pady=10, ipadx=15)

    def Member(self):
        self.Member=Toplevel(self.master)
        self.UI=Member(self.Member)

    def Buku(self):
        self.Buku=Toplevel(self.master)
        self.UI=Buku(self.Buku)

    def Status(self):
        self.Status=Toplevel(self.master)
        self.UI=Status(self.Status)

    


CRUD()
