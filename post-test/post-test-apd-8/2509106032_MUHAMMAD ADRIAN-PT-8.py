# IMPORT CLS/CLEAR TERMINAL
from os import system, name
from time import sleep
if name == 'nt':
    _ = system('cls')
else:
    _ = system('clear')

# IMPORT REGISTRASI LOGIN
from Modular.Registrasi import Registrasi
from Adds.Headline import topMessage

# DICTIONARY PRODUK
# Grosir = {
#     1: {"nama": "Roti Tawar", "harga": 12000},
#     2: {"nama": "Konohamie Mi Instan Goreng", "harga": 3200},
#     3: {"nama": "Konohamie Mi Instan Kari Ayam", "harga": 3200},
#     4: {"nama": "Geng-Geng Wafer Chocolate", "harga": 9900},
#     5: {"nama": "Silver King", "harga": 25000},
#     6: {"nama": "Lolari Sweat", "harga": 8000},
#     7: {"nama": "Bad Day", "harga": 13000},
#     8: {"nama": "Konohamilk", "harga": 14000},
#     9: {"nama": "Youzone", "harga": 16000},
#     10: {"nama": "Beras 5KG", "harga": 77000}
# }

# Keranjang_Belanja = {}
# Riwayat_Transaksi = []

# FUNGSI TOP MESSAGE
# def topMessage(topMessage):
#     msgLong = ("="*21 + f" {topMessage} " + "="*21)
#     print("="*len(msgLong))
#     print(msgLong)
#     print("="*len(msgLong))
# # FUNGSI PILIH KARAKTER
# def pilihKarakter():
#     print("\nPilih karakter anda:")
#     print('1. Admin')
#     print('2. Customer')
#     pilihan_karakter = input("\nPilih opsi diatas sebelum memasuki program [1/2]: ")
#     if pilihan_karakter == '1':
#         Registrasi(menuAdmin)
#         menuAdmin()
#     elif pilihan_karakter == '2':
#         Registrasi(menuCustomer)
#         menuCustomer()
#     else:
#         print("\n!! Pilihan tidak valid. Silahkan coba lagi. !!")
#         pilihKarakter()
# FUNGSI REGISTRASI DAN LOGIN ADMIN
# def Registrasi(fungsiMenu):
#     def Login(fungsiMenu):
#         percobaan = 5
#         while percobaan > 0:
#             loginNama = input("Nama: ")
#             loginPW = input("Password: ")
#             if loginNama == inputNama and loginPW == inputPW:
#                 print("\nLogin berhasil!\n")
#                 fungsiMenu()
#             else:
#                 percobaan -= 1
#                 print(f"\n!! Login gagal! Sisa percobaan: {percobaan} !!")
#         print("\nAnda telah melakukan 5 percobaan login yang gagal. Program dihentikan.")
#         raise SystemExit(1)
#     try:
#         inputNama = input("Masukkan Nama: ")
#         inputPW = input("Masukkan Password: ")
#         if inputNama == "" or inputPW == "":
#             raise ValueError("\n!! Nama atau Password tidak boleh kosong. Silahkan coba lagi. !!\n")
#         elif (len(str(inputPW))) < 8:
#             raise ValueError("\n!! Password harus terdiri dari minimal 8 karakter. Silahkan coba lagi. !!\n")
#     except ValueError as e:
#         print(e)
#         return Registrasi(fungsiMenu)
#     finally:
#         print("\nSign up berhasil! silahkan login dengan akun anda:")
#         return Login(fungsiMenu)
# FUNGSI MENU ADMIN
# def menuAdmin():
#     topMessage("Menu: Admin")
#     print('1. Produk yang tersedia')
#     print('2. Tambah Produk')
#     print('3. Hapus Produk')
#     print('4. Logout')
#     pilihanAdmin = input("\nPilih menu opsi yang tersedia diatas [1/2/3/4]: ")
#     if pilihanAdmin == "1":
#         topMessage("GROSIR")
#         listGrosir()
#         kembaliKeMenu(menuAdmin)
#     elif pilihanAdmin == "2":
#         topMessage("TAMBAH PRODUK")
#         tambahProduk()
#     elif pilihanAdmin == "3":
#         topMessage("HAPUS PRODUK")
#         hapusProduk()
#     elif pilihanAdmin == "4":
#         opsiLogout(menuAdmin, "admin")
#     else:
#         print("\n!! Pilihan tidak valid. Silahkan coba lagi. !!\n")
#         return menuAdmin()
# FUNGSI LIST GROSIR
# def listGrosir():
#     print(f"{'No':<4} {'Nama Produk':<30}{'Harga':>12}")
#     print("-"*50)
#     for i, produk in Grosir.items():
#         print(f"{i:<4} {produk['nama']:<30} Rp.{produk['harga']:>9,}")
#     print("-"*50)
# FUNGSI TAMBAH PRODUK
# def tambahProduk():
#     nama_produk_baru = input("\nMasukkan nama produk baru: ")
#     harga_produk_baru = input("Masukkan harga produk baru: Rp.")
#     try:
#         harga_produk_baru = int(harga_produk_baru)
#     except ValueError:
#         print("\n!! Harga produk harus berupa angka. Silahkan coba lagi. !!\n")
#         tambahProduk()
#     if nama_produk_baru == "" or nama_produk_baru == " " or  harga_produk_baru == "" or harga_produk_baru == " " :
#         print("\n!! Nama atau harga produk tidak boleh kosong. Silahkan coba lagi. !!\n")
#     elif harga_produk_baru <= 0:
#         print("\n!! Harga produk harus lebih dari 0. Silahkan coba lagi. !!\n")
#     id_baru = max(Grosir.keys()) + 1
#     Grosir[id_baru] = {"nama": nama_produk_baru, "harga": harga_produk_baru}
#     print(f"\nProduk '{nama_produk_baru}' dengan harga Rp.{harga_produk_baru:,} berhasil ditambahkan dengan ID {id_baru}!")
#     opsiLagi(menuAdmin, "Tambah produk lagi?", tambahProduk)
# FUNGSI HAPUS PRODUK
# def hapusProduk():
#     listGrosir()
#     print("\nMasukkan [0] untuk kembali ke menu awal")
#     def inputHapusProduk():
#         inputHapus = input("Pilih nomor produk yang ingin dihapus: ")
        
