from Menu_Admin.Menu import menuAdmin
from Menu_Customer.Menu import menuCustomer
from Modular.Registrasi import Registrasi


# FUNGSI PILIH KARAKTER
def pilihKarakter():
    print("\nPilih karakter anda:")
    print('1. Admin')
    print('2. Customer')
    pilihan_karakter = input("\nPilih opsi diatas sebelum memasuki program [1/2]: ")
    if pilihan_karakter == '1':
        Registrasi(menuAdmin)
        menuAdmin()
    elif pilihan_karakter == '2':
        Registrasi(menuCustomer)
        menuCustomer()
    else:
        print("\n!! Pilihan tidak valid. Silahkan coba lagi. !!")
        pilihKarakter()