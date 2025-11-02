

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