#         try:
#             intInputHapus = int(inputHapus)
#         except ValueError:
#             print("\n!! Input harus nomor. Silahkan coba lagi. !!\n")
#             inputHapusProduk()
#         if intInputHapus == 0:
#             print("\nKembali ke menu awal...\n")
#             menuAdmin()
#         elif intInputHapus not in Grosir:
#             print("\n!! Nomor produk tidak ditemukan. Silahkan coba lagi. !!\n")
#             inputHapusProduk() 
        
#         del Grosir[intInputHapus]
#         # Mengatur ulang nomor urut
#         grosirBaru = {}
#         idBaru = 1
#         for _, produk in sorted(Grosir.items()):
#             grosirBaru[idBaru] = produk
#             idBaru += 1
#         # Update dictionary Grosir dengan nomor yang baru
#         Grosir.clear()
#         Grosir.update(grosirBaru)
#         print("\nProduk berhasil dihapus.")
#         opsiLagi(menuAdmin, "Hapus produk lagi?", hapusProduk)
#     inputHapusProduk()
# FUNGSI KEMBALI KE MENU AWAL
# def kembaliKeMenu(menuAwalnya):
#     input_kembali = input("\nMasukkan [0] untuk kembali ke menu awal: ")
#     if input_kembali == '0':
#         print("kembali ke menu awal...\n")
#         menuAwalnya()
#     else:
#         print("\n!! Tolong ikuti instruksi yang tersedia. Silahkan coba lagi. !!\n")
#         kembaliKeMenu(menuAwalnya)
# FUNGSI ALUR CUSTOMER
# def menuCustomer():
#     topMessage("Menu: Customer")
#     print("1. Grosir")
#     print("2. Keranjang Belanja")
#     print("3. Transaksi")
#     print("4. Logout")
#     opsi_customer = input("Pilih menu opsi yang tersedia diatas [1/2/3/4]: ")
#     if opsi_customer == "1":
#         topMessage("GROSIR")
#         Checkout()
#         kembaliKeMenu(menuCustomer)
#     elif opsi_customer == "2":
#         topMessage("KERANJANG BELANJA")
#         listKeranjangBelanja()
#         menuKeranjang()
#     elif opsi_customer == "3":
#         topMessage("RIWAYAT TRANSAKSI")
#         menuTransaksi()
#     elif opsi_customer == "4":
#         opsiLogout(menuCustomer, "customer")
#     else:
#         print("\n!! Pilihan tidak valid. Silahkan coba lagi. !!\n")
#         return menuCustomer()
# # FUNGSI CHECKOUT KE KERANJANG BELANJA
# def Checkout():
#     print("")
#     listGrosir()
#     print("\nMasukkan [0] untuk kembali ke menu awal\n")
#     menu_grosir_input = input("Silahkan pilih nomor produk untuk dimasukkan ke keranjang belanja: ")
#     if menu_grosir_input.isdigit():
#         menu_grosir = int(menu_grosir_input)
#         if menu_grosir == 0:
#             print("\nKembali ke menu awal...\n")
#             menuCustomer()
#         elif menu_grosir in Grosir:
#             jumlah_input = input("Masukkan jumlah [1/2/...]: ")
#             if jumlah_input == "":
#                 jumlah = 1
#             elif jumlah_input.isdigit() and int(jumlah_input) > 0:
#                 jumlah = int(jumlah_input)
#             else:
#                 print("\nJumlah tidak valid. Silahkan coba lagi.\n")
#                 Checkout()
#             Keranjang_Belanja[menu_grosir] = Keranjang_Belanja.get(menu_grosir, 0) + jumlah
#             nama = Grosir[menu_grosir]['nama']
#             harga = Grosir[menu_grosir]['harga']
#             print(f"\n+ {nama} x{jumlah} seharga Rp.{harga:,} berhasil ditambahkan ke keranjang belanja.\n")
#             opsiLagi(menuCustomer, "Checkout produk lagi?", Checkout)
#         else:
#             print("\nProduk tidak ditemukan. Silahkan coba lagi.\n")
#             Checkout()
#     else:
#         print("\n!! Input harus berupa nomor. Silahkan coba lagi. !!\n")
#         Checkout()
# # LIST KERANJANG BELANJA
# def listKeranjangBelanja():
#     print(f"{'No':<4} {'Nama Produk':<30}{'Harga':>12}")
#     print("-"*50) 
#     if not Keranjang_Belanja:
#         print("Keranjang belanja kosong.")
#         kembaliKeMenu(menuCustomer)
#     else:
#         total = 0
#         for i, (product_id, jumlah) in enumerate(Keranjang_Belanja.items(), 1):
#             nama = Grosir[product_id]['nama']
#             harga = Grosir[product_id]['harga']
#             subtotal = harga * jumlah
#             total += subtotal
#             print(f"{i:<4} {nama:<30} {jumlah:>3}  Rp.{subtotal:>9,}")
#         print("-"*50)
#         print(f"{'Total pembayaran:':<35} Rp.{total:>9,}")
#         menuKeranjang()
# MENU KERANJANG
# def menuKeranjang():
    
