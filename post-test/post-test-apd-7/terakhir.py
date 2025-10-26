from os import system, name
from time import sleep
if name == 'nt':
    _ = system('cls')
else:
    _ = system('clear')
    
# DICTIONARY PRODUK
Grosir = {
    1: {"nama": "Roti Tawar", "harga": 12000},
    2: {"nama": "Konohamie Mi Instan Goreng", "harga": 3200},
    3: {"nama": "Konohamie Mi Instan Kari Ayam", "harga": 3200},
    4: {"nama": "Geng-Geng Wafer Chocolate", "harga": 9900},
    5: {"nama": "Silver King", "harga": 25000},
    6: {"nama": "Lolari Sweat", "harga": 8000},
    7: {"nama": "Bad Day", "harga": 13000},
    8: {"nama": "Konohamilk", "harga": 14000},
    9: {"nama": "Youzone", "harga": 16000},
    10: {"nama": "Beras 5KG", "harga": 77000}
}

Keranjang_Belanja = {}
Riwayat_Transaksi = []



def topMessage(topMessage):
    print("="*len(topMessage))
    print("="*20 + topMessage + "="*20)
    print("="*len(topMessage))
    
def pilihKarakter():
    print("\nPilih karakter anda:")
    print('1. Admin')
    print('2. Customer')
    pilihan_karakter = input("\nPilih opsi diatas sebelum memasuki program [1/2]: ")
    if pilihan_karakter == '1':
        alurAdmin()
    elif pilihan_karakter == '2':
        alurCustomer()
    else:
        print("\n!! Pilihan tidak valid. Silahkan coba lagi. !!")
        pilihKarakter()
        
def Registrasi():
    def Login():
        percobaan = 5
        while percobaan > 0:
            loginNama = input("Nama: ")
            loginPW = input("Password: ")
            if loginNama == inputNama and loginPW == inputPW:
                print("\nLogin berhasil!")
                return True
            else:
                percobaan -= 1
                print(f"\nLogin gagal! Sisa percobaan: {percobaan}")
        print("\nAnda telah melakukan 5 percobaan login yang gagal. Program dihentikan.")
        return False
    try:
        inputNama = input("Masukkan Nama: ")
        inputPW = (input("Masukkan Password: "))
        if inputNama == "" or inputPW == "":
            raise ValueError("\n!! Nama dan Password tidak boleh kosong. Silahkan coba lagi. !!\n")
        elif (len(str(inputPW))) + 1 < 8:
            raise ValueError("\n!! Password harus terdiri dari minimal 8 karakter. Silahkan coba lagi. !!\n")
        else:
            print("\nSign up berhasil! silahkan login dengan akun anda:")
            return Login()
    except ValueError as e:
        print(e)
        return Registrasi()
    



def alurAdmin():
    print("\nSilahkan registrasi diri anda terlebih dahulu.")
    
    Registrasi()
        
def alurCustomer():
    print("alur customer")
    
topMessage("SELAMAT DATANG DI KLIKCODEMARET")
pilihKarakter()
        