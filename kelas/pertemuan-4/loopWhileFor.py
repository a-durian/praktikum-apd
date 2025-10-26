# for i in range(10):
#     print(i + 1)
    
# [0,2,3,4,,6,7,8,9]

# for i in range(1,11,2):
#     print(i)
# for loop untuk list
# nama =['bakil', 'diftya', 'anugerah']
# for nama in range(4):
#     print(nama)
    
# WHILE LOOP
# jawab= 'ya'
# hitung=0
# while (jawab == 'ya'):
#     hitung += 1
#     jawab = input("Ulangi Lagi?: ")
    
# print(f"total jawab ya = {hitung}")

# cuaca = "hujan"
# while (cuaca == "hujan" or cuaca =="Hujan"):
#     print ("Jangan keluar rumah")
#     cuaca = input("Apa cuaca saat ini: ")

# print("Pergi keluar rumah.")

# angka = 10
# while (angka > 1):
#     print(angka)
#     angka -= 2

# NESTED LOOP

# for i in range(1,5):
#     for j in range(1,5): 
#         print (f"{i} x {j} = {i * j}")
#     print()

# BREAK

# angka = [2,5,8,12,15,7,20]

# print("Mencari angka yang lebih besar dari 10...")

# for i in angka:
#     print(f"Memerika angka {i}")
#     if i > 10: 
#         print(f"{i} lebih besar dari 10")
#         break
# print("Program selesai")

# for i in range(1,11):
#     if i % 2 == 0:
#         continue
#     print(f"Angka ditemukan yaitu : {i}")
# print("Program selesai")

# LIST COMPREHENSION

# kuadrat = [i**2 for i in range(1,6)]
# print(kuadrat)

# angka_genap = [x for x in range (1,11) if x%2==0]
# print(angka_genap)
# print()
# for x in range(1,11):
#     if x%2 == 0:
#         print (x)

# angka_ganjil = [x for x in range(1,11) if x%2 != 0]
# print(angka_ganjil)
# for i in range(0,6):
    # print("*" * i)
    # print("*" * (6 - i))
