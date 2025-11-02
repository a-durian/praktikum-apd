from Adds.Headline import topMessage
from Modular.ListGrosir import listGrosir
from Modular.OpsiLogout import opsiLogout
from Menu_Admin.TambahProduk import tambahProduk
from Modular.OpsiKembali import kembaliKeMenu
from HapusProduk import hapusProduk
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