"""
karakter.py
Pilih peran (Admin / Customer) sebelum memasuki aplikasi.
Melakukan import lokal untuk menghindari import cycle saat modul dipanggil.
"""

def pilihKarakter():
    """Membiarkan user memilih peran dan mengarahkan alur program.

    Import dilakukan di dalam fungsi agar modul-modul menu tidak diimpor
    saat file ini diimport, mengurangi kemungkinan circular import.
    """
    from autentikasi_register import Registrasi
    from admin1 import menuAdmin
    from customer1 import menuCustomer
    print("\nPilih karakter anda:")
    print('1. Admin')
    print('2. Customer')
    pilihan_karakter = input("\nPilih opsi diatas sebelum memasuki program [1/2]: ")
    if pilihan_karakter == '1':
        Registrasi(menuAdmin)
        return menuAdmin()
    elif pilihan_karakter == '2':
        Registrasi(menuCustomer)
        return menuCustomer()
    else:
        print("\n!! Pilihan tidak valid. Silahkan coba lagi. !!")
        return pilihKarakter()