def opsiLogout(insertMenu, menuApa):
    inputLogout = input("\nApakah anda yakin untuk logout dari akun anda? [y/n]: ")
    if inputLogout == "y" or inputLogout == "Y":
        print("\nLogout berhasil. Kembali ke halaman awal..\n")
        pilihKarakter()
    elif inputLogout == "n" or inputLogout == "N":
        print(f"\nKembali ke menu {menuApa}..\n")
        insertMenu()
    else:
        print("\n!! Input tidak valid. Silahkan coba lagi. !!")
        return opsiLogout(insertMenu)