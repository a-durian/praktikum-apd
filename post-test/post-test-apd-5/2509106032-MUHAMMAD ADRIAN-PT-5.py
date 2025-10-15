from os import system, name
from time import sleep
if name == 'nt':
    _ = system('cls')
else:
    _ = system('clear')
    
# LIST PRODUK
Grosir = [('Roti Tawar', 12000),  
           ('Konohamie Mi Instan Goreng', 3200), 
           ('Konohamie Mi Instan Kari Ayam', 3200),
           ('Geng-Geng Wafer Chocolate', 9900),
           ('Silver King', 25000),
           ('Lolari Sweat', 8000),  
           ('Bad Day', 13000), 
           ('Konohamilk', 14000), 
           ('Youzone', 16000), 
           ('Beras 5KG', 77000),
           ('Minyak Goreng 2L', 42200), 
           ('XYZ Sambal Trasi 180G', 23600),
           ('Konohafood Saus Sambal 335G', 16400),
           ('Bumbu Nasi Goreng Sajikau 20G', 2700),
           ('Bumbu Racik Nasi Goreng Isi 3', 7000),
           ('Lifebuoy Sabun Mandi', 6300), 
           ('Leg & Shoulders', 35500), 
           ('SensiDyne Pasta Gigi', 25000),
           ('Shampo Zinc', 22400),
           ('Facial Tissue Isi 100', 10600)]
Keranjang_Belanja = []
Riwayat_Transaksi = []
welcome_to_codemaret = ("="*20 + " Selamat Datang di KLikCodemaret " + "="*20)

