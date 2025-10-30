# num = int("42") # 42
# name = str(123) # "123"
# data = list("abc") # ['a', 'b', 'c']
# data = dict(a=1, b=2) # {'a': 1, 'b': 2}
# print(type(num))

# listAngka = [1,2, 45, 7, 8, 9, 12, 13, 45, 230]

# print(len(listAngka)) 
# print(sorted(listAngka))

# for i, v in enumerate(['a','b']):
#     print(i, v) # 0 a , 1 b
# len([10, 20, 30]) # 3
# list(map(str, [1,2,3])) # ['1', '2', '3']
# sorted([3, 1, 2]) # [1, 2, 3]
# list(zip([1,2],['a','b'])) # [(1,'a'), (2,'b')]

# x = 42
# def fungsi():
    # x = 10
    # y = 20
    # z = 30
    # print(globals()['x']) # mendapatkan isi dari variabel x (global)
    # print(locals()['x']) # mendapatkan isi dari variabel x (lokal)
    # print(locals()) # {'x': 10, 'y': 20, 'z': 30}
# fungsi()

# ///METHOD///
# pilihan = input("apakah anda ingin lanjut? (ya/tidak): ").upper()
# if pilihan == "YA":
#     print("Program berlanjut")
# elif pilihan == "tidak":
#     print("Program dihentikan")
# else:
#     print("pilihan salah kocak")


# ///LIBRARY///
# 3 CARA PANGGIL LIBRARY
# import math
# # /
# from math import sqrt
# # /
# import math as terserah

# print(math.sqrt(16)) # 4.0
# print(math.factorial(4))
# # /
# # print(sqrt(25)) # 5.0
# # /
# print(terserah.sqrt(36)) # 6.0

# # RANDOM
# import random

# # print(random.randint(1, 5)) # menghasilkan angka random dari 1 - 4

# # pilih_acak = ["pisang", "rambutan", "manggis"]
# # acak = "apcb"
# # print(random.choice(pilih_acak)) # memilih 1 element secara acak pada list
# # print(random.choice(acak)) # memilih 1 karakter acak pada string

# # # memasukkan satu persatu nilai dari kumpulan_angka
# # # ke dalam variabel hasil dengan isinya 4 karakter hasil randomize
# # kumpulan_angka = "1234567890"
# # # hasil = ""
# # for i in range(4):
# #     hasil += random.choice(kumpulan_angka)
# # print(hasil)

# acak_kartu = ["1 wajik", "3 wajik", "5 wajik"]
# random.shuffle(acak_kartu) # kocok kartu, output berupa urutan list yang berubah
# print(acak_kartu)

# from datetime import datetime
# while True:
#     print(datetime.now())

import inquirer
pertanyaan = [
inquirer.List(
'size',
message="What size do you need?",
choices=['Jumbo', 'Large', 'Standard', 'Medium', 'Small', 'Micro'],
),
]
# mendapatkan jawaban
answer = inquirer.prompt(pertanyaan)
print(answer) # Output dalam bentuk Dictionary {'size': 'Large'}
print(answer['size']) # Ambil value dari key 'size' (Large)