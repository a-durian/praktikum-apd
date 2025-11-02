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