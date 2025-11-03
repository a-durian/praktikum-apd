

def menuAdmin():
    topMessage("Menu: Admin")
    print('1. Produk yang tersedia')
    print('2. Tambah Produk')
    print('3. Hapus Produk')
    print('4. Logout')
    pilihanAdmin = input("\nPilih menu opsi yang tersedia diatas [1/2/3/4]: ")
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
        opsiLogout(menuAdmin, "admin")
    else:
        print("\n!! Pilihan tidak valid. Silahkan coba lagi. !!\n")
        return menuAdmin()
    
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
        if intInputHapus == 0:
            print("\nKembali ke menu awal...\n")
            menuAdmin()
        elif intInputHapus not in Grosir:
            print("\n!! Nomor produk tidak ditemukan. Silahkan coba lagi. !!\n")
            inputHapusProduk() 
        
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