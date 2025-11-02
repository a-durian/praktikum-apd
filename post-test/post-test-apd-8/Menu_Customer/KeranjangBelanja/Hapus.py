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