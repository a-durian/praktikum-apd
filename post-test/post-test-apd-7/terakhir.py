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

# def secTopMessage(secTopMessage):
#     print
    
def pilihKarakter():
    print("\nPilih karakter anda:")
    print('1. Admin')
    print('2. Customer')
    pilihan_karakter = input("\nPilih opsi diatas sebelum memasuki program [1/2]: ")
    if pilihan_karakter == '1':
        menuAdmin()
    elif pilihan_karakter == '2':
        alurCustomer()
    else:
        print("\n!! Pilihan tidak valid. Silahkan coba lagi. !!")
        pilihKarakter()
        
def Registrasi():
    percobaan = 5
    def Login():
        while percobaan > 0:
            loginNama = input("Nama: ")
            loginPW = input("Password: ")
            if loginNama == inputNama and loginPW == inputPW:
                print("\nLogin berhasil!\n")
                topMessage(f"SELAMAT DATANG KEMBALI, {loginNama.upper()}")
                menuAdmin()
            else:
                percobaan -= 1
                print(f"\n!! Login gagal! Sisa percobaan: {percobaan} !!")
                return Login()
        print("\nAnda telah melakukan 5 percobaan login yang gagal. Program dihentikan.")
        return False
    try:
        inputNama = input("Masukkan Nama: ")
        inputPW = (input("Masukkan Password: "))
        if inputNama == "" or inputPW == "":
            raise ValueError("\n!! Nama dan Password tidak boleh kosong. Silahkan coba lagi. !!\n")
        elif (len(str(inputPW))) + 1 < 8:
            raise ValueError("\n!! Password harus terdiri dari minimal 8 karakter. Silahkan coba lagi. !!\n")
    except ValueError as e:
        print(e)
        return Registrasi()
    finally:
        print("\nSign up berhasil! silahkan login dengan akun anda:")
        return Login()

def menuAdmin():
    print("\n" + "-"* 10 + " Menu: Admin " + "-"*10)
    print('1. Produk yang tersedia')
    print('2. Tambah Produk')
    print('3. Hapus Produk')
    print('4. Logout')
    pilihanAdmin = input("\nPilih menu opsi yang tersedia diatas [1/2/3]: ")
    if pilihanAdmin == "1":
        listGrosir()
    elif pilihanAdmin == "2":
        topMessage("TAMBAH PRODUK")
        tambahProduk()
    elif pilihanAdmin == "3":
        topMessage("HAPUS PRODUK")
        
    elif pilihanAdmin == "4":
        print()
    
def listGrosir():
    topMessage("GROSIR")
    print(f"{'No':<4} {'Nama Produk':<30}{'Harga':>12}")
    print("-"*50)
    for i, produk in Grosir.items():
        print(f"{i:<4} {produk['nama']:<30} Rp.{produk['harga']:>9,}")
    kembaliKeMenu(menuAdmin)

def tambahProduk():
    nama_produk_baru = input("Masukkan nama produk baru: ")
    input_harga_produk_baru = input("Masukkan harga produk baru: Rp.")
    try:
        harga_produk_baru = int(input_harga_produk_baru)
        if nama_produk_baru == "" or harga_produk_baru <= 0:
            raise ValueError("\n!! Nama produk tidak boleh kosong dan harga harus lebih dari 0. Silahkan coba lagi. !!\n")
    except ValueError as e:
        print(e)
        return tambahProduk()
    else:
        id_baru = max(Grosir.keys()) + 1
        Grosir[id_baru] = {"nama": nama_produk_baru, "harga": harga_produk_baru}
        print(f"\nProduk '{nama_produk_baru}' dengan harga Rp.{harga_produk_baru:,} berhasil ditambahkan dengan ID {id_baru}!")
        tambahLagi(menuAdmin)

def hapusProduk():
    topMessage("HAPUS PRODUK")
    print(f"{'No':<4} {'Nama Produk':<30}{'Harga':>12}")
    print("-"*61)
    for i, produk in Grosir.items():
        print(f"{i:<4} {produk['nama']:<30} Rp.{produk['harga']:>9,}")
    print("-"*61)
    print("\nMasukkan [0] untuk kembali ke menu awal: ")
    def inputHapusProduk():
        try:
            inputHapus = int(input("Pilih nomor produk yang ingin dihapus: "))
            if not inputHapus.isdigit:
                raise ValueError("\n!! Input harus nomor. Silahkan coba lagi. !!\n")
            elif  not inputHapus in Grosir:
                raise ValueError("\n!! Nomor produk tidak ditemukan. Silahkan coba lagi. !!\n")
        except ValueError as e:
            print(e)
            inputHapusProduk
        else:
            if inputHapus == '0':
                print("\nKembali ke menu awal...\n")
                kembaliKeMenu(menuAdmin)
            else:
                del Grosir[inputHapus]
                print("\nProduk berhasil dihapus.")
            
            
            
    
    
def kembaliKeMenu(menuAwalnya):
    input_kembali = input("\nMasukkan [0] untuk kembali ke menu awal: ")
    if input_kembali == '0':
        print("kembali ke menu awal...")
        menuAwalnya()
    else:
        print("\n! Tolong ikuti instruksi yang tersedia. Silahkan coba lagi.\n")
        kembaliKeMenu(menuAwalnya)
        
# def alurAdmin():
#     print("\nSilahkan registrasi diri anda terlebih dahulu.")
    
#     Registrasi()
        
def alurCustomer():
    print("alur customer")
    
topMessage("SELAMAT DATANG DI KLIKCODEMARET")
pilihKarakter()

def tambahLagi(kembali):
    opsi_lagi = input("Tambah produk lagi? [y/n]: ")
    if opsi_lagi == "y" or opsi_lagi == "Y":
        return tambahProduk()
    elif opsi_lagi == "n" or opsi_lagi == "N":
        ("\nKembali ke menu awal..\n")
        kembaliKeMenu(kembali)
    else:
        print("\n!! Input tidak valid. Coba lagi !!\n")
        tambahProduk