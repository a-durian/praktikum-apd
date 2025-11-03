# IMPORT DICT N LIST
from Adds.dictnlist import Grosir
from prettytable import PrettyTable
tabel = PrettyTable()

# FUNGSI PILIH KARAKTER
def pilihKarakter():
    print("\nPilih karakter anda:")
    print('1. Admin')
    print('2. Customer')
    pilihan_karakter = input("\nPilih opsi diatas sebelum memasuki program [1/2]: ")
    if pilihan_karakter == '1':
        Registrasi(menuAdmin)
        menuAdmin()
    elif pilihan_karakter == '2':
        Registrasi(menuCustomer)
        menuCustomer()
    else:
        print("\n!! Pilihan tidak valid. Silahkan coba lagi. !!")
        pilihKarakter()
        
# FUNGSI LIST GROSIR
def listGrosir():
    # print(f"{'No':<4} {'Nama Produk':<30}{'Harga':>12}")
    # print("-"*50)
    # for i, produk in Grosir.items():
    #     print(f"{i:<4} {produk['nama']:<30} Rp.{produk['harga']:>9,}")
    # print("-"*50)
    
    tabel.field_names = ["No.", "Produk", "Harga"]
    for i, produk in Grosir.items():
        tabel.add_row([i, produk['nama'], produk['harga']])
    print(tabel)
    

# FUNGSI KEMBALI KE MENU()
def kembaliKeMenu(menuAwalnya):
    input_kembali = input("\nMasukkan [0] untuk kembali ke menu awal: ")
    if input_kembali == '0':
        print("kembali ke menu awal...\n")
        menuAwalnya()
    else:
        print("\n!! Tolong ikuti instruksi yang tersedia. Silahkan coba lagi. !!\n")
        kembaliKeMenu(menuAwalnya)
        

# FUNGSI OPSI MENGULANG LAGI ATAU KEMBALI KE MENU AWAL
def opsiLagi(kembali, outputLagi, fungsiKembali):
    opsi_lagi = input(f"{outputLagi} [y/n]: ")
    if opsi_lagi == "y" or opsi_lagi == "Y":
        return fungsiKembali()
    elif opsi_lagi == "n" or opsi_lagi == "N":
        print("\nKembali ke menu awal..\n")
        kembali()
    else:
        print("\n!! Input tidak valid. Coba lagi !!\n")
        opsiLagi(kembali, outputLagi, fungsiKembali)
        

# FUNGSI OPSI LOGOUT
def opsiLogout(insertMenu, menuApa):
    inputLogout = input("\nApakah anda yakin untuk logout dari akun anda? [y/n]: ")
    if inputLogout == "y" or inputLogout == "Y":
        print("\nLogout berhasil. Kembali ke halaman awal..\n")
        pilihKarakter()
    elif inputLogout == "n" or inputLogout == "N":
        print(f"\nKembali ke menu {menuApa}..\n")
        insertMenu()
    else:
        print("\n!! Input tidak valid. Silahkan coba lagi. !!")
        return opsiLogout(insertMenu)