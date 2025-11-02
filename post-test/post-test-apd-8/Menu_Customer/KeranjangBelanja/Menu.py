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