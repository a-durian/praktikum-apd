# SET & DICTIONARY
# Membuat SET
# buah = {"apel", "jeruk", "mangga", "apel"}

# # for i in buah:
# #     print(i, end=' ')
    
#     angka = (1, 2, 3, 4, 5, 1, 2, 3)
#     angka_set = set(angka)
#     print(angka_set)
#     for i in angka_set:
#         print(i, end=' ')

# DICTIONARY
# daftar_buku = {
#     "Buku1" : "Bumi Manusia",
#     "Buku2" : "Laut Bercerita"
# }

# print(daftar_buku["Buku1"])

Biodata = {
"Nama" : "Muhammad Adrian",
"NIM" : 2509106032,
"KRS" : ["Pemrograman Web", "Struktur Data", "Basis Data"],
"Mahasiswa_Aktif" : True,
"Social Media" : {"Twitter" : "daffahrhap", "Instagram" : "daffahrhap"}
}

# print(Biodata)
# for i, j in Biodata.items():
#     print(i)
#     print(j)
    
# print(f"nama saya adalah {Biodata['Nama']}")
# print(f"Instagram : {Biodata['Social Media']['Instagram']}")
# print(f"nama saya adalah {Biodata.get["Nama"]}")#//(.get)//

# Film = {
# "Avenger Endgame" : "Action",
# "Sherlock Holmes" : "Mystery",
# "The Conjuring" : "Horror"
# }

# print(Film)
# # Tambah++
# Film["Zombie Land"] = "Comedy"
# Film.update({"The Conjuring" : "Comedy Horror"})#Ganti key dari The Conjuring
# Film.update({"Doraemon" : "Anime"})#Tambah key baru
# print(Film)

# del Film["Sherlock Holmes"]#Hapus key Sherlock Holmes
# print(Film)

# hapus = Film.pop("Avenger Endgame")#Hapus key Avenger Endgame
# print(Film)
# print(hapus)#Menampilkan key yang dihapus
# Film.clear()#Menghapus semua isi dictionary
# print(Film)

# Musik = {
#     "The Chainsmoker": ["All we Know", "The Paris"],
#     "Alan Walker": ["Alone", "Lily"],
#     "Neffex": ["Best of Me",['tes','halo'], "Memories"],
#     'Paramore' : ["Misery Business", "Ain't It Fun", 
#                 ['All We Know Is Falling',['Here We Go Again', 'My Heart']],'This Is Why' ]
# }

# print(Musik['Paramore'][2][1][1])
# print(Musik['Neffex'][1][0])
# print(Musik['Paramore'][2][1][0])

# angka = {}
# angka = set()
# print(type(angka))

a = {10, 11, 12}
b = {11, 13, 14}
# c = a.union(b)
# d = a.intersection(b)# irisan
# e = a.difference(b)# selisih
# f = b.difference(a)# selisih
# g = a | b# union
# h = a & b# intersection

# print(c)

# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81
# }
# # 
# print("Nilai : ", Nilai.setdefault("Kimia", 70))

mahasiswa = [["Adrian", 2509106032], ["Daffa", 2509106033], ["Rhap", 2509106034]]

for i in mahasiswa:
    for j in i:
        print(j)
        
print(dict(mahasiswa))
print(mahasiswa[0][1])