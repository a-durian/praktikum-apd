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