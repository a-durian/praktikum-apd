def kembaliKeMenu(menuAwalnya):
    input_kembali = input("\nMasukkan [0] untuk kembali ke menu awal: ")
    if input_kembali == '0':
        print("kembali ke menu awal...\n")
        menuAwalnya()
    else:
        print("\n!! Tolong ikuti instruksi yang tersedia. Silahkan coba lagi. !!\n")
        kembaliKeMenu(menuAwalnya)