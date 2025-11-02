
# IMPORT LIST GROSIR
from Modular.ListGrosir import listGrosir
from Adds.dictnlist import Grosir
from Modular.OpsiLagi import opsiLagi
from Menu_Admin.Menu import menuAdmin
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