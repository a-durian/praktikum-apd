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

# FUNGSI TOP MESSAGE
def topMessage(topMessage):
    msgLong = ("="*21 + f" {topMessage} " + "="*21)
    print("="*len(msgLong))
    print(msgLong)
    print("="*len(msgLong))
# FUNGSI PILIH KARAKTER
def pilihKarakter():
    print("\nPilih karakter anda:")
    print('1. Admin')
    print('2. Customer')
    pilihan_karakter = input("\nPilih opsi diatas sebelum memasuki program [1/2]: ")
    if pilihan_karakter == '1':
        Registrasi()
        menuAdmin()
    elif pilihan_karakter == '2':
        Registrasi()
        menuCustomer()
    else:
        print("\n!! Pilihan tidak valid. Silahkan coba lagi. !!")
        pilihKarakter()
# FUNGSI REGISTRASI DAN LOGIN ADMIN
def Registrasi():
    def Login():
        percobaan = 5
        while percobaan > 0:
            loginNama = input("Nama: ")
            loginPW = input("Password: ")
            if loginNama == inputNama and loginPW == inputPW:
                print("\nLogin berhasil!\n")
                topMessage(f"SELAMAT DATANG KEMBALI, {loginNama.upper()}")
                menuAdmin()
                return True
            else:
                percobaan -= 1
                print(f"\n!! Login gagal! Sisa percobaan: {percobaan} !!")
                
        print("\nAnda telah melakukan 5 percobaan login yang gagal. Program dihentikan.")
        return False
    print("hehhhhhhh")#######
    try:
        inputNama = input("Masukkan Nama: ")
        inputPW = input("Masukkan Password: ")
        if inputNama == "" or inputPW == "":
            raise ValueError("\n!! Nama atau Password tidak boleh kosong. Silahkan coba lagi. !!\n")
        elif (len(str(inputPW))) + 1 < 8:
            raise ValueError("\n!! Password harus terdiri dari minimal 8 karakter. Silahkan coba lagi. !!\n")
    except ValueError as e:
        print(e)
        return Registrasi()
    finally:
        print("\nSign up berhasil! silahkan login dengan akun anda:")
        return Login()
# FUNGSI MENU ADMIN
def menuAdmin():
    topMessage("Menu: Admin")
    print('1. Produk yang tersedia')
    print('2. Tambah Produk')
    print('3. Hapus Produk')
    print('4. Logout')
    pilihanAdmin = input("\nPilih menu opsi yang tersedia diatas [1/2/3]: ")
    if pilihanAdmin == "1":
        topMessage("GROSIR")
        listGrosir()
        kembaliKeMenu(menuAdmin)
    elif pilihanAdmin == "2":
        topMessage("TAMBAH PRODUK")
        tambahProduk()
    elif pilihanAdmin == "3":
        topMessage("HAPUS PRODUK")
        hapusProduk()
    elif pilihanAdmin == "4":
        opsiLogout(menuAdmin)
    else:
        print("\n!! Pilihan tidak valid. Silahkan coba lagi. !!\n")
        return menuAdmin()
# FUNGSI LIST GROSIR
def listGrosir():
    print(f"{'No':<4} {'Nama Produk':<30}{'Harga':>12}")
    print("-"*50)
    for i, produk in Grosir.items():
        print(f"{i:<4} {produk['nama']:<30} Rp.{produk['harga']:>9,}")
    print("-"*50)