#     print("\nMenu Keranjang Belanja:")
#     print("1. Lanjut ke Pembayaran")
#     print("2. Hapus Produk dari Keranjang")
#     print("3. Kembali ke menu awal")
#     menu_checkout = input("\nPilih menu opsi yang tersedia diatas [1/2/3]: ")
#     if menu_checkout == "1":
#         print("\nLanjut ke pembayaran...\n")
#         opsiPembayaran()
#     elif menu_checkout == "2":
#         opsiHapusDariKeranjang()
#     elif menu_checkout == "3":
#         print("\nKembali ke menu awal..\n")
#         menuCustomer()
#     else:
#         print("\n!! Pilihan tidak valid. Silahkan coba lagi. !!\n")
#         return menuKeranjang()
# # OPSI PEMBAYARAN CUSTOMER
# def opsiPembayaran():
#     try:
#         not Keranjang_Belanja
#     except ValueError:
#         print("Keranjang belanja kosong.")
#         kembaliKeMenu(menuCustomer)
 
#     opsi_beli = input("\nApakah anda mau melakukan transaksi? [y/n]: ")
#     if opsi_beli == 'y' or opsi_beli == 'Y':
#         print("\nBerhasil melakukan pembelian! Terima kasih telah berbelanja di KlikCodemaret.\n")
#         Riwayat_Transaksi.append(Keranjang_Belanja.copy())
#         Keranjang_Belanja.clear()
#         print("Kembali ke menu customer...\n")
#         menuCustomer()
#     elif opsi_beli == 'n' or opsi_beli == 'N':
#         print("\nTransaksi dibatalkan. Kembali ke menu customer...\n")
#         menuCustomer()
#     else:
#         print("\n!! Tolong ikuti instruksi yang tersedia. Silahkan coba lagi. !!\n")
#         return opsiPembayaran()
# # OPSI HAPUS DARI KERANJANG
# def opsiHapusDariKeranjang():
#     print("\nHapus produk dari keranjang belanja...\n")
#     if not Keranjang_Belanja:
#         print("Keranjang belanja kosong.")
#         kembaliKeMenu(menuCustomer)
#     else:
#         items = list(Keranjang_Belanja.items())
#         for no_id, (id_produk, jumlah) in enumerate(items, 1):
#             nama = Grosir[id_produk]['nama']
#             harga = Grosir[id_produk]['harga']
#             print(f"{no_id}. {nama} x{jumlah} - Rp.{harga*jumlah:,}")
#         hapus_produk = input("\nMasukkan nomor produk yang ingin dihapus: ")
#         if hapus_produk.isdigit():
#             hapus_noId = int(hapus_produk)
#             if 1 <= hapus_noId <= len(items):
#                 id_produk_to_remove = items[hapus_noId - 1][0]
#                 del Keranjang_Belanja[id_produk_to_remove]
#                 print("\n- Produk berhasil dihapus dari keranjang belanja.")
#                 opsiLagi(menuKeranjang, "Hapus produk lagi dari keranjang?", opsiHapusDariKeranjang)
#             else:
#                 print("\n!! Nomor produk tidak valid. Silahkan coba lagi. !!\n")
#                 return opsiHapusDariKeranjang()
#         else:
#             print("\n! Tolong ikuti instruksi yang tersedia. Silahkan coba lagi.\n")
#             return opsiHapusDariKeranjang()
# MENU TRANSAKSI CUSTOMER
# def menuTransaksi():
#     if not Riwayat_Transaksi:
#         print("Belum ada transaksi.")
#         kembaliKeMenu(menuCustomer)
#     else:
#         for t_idx, transaksi in enumerate(Riwayat_Transaksi, 1):
#             print(f"\nTransaksi {t_idx}:")
#             print(f"{'No':<4} {'Nama Produk':<30}{'Jumlah':>8}{'Subtotal':>14}")
#             print('-'*60)
#             total_t = 0
#             for j, (product_id, jumlah) in enumerate(transaksi.items(), 1):
#                 nama = Grosir.get(product_id, {}).get('nama', '<produk dihapus>')
#                 harga = Grosir.get(product_id, {}).get('harga', 0)
#                 subtotal = harga * jumlah
#                 total_t += subtotal
#                 print(f"{j:<4} {nama:<30}{jumlah:>8} Rp.{subtotal:>11,}")
#             print('-'*60)
#             print(f"{'Total transaksi:':<46} Rp.{total_t:>8,}\n")
#         kembaliKeMenu(menuCustomer)
# # FUNGSI OPSI MENGULANG LAGI ATAU KEMBALI KE MENU AWAL
# def opsiLagi(kembali, outputLagi, fungsiKembali):
#     opsi_lagi = input(f"{outputLagi} [y/n]: ")
#     if opsi_lagi == "y" or opsi_lagi == "Y":
#         return fungsiKembali()
#     elif opsi_lagi == "n" or opsi_lagi == "N":
#         print("\nKembali ke menu awal..\n")
#         kembali()
#     else:
#         print("\n!! Input tidak valid. Coba lagi !!\n")
#         opsiLagi(kembali, outputLagi, fungsiKembali)
# FUNGSI OPSI LOGOUT
# def opsiLogout(insertMenu, menuApa):
#     inputLogout = input("\nApakah anda yakin untuk logout dari akun anda? [y/n]: ")
#     if inputLogout == "y" or inputLogout == "Y":
#         print("\nLogout berhasil. Kembali ke halaman awal..\n")
#         pilihKarakter()
#     elif inputLogout == "n" or inputLogout == "N":
#         print(f"\nKembali ke menu {menuApa}..\n")
#         insertMenu()
#     else:
#         print("\n!! Input tidak valid. Silahkan coba lagi. !!")
#         return opsiLogout(insertMenu)

# MAIN PROGRAM
topMessage("SELAMAT DATANG DI KLIKCODEMARET")
pilihKarakter()
