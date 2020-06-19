import os
from app_cruds_buku_perpus import *
from app_cruds_member_perpus import *
from app_cruds_pinjam_kembali_perpus import *

def show_app():
    print("---Selamat Datang---")
    print("Pilih menu yang tersedia:")
    print("1. Database Member")
    print("2. Database Buku")
    print("3. Peminjaman dan Pengembalian")
    print("0. Keluar")
    menu= input("> ")

    os.system("clear")
    if menu=="1":
        show_member_menu(db)
    elif menu=="2":
        show_buku_menu
        (db)
    elif menu=="3":
        show_menu(db)
    elif menu=="0":
        exit()
    else:
        print("Silahkan pilih menu yang ada")
              
if __name__=="__main__":
    while(True):
        show_app()
