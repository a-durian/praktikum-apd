"""
tambahan.py
Kumpulan fungsi utilitas yang digunakan di banyak tempat:
- `kembaliKeMenu` : meminta user menekan 0 untuk kembali ke menu sebelumnya
- `opsiLagi`      : menanyakan apakah user ingin mengulangi aksi (y/n)
- `opsiLogout`    : konfirmasi logout dan kembali ke menu awal
"""


# FUNGSI KEMBALI KE MENU AWAL
def kembaliKeMenu(menuAwalnya):
    """Minta input [0] untuk kembali ke fungsi/menu yang diberikan.

    Parameter:
    - menuAwalnya: callable (mis. menuAdmin atau menuCustomer) yang akan dipanggil jika user menekan 0.
    """
    input_kembali = input("\nMasukkan [0] untuk kembali ke menu awal: ")
    if input_kembali == '0':
        print("kembali ke menu awal...\n")
        return menuAwalnya()
    else:
        print("\n!! Tolong ikuti instruksi yang tersedia. Silahkan coba lagi. !!\n")
        return kembaliKeMenu(menuAwalnya)
        

# FUNGSI OPSI MENGULANG LAGI ATAU KEMBALI KE MENU AWAL
def opsiLagi(kembali, outputLagi, fungsiKembali):
    """Tanyakan [y/n] kepada user. Jika 'y' panggil `fungsiKembali`, jika 'n' panggil `kembali`.

    Parameter:
    - kembali: callable yang menandakan menu utama (mis. menuAdmin/menuCustomer)
    - outputLagi: string pesan yang ditampilkan sebelum prompt
    - fungsiKembali: callable yang dipanggil bila user memilih ingin mengulangi
    """
    opsi_lagi = input(f"{outputLagi} [y/n]: ")
    if opsi_lagi == "y" or opsi_lagi == "Y":
        return fungsiKembali()
    elif opsi_lagi == "n" or opsi_lagi == "N":
        print("\nKembali ke menu awal..\n")
        return kembali()
    else:
        print("\n!! Input tidak valid. Coba lagi !!\n")
        return opsiLagi(kembali, outputLagi, fungsiKembali)
        

# FUNGSI OPSI LOGOUT
def opsiLogout(insertMenu, menuApa):
    """Tanyakan konfirmasi logout lalu kembali ke `pilihKarakter` jika disetujui."""
    from karakter import pilihKarakter
    inputLogout = input("\nApakah anda yakin untuk logout dari akun anda? [y/n]: ")
    if inputLogout == "y" or inputLogout == "Y":
        print("\nLogout berhasil. Kembali ke halaman awal..\n")
        return pilihKarakter()
    elif inputLogout == "n" or inputLogout == "N":
        print(f"\nKembali ke menu {menuApa}..\n")
        return insertMenu()
    else:
        print("\n!! Input tidak valid. Silahkan coba lagi. !!")
        return opsiLogout(insertMenu)