while True:
    print("="*len(welcome_to_codemaret))
    print(welcome_to_codemaret)
    print("="*len(welcome_to_codemaret))
    print('1. Admin')
    print('2. Customer')
    pilihan_karakter = input("\nPilih opsi diatas sebelum memasuki program [1/2]: ")
    
    if pilihan_karakter == '1':# ALUR ADMIN
        print("Silahkan registrasi diri anda terlebih dahulu.")
        while True:
            nama_admin = input("Masukkan Nama: ")
            pw_admin = input("Masukkan Password: ")
            if nama_admin == "" or pw_admin == "":
                print("\nNama atau Password tidak boleh kosong! Silahkan coba lagi.\n")
            else:
                print("\nSign up berhasil! silahkan login dengan akun anda:")
                percobaan = 5
                while percobaan > 0:
                    login_NA = input("Nama: ")
                    login_PA = input("Password: ")

                    if login_NA == nama_admin and  login_PA == pw_admin:
                        selamat_datang = (f"="*20 + " Selamat Datang {nama_admin} " + "="*20)
                        print("="*len(selamat_datang))
                        print(selamat_datang)
                        print("="*len(selamat_datang))
                        while True:
                            print('\nMenu:')
                            print('1. Produk yang tersedia')
                            print('2. Tambah Produk')
                            print('3. Hapus Produk')
                            pilihan_admin = input("\nPilih menu opsi yang tersedia diatas [1/2/3]: ")
                            if pilihan_admin == '1':
                                while True:
                                    print("="*21 + " Grosir " + "="*21)
                                    print(f"{'No':<4} {'Nama Produk':<30}{'Harga':>12}")
                                    print("-"*50)
                                    for i, (produk, harga) in enumerate(Grosir, 1):
                                        print(f"{i:<4} {produk:<30} Rp.{harga:>9,}")
                                    input_stok = input("\nMasukkan [0] untuk kembali ke menu awal: ")
                                    if input_stok == '0':
                                        print("kembali ke menu awal...")
                                        break
                                    else:
                                        print("\n! Tolong ikuti instruksi yang tersedia. Silahkan coba lagi.\n")
                            elif pilihan_admin == '2':
                                print("="*61)
                                print("="*22 + " Tambah Produk " + "="*22)
                                print("="*61)
                                while True:
                                    nama_produk_baru = input("Masukkan nama produk baru: ")
                                    input_harga_produk_baru = (input("Masukkan harga produk baru: Rp."))
                                    if input_harga_produk_baru.isdigit():
                                        harga_produk_baru = int(input_harga_produk_baru)
                                        Grosir.append((nama_produk_baru, harga_produk_baru))
                                        print("\nProduk berhasil ditambahkan.")
                                        
                                        opsi_lagi = input("Tambah produk lagi? [y/n]: ")
                                        if opsi_lagi == 'y' or opsi_lagi == 'Y':
                                            print("\nAnda memilih untuk menambahkan produk lagi...\n")
                                        elif opsi_lagi == 'n' or opsi_lagi == 'N':
                                            print('\nkembali ke menu awal...\n')
                                            break
                                        else:
                                            print("\n! Tolong ikuti instruksi yang tersedia. Silahkan coba lagi.\n")
                                    else:
                                        print("\nHarga produk harus berupa angka. Silahkan coba lagi.\n")
                            elif pilihan_admin == '3':
                                while True:
                                    print("="*61)
                                    print("="*22 + " Hapus Produk " + "="*22)
                                    print("="*61)
                                    print(f"{'No':<4} {'Nama Produk':<30}{'Harga':>12}")
                                    print("-"*61)
                                    for i, (produk, harga) in enumerate(Grosir, 1):
                                        print(f"{i:<4} {produk:<30} Rp.{harga:>9,}")
                                    print("\nMasukkan [0] untuk kembali ke menu awal\n")
                                    hapus_produk_input = input("Pilih nomor produk yang ingin dihapus: ")
                                    if hapus_produk_input == '0':
                                        print("\nKembali ke menu awal...\n")
                                        break
                                    elif hapus_produk_input.isdigit() and int(hapus_produk_input) <= len(Grosir):
                                        hapus_produk = int(hapus_produk_input) - 1
                                        del Grosir[hapus_produk]
                                        print("\nProduk berhasil dihapus.")
                                    
                                    else:
                                        print("\n! Tolong ikuti instruksi yang tersedia. Silahkan coba lagi.\n")
                            else:
                                print("\n! Tolong ikuti instruksi yang tersedia. Silahkan coba lagi.\n")
                    else:
                        percobaan -= 1
                        if percobaan == 0:
                            print("nLogin gagal! Program dihentikan.\n")
                            break
                        elif login_NA == "" or login_PA == "" or nama_admin == "" or pw_admin == "":
                            print("\nNama atau Password tidak boleh kosong! Silahkan coba lagi.")
                            print(f"Tersisa {percobaan}x Percobaaan.\n")
                        else:
                            print("\nNama atau Password yang anda masukkan salah! Silahkan coba lagi.")
                            print(f"Tersisa {percobaan}x Percobaaan.\n")
                
    
    elif pilihan_karakter == '2':# ALUR CUSTOMER/PENGGUNA BIASA
        print("="*len(welcome_to_codemaret))
        print(welcome_to_codemaret)
        print("="*len(welcome_to_codemaret))
        print("Anda belum mempunyai akun, silahkan sign up terlebih dahulu.")
        while True:
            nama_customer = input("Masukkan Username: ")
            pw_customer = input("Masukkan Password: ")
            if nama_customer == "" or pw_customer == "":
                print("\nUsername atau Password tidak boleh kosong! Silahkan coba lagi.\n")
            else:
                print("\nSign up berhasil! silahkan login dengan akun anda:")
                percobaan = 5
                while percobaan > 0:
                    login_NC = input("Username: ")
                    login_PC = input("Password: ")
                
                    if login_NC == nama_customer and  login_PC == pw_customer:
                        print("="*61)
                        print(f"="*6 + " Login berhasil! Selamat datang di KlikCodemaret " + "="*6)
                        print("="*61)
                        while True:
                            print("\nMenu:")
                            print("1. Grosir")
                            print("2. Keranjang Belanja")
                            print("3. Transaksi")
                            opsi_customer = input("Pilih menu opsi yang tersedia diatas [1/2/3]: ")
                            if opsi_customer == '1':
                                while True:
                                    print("="*21 + " Grosir " + "="*21)
                                    print(f"{'No':<4} {'Nama Produk':<30}{'Harga':>12}")
                                    print("-"*50)
                                    for i, (produk, harga) in enumerate(Grosir, 1):
                                        print(f"{i:<4} {produk:<30} Rp.{harga:>9,}")
                                    print("\nMasukkan [0] untuk kembali ke menu awal\n")
                                    menu_grosir_input = input("Silahkan pilih produk untuk dimasukkan ke keranjang belanja: ")
                                    if menu_grosir_input.isdigit() and int(menu_grosir_input) <= 20:
                                        menu_grosir = int(menu_grosir_input)
                                        if menu_grosir == 0:
                                            print("\nKembali ke menu awal...\n")
                                            break
                                        elif menu_grosir in range(1, 21):
                                            index_produk = menu_grosir - 1
                                            produk_terpilih, harga_terpilih = Grosir[index_produk]
                                            print(f"\n+ {produk_terpilih} seharga Rp.{harga_terpilih:,} berhasil ditambahkan ke keranjang belanja.\n")
                                            Keranjang_Belanja.append((produk_terpilih, harga_terpilih))
                                    else:
                                        print("\n! Tolong ikuti instruksi yang tersedia. Silahkan coba lagi.\n")
                            elif opsi_customer == '2':
                                
                                print("="*15 + " Keranjang Belanja " + "="*15)
                                print(f"{'No':<4} {'Nama Produk':<30}{'Harga':>12}")
                                print("-"*50)
                                for i, (produk, harga) in enumerate(Keranjang_Belanja, 1):
                                    print(f"{i:<4} {produk:<30} Rp.{harga:>9,}")
                                print("-"*50)
                                print(f"{'Total pembayaran:':<35} Rp.{sum(harga for _, harga in Keranjang_Belanja):>9,}")

                                while True:
                                    print("\nMenu Keranjang Belanja:")
                                    print("1. Lanjut ke Pembayaran")
                                    print("2. Hapus Produk dari Keranjang")
                                    print("3. Kembali ke menu awal")
                                    menu_checkout = input("\nPilih menu opsi yang tersedia diatas [1/2/3]: ")
                                    if menu_checkout == '1':
                                        print("\nLanjut ke pembayaran...\n")
                                        for i, (produk, harga) in enumerate(Keranjang_Belanja, 1):
                                            print(f"{i:<4} {produk:<30} Rp.{harga:>9,}")
                                        while True: 
                                            opsi_beli = input("\nApakah anda mau melakukan transaksi? [y/n]")
                                            if opsi_beli == 'y' or opsi_beli == 'Y':  
                                                print("\nBerhasil melakukan pembelian! Terima kasih telah berbelanja di KlikCodemaret.\n")
                                                Riwayat_Transaksi.extend(Keranjang_Belanja)
                                                Keranjang_Belanja.clear()
                                                print("Kembali ke menu keranjang belanja...\n")
                                                break
                                            elif opsi_beli == 'n' or opsi_beli == 'N':
                                                print("\nTransaksi dibatalkan. Kembali ke menu keranjang belanja...\n")
                                                break
                                            else:
                                                print("\n! Tolong ikuti instruksi yang tersedia. Silahkan coba lagi.\n")
                                    elif menu_checkout == '2':
                                        print("\nHapus produk dari keranjang belanja...\n")
                                        if not Keranjang_Belanja:
                                            print("Keranjang belanja kosong.")
                                        else:
                                            for i, (produk, harga) in enumerate(Keranjang_Belanja, 1):
                                                print(f"{i}. {produk} - Rp.{harga:,}")
                                            while True:
                                                hapus_produk = input("\nMasukkan nomor produk yang ingin dihapus: ")
                                                if hapus_produk.isdigit():
                                                    hapus_produk = int(hapus_produk)
                                                    if 1 <= hapus_produk <= len(Keranjang_Belanja):
                                                        del Keranjang_Belanja[hapus_produk - 1]
                                                        print("\n- Produk berhasil dihapus dari keranjang belanja.")
                                                        for i, (produk, harga) in enumerate(Keranjang_Belanja, 1):
                                                            print(f"{i}. {produk} - Rp.{harga:,}")
                                                        print("\nKembali ke menu Keranjang Belanja...")
                                                        break
                                                    else:
                                                        print("Nomor produk tidak valid. Silahkan coba lagi.\n")
                                                else:
                                                    print("\n! Tolong ikuti instruksi yang tersedia. Silahkan coba lagi.\n")
                                        
                                    elif menu_checkout == '3':
                                        print("kembali ke menu awal...")
                                        break
                                    else:
                                        print("\n! Tolong ikuti instruksi yang tersedia. Silahkan coba lagi.\n")
                            elif opsi_customer == '3':
                                print("-"*50)
                                print("="*15 + " Riwayat Transaksi " + "="*15)
                                print(f"{'No':<4} {'Nama Produk':<30}{'Harga':>12}")
                                print("-"*50)
                                for i, (produk, harga) in enumerate(Riwayat_Transaksi, 1):
                                    print(f"{i:<4} {produk:<30} Rp.{harga:>9,}")
                                print("-"*50)
                                while True:
                                    opsi_kembali = input("\nMasukkan [0] untuk kembali ke menu awal: ")
                                    if opsi_kembali == '0':
                                        print("\nKembali ke menu awal...\n")
                                        break
                                    else:
                                        print("\n! Tolong ikuti instruksi yang tersedia. Silahkan coba lagi.\n")
                            else:
                                print(" \n! Tolong ikuti instruksi yang tersedia. Silahkan coba lagi.\n")
                                    
                    else:
                        percobaan -= 1
                        if percobaan == 0:
                            print("Login gagal! Program dihentikan.")
                            break
                        elif login_NC == "" or login_PC == "":
                            print("\nUsername atau Password tidak boleh kosong! Silahkan coba lagi.")
                            print(f"Tersisa {percobaan}x Percobaaan.\n")
                        else:
                            print("\nUsername atau Password yang anda masukkan salah! Silahkan coba lagi.")
                            print(f"Tersisa {percobaan}x Percobaaan.\n")
    else:
        print("\n! Tolong ikuti instruksi yang tersedia. Silahkan coba lagi.\n")