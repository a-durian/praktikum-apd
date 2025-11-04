from tambahan import kembaliKeMenu, opsiLagi, opsiLogout
from data_dictlist import Grosir, Keranjang_Belanja, Riwayat_Transaksi
from admin1 import listGrosir
from helperss import topMessage
# FUNGSI ALUR CUSTOMER
def menuCustomer():
    topMessage("Menu: Customer")
    print("1. Grosir")
    print("2. Keranjang Belanja")
    print("3. Transaksi")
    print("4. Logout")
    opsi_customer = input("Pilih menu opsi yang tersedia diatas [1/2/3/4]: ")
    if opsi_customer == "1":
        topMessage("GROSIR")
        Checkout()
        kembaliKeMenu(menuCustomer)
    elif opsi_customer == "2":
        topMessage("KERANJANG BELANJA")
        listKeranjangBelanja()
        menuKeranjang()
    elif opsi_customer == "3":
        topMessage("RIWAYAT TRANSAKSI")
        menuTransaksi()
    elif opsi_customer == "4":
        opsiLogout(menuCustomer, "customer")
    else:
        print("\n!! Pilihan tidak valid. Silahkan coba lagi. !!\n")
        return menuCustomer()
    
# FUNGSI CHECKOUT 
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
        
# LIST KERANJANG BELANJA
def listKeranjangBelanja():
    print(f"{'No':<4} {'Nama Produk':<30}{'Harga':>12}")
    print("-"*50) 
    if not Keranjang_Belanja:
        print("Keranjang belanja kosong.")
        kembaliKeMenu(menuCustomer)
    else:
        total = 0
        for i, (product_id, jumlah) in enumerate(Keranjang_Belanja.items(), 1):
            nama = Grosir[product_id]['nama']
            harga = Grosir[product_id]['harga']
            subtotal = harga * jumlah
            total += subtotal
            print(f"{i:<4} {nama:<30} {jumlah:>3}  Rp.{subtotal:>9,}")
        print("-"*50)
        print(f"{'Total pembayaran:':<35} Rp.{total:>9,}")
        menuKeranjang()
        
# MENU KERANJANG
def menuKeranjang():
    
    print("\nMenu Keranjang Belanja:")
    print("1. Lanjut ke Pembayaran")
    print("2. Hapus Produk dari Keranjang")
    print("3. Kembali ke menu awal")
    menu_checkout = input("\nPilih menu opsi yang tersedia diatas [1/2/3]: ")
    if menu_checkout == "1":
        print("\nLanjut ke pembayaran...\n")
        opsiPembayaran()
    elif menu_checkout == "2":
        opsiHapusDariKeranjang()
    elif menu_checkout == "3":
        print("\nKembali ke menu awal..\n")
        menuCustomer()
    else:
        print("\n!! Pilihan tidak valid. Silahkan coba lagi. !!\n")
        return menuKeranjang()
    
# OPSI PEMBAYARAN CUSTOMER
def opsiPembayaran():
    try:
        not Keranjang_Belanja
    except ValueError:
        print("Keranjang belanja kosong.")
        kembaliKeMenu(menuCustomer)
 
    opsi_beli = input("\nApakah anda mau melakukan transaksi? [y/n]: ")
    if opsi_beli == 'y' or opsi_beli == 'Y':
        print("\nBerhasil melakukan pembelian! Terima kasih telah berbelanja di KlikCodemaret.\n")
        Riwayat_Transaksi.append(Keranjang_Belanja.copy())
        Keranjang_Belanja.clear()
        print("Kembali ke menu customer...\n")
        menuCustomer()
    elif opsi_beli == 'n' or opsi_beli == 'N':
        print("\nTransaksi dibatalkan. Kembali ke menu customer...\n")
        menuCustomer()
    else:
        print("\n!! Tolong ikuti instruksi yang tersedia. Silahkan coba lagi. !!\n")
        return opsiPembayaran()
    
# OPSI HAPUS DARI KERANJANG
def opsiHapusDariKeranjang():
    print("\nHapus produk dari keranjang belanja...\n")
    if not Keranjang_Belanja:
        print("Keranjang belanja kosong.")
        kembaliKeMenu(menuCustomer)
    else:
        items = list(Keranjang_Belanja.items())
        for no_id, (id_produk, jumlah) in enumerate(items, 1):
            nama = Grosir[id_produk]['nama']
            harga = Grosir[id_produk]['harga']
            print(f"{no_id}. {nama} x{jumlah} - Rp.{harga*jumlah:,}")
        hapus_produk = input("\nMasukkan nomor produk yang ingin dihapus: ")
        if hapus_produk.isdigit():
            hapus_noId = int(hapus_produk)
            if 1 <= hapus_noId <= len(items):
                id_produk_to_remove = items[hapus_noId - 1][0]
                del Keranjang_Belanja[id_produk_to_remove]
                print("\n- Produk berhasil dihapus dari keranjang belanja.")
                opsiLagi(menuKeranjang, "Hapus produk lagi dari keranjang?", opsiHapusDariKeranjang)
            else:
                print("\n!! Nomor produk tidak valid. Silahkan coba lagi. !!\n")
                return opsiHapusDariKeranjang()
        else:
            print("\n! Tolong ikuti instruksi yang tersedia. Silahkan coba lagi.\n")
            return opsiHapusDariKeranjang()
        
# MENU TRANSAKSI CUSTOMER
def menuTransaksi():
    if not Riwayat_Transaksi:
        print("Belum ada transaksi.")
        kembaliKeMenu(menuCustomer)
    else:
        for t_idx, transaksi in enumerate(Riwayat_Transaksi, 1):
            print(f"\nTransaksi {t_idx}:")
            print(f"{'No':<4} {'Nama Produk':<30}{'Jumlah':>8}{'Subtotal':>14}")
            print('-'*60)
            total_t = 0
            for j, (product_id, jumlah) in enumerate(transaksi.items(), 1):
                nama = Grosir.get(product_id, {}).get('nama', '<produk dihapus>')
                harga = Grosir.get(product_id, {}).get('harga', 0)
                subtotal = harga * jumlah
                total_t += subtotal
                print(f"{j:<4} {nama:<30}{jumlah:>8} Rp.{subtotal:>11,}")
            print('-'*60)
            print(f"{'Total transaksi:':<46} Rp.{total_t:>8,}\n")
        kembaliKeMenu(menuCustomer)
