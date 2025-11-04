# FUNGSI REGISTRASI DAN LOGIN ADMIN
def Registrasi(fungsiMenu):
    def Login(fungsiMenu):
        percobaan = 5
        while percobaan > 0:
            loginNama = input("Nama: ")
            loginPW = input("Password: ")
            if loginNama == inputNama and loginPW == inputPW:
                print("\nLogin berhasil!\n")
                fungsiMenu()
            else:
                percobaan -= 1
                print(f"\n!! Login gagal! Sisa percobaan: {percobaan} !!")
        print("\nAnda telah melakukan 5 percobaan login yang gagal. Program dihentikan.")
        raise SystemExit(1)
    try:
        inputNama = input("Masukkan Nama: ")
        inputPW = input("Masukkan Password: ")
        if inputNama == "" or inputPW == "":
            raise ValueError("\n!! Nama atau Password tidak boleh kosong. Silahkan coba lagi. !!\n")
        elif (len(str(inputPW))) < 8:
            raise ValueError("\n!! Password harus terdiri dari minimal 8 karakter. Silahkan coba lagi. !!\n")
    except ValueError as e:
        print(e)
        return Registrasi(fungsiMenu)
    finally:
        print("\nSign up berhasil! silahkan login dengan akun anda:")
        return Login(fungsiMenu)