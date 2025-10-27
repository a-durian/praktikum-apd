# while True:
#     try:
#         umur = int(input("masukkan umur: "))
#         if umur < 0:
#             raise ValueError("umur tidak boleh kurang dari nol")
#     except ValueError as e:
#         print(e)
#     # else:
#     #     print(f"umur yang dimasukkan adalah {umur}")
#     # finally:
#     #     print("Selesai")
    
# while True:
#     try:
#         nama = input("Masukkan nama: ")
#         if nama == "" or nama == " ":
#             raise ValueError("Nama tidak boleh kosong")
#     except ValueError as e:
#         print(e)
#     # else:
#     #     print(f"Nama yang dimasukkan adalah {nama}")
#     # finally:
#     #     print("Selesai")
    
# try:
#     buat_pw = input("Buat Password: ")
#     if len(buat_pw) < 8:
#         raise ValueError("Password harus terdiri dari minimal 8 karakter")
# except ValueError as e:
#     print(e)

# if inputHapus == str():
#     print("\n!! Input harus nomor. Silahkan coba lagi. !!\n")
# elif inputHapus not in Grosir:
#     print("\n!! Nomor produk tidak ditemukan. Silahkan coba lagi. !!\n")
 try:
            inputHapus = int(input("Pilih nomor produk yang ingin dihapus: "))
            if not isinstance(inputHapus, int):
                raise ValueError("\n!! Input harus nomor. Silahkan coba lagi. !!\n")
            elif inputHapus not in Grosir:
                raise ValueError("\n!! Nomor produk tidak ditemukan. Silahkan coba lagi. !!\n")
        except ValueError as e:
            print(e)
            inputHapusProduk()
        finally:
            if inputHapus == 0:
                print("\nKembali ke menu awal...\n")
                menuAdmin()
            else:
                del Grosir[inputHapus]
                # Mengatur ulang nomor urut
                grosirBaru = {}
                idBaru = 1
                for _, produk in sorted(Grosir.items()):
                    grosirBaru[idBaru] = produk
                    idBaru += 1
                # Update dictionary Grosir dengan nomor yang baru
                Grosir.clear()
                Grosir.update(grosirBaru)
                print("\nProduk berhasil dihapus.")
                opsiLagi(menuAdmin, "Hapus produk lagi?", hapusProduk)