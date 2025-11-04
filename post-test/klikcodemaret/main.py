from os import system, name
def clear():
    _ = system('cls' if name == 'nt' else 'clear')

from utils import topMessage
from admin import menuAdmin
from customer import menuCustomer
from autentikasi import Registrasi

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

# MAIN PROGRAM
# topMessage("SELAMAT DATANG DI KLIKCODEMARET")
# pilihKarakter()
if __name__ == "__main__":
    clear()
    topMessage("SELAMAT DATANG DI KLIKCODEMARET")
    pilihKarakter()
