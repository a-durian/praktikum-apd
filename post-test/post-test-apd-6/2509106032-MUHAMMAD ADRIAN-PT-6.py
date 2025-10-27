from os import system, name
from time import sleep
if name == 'nt':
    _ = system('cls')
else:
    _ = system('clear')
    
# LIST PRODUK
Grosir = {
    1: {"nama": "Roti Tawar", "harga": 12000},
    2: {"nama": "Konohamie Mi Instan Goreng", "harga": 3200},
    3: {"nama": "Konohamie Mi Instan Kari Ayam", "harga": 3200},
    4: {"nama": "Geng-Geng Wafer Chocolate", "harga": 9900},
    5: {"nama": "Silver King", "harga": 25000},
    6: {"nama": "Lolari Sweat", "harga": 8000},
    7: {"nama": "Bad Day", "harga": 13000},
    8: {"nama": "Konohamilk", "harga": 14000},
    9: {"nama": "Youzone", "harga": 16000},
    10: {"nama": "Beras 5KG", "harga": 77000}
}

Keranjang_Belanja = {}
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
                            print('4. Logout ')
                            pilihan_admin = input("\nPilih menu opsi yang tersedia diatas [1/2/3]: ")
                            if pilihan_admin == '1':
                                while True:
                                    print("="*21 + " Grosir " + "="*21)
                                    print(f"{'No':<4} {'Nama Produk':<30}{'Harga':>12}")
                                    print("-"*50)
                                    for i, produk in Grosir.items():
                                        print(f"{i:<4} {produk['nama']:<30} Rp.{produk['harga']:>9,}")
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
                                    input_harga_produk_baru = input("Masukkan harga produk baru: Rp.")
                                    # validasi harga (harus angka positif)
                                    if input_harga_produk_baru.isdigit():
                                        harga_produk_baru = int(input_harga_produk_baru)
                                        # menentukan id prodk baru
                                        new_id = max(Grosir.keys(), default=0) + 1
                                        Grosir[new_id] = {"nama": nama_produk_baru, "harga": harga_produk_baru}
                                        print(f"\nProduk berhasil ditambahkan. ID={new_id} {nama_produk_baru} Rp.{harga_produk_baru:,}")

                                        opsi_lagi = input("Tambah produk lagi? [y/n]: ")
                                        if opsi_lagi.lower() == 'y':
                                            print("\nAnda memilih untuk menambahkan produk lagi...\n")
                                            continue
                                        elif opsi_lagi.lower() == 'n':
                                            print('\nkembali ke menu awal...\n')
                                            break
                                        else:
                                            print("\n! Tolong ikuti instruksi yang tersedia. Silahkan coba lagi.\n")
                                            break
                                    else:
                                        print("\nHarga produk harus berupa angka. Silahkan coba lagi.\n")
                            elif pilihan_admin == '3':
                                while True:
                                    print("="*61)
                                    print("="*22 + " Hapus Produk " + "="*22)
                                    print("="*61)
                                    print(f"{'No':<4} {'Nama Produk':<30}{'Harga':>12}")
                                    print("-"*61)
                                    for i, produk in Grosir.items():
                                        print(f"{i:<4} {produk['nama']:<30} Rp.{produk['harga']:>9,}")
                                    print("\nMasukkan [0] untuk kembali ke menu awal\n")
                                    hapus_produk_input = input("Pilih nomor produk yang ingin dihapus: ")
                                    if hapus_produk_input == '0':
                                        print("\nKembali ke menu awal...\n")
                                        break
                                    elif hapus_produk_input.isdigit():
                                        hapus_produk = int(hapus_produk_input)
                                        if hapus_produk in Grosir:
                                            del Grosir[hapus_produk]
                                            print("\nProduk berhasil dihapus.")
                                        else:
                                            print("\nNomor produk tidak ditemukan. Silahkan coba lagi.\n")
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
                                    for i, produk in Grosir.items():
                                        print(f"{i:<4} {produk['nama']:<30} Rp.{produk['harga']:>9,}")
                                    print("\nMasukkan [0] untuk kembali ke menu awal\n")
                                    menu_grosir_input = input("Silahkan pilih produk untuk dimasukkan ke keranjang belanja: ")
                                    if menu_grosir_input.isdigit():
                                        menu_grosir = int(menu_grosir_input)
                                        if menu_grosir == 0:
                                            print("\nKembali ke menu awal...\n")
                                            break
                                        if menu_grosir in Grosir:
                                            jumlah_input = input("Masukkan jumlah [default 1]: ")
                                            if jumlah_input == "":
                                                jumlah = 1
                                            elif jumlah_input.isdigit() and int(jumlah_input) > 0:
                                                jumlah = int(jumlah_input)
                                            else:
                                                print("\nJumlah tidak valid. Silahkan coba lagi.\n")
                                            Keranjang_Belanja[menu_grosir] = Keranjang_Belanja.get(menu_grosir, 0) + jumlah
                                            nama = Grosir[menu_grosir]['nama']
                                            harga = Grosir[menu_grosir]['harga']
                                            print(f"\n+ {nama} x{jumlah} seharga Rp.{harga:,} berhasil ditambahkan ke keranjang belanja.\n")
                                        else:
                                            print("\nProduk tidak ditemukan. Silahkan coba lagi.\n")
                                    else:
                                        print("\n! Tolong ikuti instruksi yang tersedia. Silahkan coba lagi.\n")
                            elif opsi_customer == '2':
                                
                                print("="*15 + " Keranjang Belanja " + "="*15)
                                print(f"{'No':<4} {'Nama Produk':<30}{'Harga':>12}")
                                print("-"*50)
                                if not Keranjang_Belanja:
                                    print("Keranjang belanja kosong.")
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

                                while True:
                                    print("\nMenu Keranjang Belanja:")
                                    print("1. Lanjut ke Pembayaran")
                                    print("2. Hapus Produk dari Keranjang")
                                    print("3. Kembali ke menu awal")
                                    menu_checkout = input("\nPilih menu opsi yang tersedia diatas [1/2/3]: ")
                                    if menu_checkout == '1':
                                        print("\nLanjut ke pembayaran...\n")
                                        for i, (product_id, jumlah) in enumerate(Keranjang_Belanja.items(), 1):
                                            nama = Grosir[product_id]['nama']
                                            harga = Grosir[product_id]['harga']
                                            subtotal = harga * jumlah
                                            total += subtotal
                                            print(f"{i:<4} {nama:<30} {jumlah:>3}  Rp.{subtotal:>9,}")
                                        print("-"*50)
                                        print(f"{'Total pembayaran:':<35} Rp.{total:>9,}")
                                        while True: 
                                            opsi_beli = input("\nApakah anda mau melakukan transaksi? [y/n]")
                                            if opsi_beli == 'y' or opsi_beli == 'Y':  
                                                print("\nBerhasil melakukan pembelian! Terima kasih telah berbelanja di KlikCodemaret.\n")
                                                Riwayat_Transaksi.append(Keranjang_Belanja.copy())
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
                                            items = list(Keranjang_Belanja.items())
                                            for no_id, (id_produk, jumlah) in enumerate(items, 1):
                                                nama = Grosir[id_produk]['nama']
                                                harga = Grosir[id_produk]['harga']
                                                print(f"{no_id}. {nama} x{jumlah} - Rp.{harga*jumlah:,}")
                                            while True:
                                                hapus_produk = input("\nMasukkan nomor item (1-based) yang ingin dihapus: ")
                                                if hapus_produk.isdigit():
                                                    hapus_noId = int(hapus_produk)
                                                    if 1 <= hapus_noId <= len(items):
                                                        id_produk_to_remove = items[hapus_noId - 1][0]
                                                        del Keranjang_Belanja[id_produk_to_remove]
                                                        print("\n- Produk berhasil dihapus dari keranjang belanja.")
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
                                if not Riwayat_Transaksi:
                                    print("Belum ada transaksi.")
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
                                        print(f"{'Total transaksi:':<46} Rp.{total_t:>11,}\n")
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