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
    
try:
    buat_pw = input("Buat Password: ")
    if len(buat_pw) < 8:
        raise ValueError("Password harus terdiri dari minimal 8 karakter")
except ValueError as e:
    print(e)