# FUNGSI TAMBAH PRODUK
def tambahProduk():
    nama_produk_baru = input("\nMasukkan nama produk baru: ")
    harga_produk_baru = input("Masukkan harga produk baru: Rp.")
    try:
        harga_produk_baru = int(harga_produk_baru)
    except ValueError:
        print("\n!! Harga produk harus berupa angka. Silahkan coba lagi. !!\n")
        tambahProduk()
    if nama_produk_baru == "" or nama_produk_baru == " " or  harga_produk_baru == "" or harga_produk_baru == " " :
        print("\n!! Nama atau harga produk tidak boleh kosong. Silahkan coba lagi. !!\n")
    elif harga_produk_baru <= 0:
        print("\n!! Harga produk harus lebih dari 0. Silahkan coba lagi. !!\n")
    id_baru = max(Grosir.keys()) + 1
    Grosir[id_baru] = {"nama": nama_produk_baru, "harga": harga_produk_baru}
    print(f"\nProduk '{nama_produk_baru}' dengan harga Rp.{harga_produk_baru:,} berhasil ditambahkan dengan ID {id_baru}!")
    opsiLagi(menuAdmin, "Tambah produk lagi?", tambahProduk)
# FUNGSI HAPUS PRODUK
def hapusProduk():
    listGrosir()
    print("\nMasukkan [0] untuk kembali ke menu awal")
    def inputHapusProduk():
        inputHapus = input("Pilih nomor produk yang ingin dihapus: ")
        
        try:
            intInputHapus = int(inputHapus)
        except ValueError:
            print("\n!! Input harus nomor. Silahkan coba lagi. !!\n")
            inputHapusProduk()
        if intInputHapus not in Grosir:
            print("\n!! Nomor produk tidak ditemukan. Silahkan coba lagi. !!\n")
            inputHapusProduk() 
        elif intInputHapus == 0:
            print("\nKembali ke menu awal...\n")
            menuAdmin()
        del Grosir[intInputHapus]
        # Mengatur ulang nomor urut
        grosirBaru = {}
        idBaru = 1
        for _, produk in sorted(Grosir.items()):
            grosirBaru[idBaru] = produk
            idBaru += 1
        # Update dictionary Grosir dengan nomor yang baru
        Grosir.clear()
        Grosir.update(grosirBaru)
        print("\nProduk berhasil dihapus.")
        opsiLagi(menuAdmin, "Hapus produk lagi?", hapusProduk)
    inputHapusProduk()
# FUNGSI KEMBALI KE MENU AWAL
def kembaliKeMenu(menuAwalnya):
    input_kembali = input("\nMasukkan [0] untuk kembali ke menu awal: ")
    if input_kembali == '0':
        print("kembali ke menu awal...")
        menuAwalnya()
    else:
        print("\n! Tolong ikuti instruksi yang tersedia. Silahkan coba lagi.\n")
        kembaliKeMenu(menuAwalnya)
# FUNGSI ALUR CUSTOMER
def menuCustomer():
    print("alur customer")
    
# FUNGSI OPSI MENGULANG LAGI ATAU KEMBALI KE MENU AWAL
def opsiLagi(kembali, outputLagi, fungsiKembali):
    opsi_lagi = input(f"{outputLagi} [y/n]: ")
    if opsi_lagi == "y" or opsi_lagi == "Y":
        return fungsiKembali()
    elif opsi_lagi == "n" or opsi_lagi == "N":
        print("\nKembali ke menu awal..\n")
        menuAdmin()
    else:
        print("\n!! Input tidak valid. Coba lagi !!\n")
        opsiLagi(kembali, outputLagi, fungsiKembali)
# FUNGSI OPSI LOGOUT
def opsiLogout(insertMenu):
    inputLogout = input("\nApakah anda yakin untuk logout dari akun anda? [y/n]: ")
    if inputLogout == "y" or inputLogout == "Y":
        print("\nLogout berhasil. Kembali ke halaman awal..\n")
        pilihKarakter()
    elif inputLogout == "n" or inputLogout == "N":
        print("\nKembali ke menu admin..\n")
        insertMenu()
    else:
        print("\n!! Input tidak valid. Silahkan coba lagi. !!")
        return opsiLogout(insertMenu)

# MAIN PROGRAM
topMessage("SELAMAT DATANG DI KLIKCODEMARET")
pilihKarakter()

# Catatan perhatian!:
