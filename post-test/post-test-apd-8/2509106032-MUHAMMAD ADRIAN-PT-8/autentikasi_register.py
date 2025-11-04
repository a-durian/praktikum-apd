"""
autentikasi_register.py
Fungsi registrasi dan login sederhana untuk Admin dan Customer.

Cara kerja:
- `Registrasi(fungsiMenu)` meminta username dan password baru, melakukan validasi,
  lalu memanggil fungsi `Login` untuk proses autentikasi.
- `Login` memberi pengguna 5 percobaan untuk memasukkan kredensial yang sama seperti yang didaftarkan.
"""

def Registrasi(fungsiMenu):
    """Mendaftarkan akun sementara (disimpan di variabel lokal) lalu meminta login.

    Parameter:
    - fungsiMenu: callable yang akan dipanggil setelah login berhasil (mis. menuAdmin)
    """
    def Login(fungsiMenu):
        percobaan = 5
        # Perulangan login sebanyak percobaan yang diberikan
        while percobaan > 0:
            loginNama = input("Nama: ")
            loginPW = input("Password: ")
            if loginNama == inputNama and loginPW == inputPW:
                print("\nLogin berhasil!\n")
                return fungsiMenu()
            else:
                percobaan -= 1
                print(f"\n!! Login gagal! Sisa percobaan: {percobaan} !!")
        # Jika sudah habis percobaan, hentikan program
        print("\nAnda telah melakukan 5 percobaan login yang gagal. Program dihentikan.")
        raise SystemExit(1)

    try:
        inputNama = input("Masukkan Nama: ")
        inputPW = input("Masukkan Password: ")
        # Validasi input dasar
        if inputNama == "" or inputPW == "":
            raise ValueError("\n!! Nama atau Password tidak boleh kosong. Silahkan coba lagi. !!\n")
        elif (len(str(inputPW))) < 8:
            raise ValueError("\n!! Password harus terdiri dari minimal 8 karakter. Silahkan coba lagi. !!\n")
    except ValueError as e:
        # Jika validasi gagal, ulangi proses registrasi
        print(e)
        return Registrasi(fungsiMenu)
    finally:
        # Setelah registrasi selesai, arahkan user untuk login
        print("\nSign up berhasil! silahkan login dengan akun anda:")
        return Login(fungsiMenu)