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

# FUNGSI MENU KERANJANG BELANJA
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