
# FUNGSI KEMBALI KE MENU

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
        
# FUNGSI MENU TRANSAKSI

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