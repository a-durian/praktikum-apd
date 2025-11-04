from main import pilihKarakter
# FUNGSI TOP MESSAGE
def topMessage(topMessage):
    msgLong = ("="*21 + f" {topMessage} " + "="*21)
    print("="*len(msgLong))
    print(msgLong)
    print("="*len(msgLong))
    
# FUNGSI KEMBALI KE MENU AWAL
def kembaliKeMenu(menuAwalnya):
    input_kembali = input("\nMasukkan [0] untuk kembali ke menu awal: ")
    if input_kembali == '0':
        print("kembali ke menu awal...\n")
        menuAwalnya()
    else:
        print("\n!! Tolong ikuti instruksi yang tersedia. Silahkan coba lagi. !!\n")
        kembaliKeMenu(menuAwalnya)
        
# FUNGSI OPSI MENGULANG LAGI ATAU KEMBALI KE MENU AWAL
def opsiLagi(kembali, outputLagi, fungsiKembali):
    opsi_lagi = input(f"{outputLagi} [y/n]: ")
    if opsi_lagi == "y" or opsi_lagi == "Y":
        return fungsiKembali()
    elif opsi_lagi == "n" or opsi_lagi == "N":
        print("\nKembali ke menu awal..\n")
        kembali()
    else:
        print("\n!! Input tidak valid. Coba lagi !!\n")
        opsiLagi(kembali, outputLagi, fungsiKembali)
        
# FUNGSI OPSI LOGOUT
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
