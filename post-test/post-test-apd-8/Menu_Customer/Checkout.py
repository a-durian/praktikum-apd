from Modular.ListGrosir import listGrosir
from Adds.dictnlist import Grosir, Keranjang_Belanja
from Modular.OpsiLagi import opsiLagi
from Menu_Customer.Menu import menuCustomer


# FUNGSI CHECKOUT KE KERANJANG BELANJA
def Checkout():
    print("")
    listGrosir()
    print("\nMasukkan [0] untuk kembali ke menu awal\n")
    menu_grosir_input = input("Silahkan pilih nomor produk untuk dimasukkan ke keranjang belanja: ")
    if menu_grosir_input.isdigit():
        menu_grosir = int(menu_grosir_input)
        if menu_grosir == 0:
            print("\nKembali ke menu awal...\n")
            menuCustomer()
        elif menu_grosir in Grosir:
            jumlah_input = input("Masukkan jumlah [1/2/...]: ")
            if jumlah_input == "":
                jumlah = 1
            elif jumlah_input.isdigit() and int(jumlah_input) > 0:
                jumlah = int(jumlah_input)
            else:
                print("\nJumlah tidak valid. Silahkan coba lagi.\n")
                Checkout()
            Keranjang_Belanja[menu_grosir] = Keranjang_Belanja.get(menu_grosir, 0) + jumlah
            nama = Grosir[menu_grosir]['nama']
            harga = Grosir[menu_grosir]['harga']
            print(f"\n+ {nama} x{jumlah} seharga Rp.{harga:,} berhasil ditambahkan ke keranjang belanja.\n")
            opsiLagi(menuCustomer, "Checkout produk lagi?", Checkout)
        else:
            print("\nProduk tidak ditemukan. Silahkan coba lagi.\n")
            Checkout()
    else:
        print("\n!! Input harus berupa nomor. Silahkan coba lagi. !!\n")
        Checkout()