from os import system, name
from time import sleep

if name == 'nt':
    _ = system('cls')
else:
    _ = system('clear')
pilihan_karakter = '1' or '2'
while pilihan_karakter != '1' or pilihan_karakter != '2':
    print('1. Admin')
    print('2. Customer')
    pilihan_karakter = input("\nPilih opsi diatas sebelum memasuki program [1/2]: ")

    if pilihan_karakter == '1':
        print('Opsi admin:')
        print('1. Stok Produk')
        print('2. Harga Promo')
        print('3. ')
        break
    elif pilihan_karakter == '2':
        print("="*61)
        print("============== Selamat Datang di KLikCodemaret ==============")
        print("="*61)
        print("Anda belum mempunyai akun, silahkan sign up terlebih dahulu.")
        nama_customer = input("Masukkan Nama: ")
        pw_customer = input("Masukkan Password: ")
        print("\nSign up berhasil! silahkan login dengan akun anda:")
        
        percobaan = 5
        while percobaan > 0:
            login_NC = input("Nama: ")
            login_PC = input("Password: ")
        
            if login_NC == nama_customer and  login_PC == pw_customer:
                print("="*57)
                print(f"=====Login berhasil! Selamat datang di KlikCodemaret=====")
                print("="*57)
                print("1. Grosir")
                print("2. Keranjang Belanja")
                print("3. Transaksi")
                opsi_customer = input("Pilih opsi yang tersedia diatas [1/2/3]: ")
                if opsi_customer == '1':
                    print("===Grosir===")
                    print()#LIST PRODUK-PRODUK
                    input("Pilih Kategori Belanja [1/2/3/4]: ")
                elif opsi_customer == '2':
                    print("===Keranjang Belanja===")
                    print()#LIST KERANJANG BELANJA(Berikan output 'kosong' bila belum ada produk didalam keranjang)
                elif opsi_customer == '3':
                    print("===Transaksi===")
                break
            elif login_NC != nama_customer or login_PC != pw_customer:
                percobaan -= 1
                if percobaan == 0:
                    print("Login gagal! Program dihentikan.")
                    break
                else:
                    print("\nNama atau Password yang anda masukkan salah! Silahkan coba lagi.")
                    print(f"Tersisa {percobaan}x Percobaaan.\n")
        break
    else:
        print("\nTolong ikuti instruksi yang tersedia. Coba lagi.\n")
print("\nTembus kebawah!")