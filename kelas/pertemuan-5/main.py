# LIST
# mataKuliah = ['APD', 'Kalkulus', 'Orsikom']
# mataKuliah_1 = []
# membaca list
# print(mataKuliah[1:2])

# print(mataKuliah[-2])
# print('')
# print(mataKuliah[1:3:2])
# print('')
# mataKuliah.append('Matdis')
# print(mataKuliah)

# //// APPEND & INSERT ////
# mataKuliah.append('Matematika')
# mataKuliah.insert(2, 'Bahasa Inggris')
# print(mataKuliah)

# /// MENGGANTI LANGSUNG ///
# studyclub = ["Data Science", "Robotics", "Multimedia", "Network"]
# print(studyclub)

# studyclub[2] = 'AI'
# print(studyclub)

# /// DELETE ///

# del nama_list[indeks]
# matakuliah = ['PTI', 'APD','Kalkulus','Diskrit']
# print(matakuliah)

# del matakuliah[2]
# print(matakuliah)

# nama_list.remove(nilai)
# matakuliah.remove('Kalkulus')
# print(matakuliah)

# POP
# hapus = matakuliah.pop(2)
# print(hapus)
# ambil_matkul = matakuliah.pop(2)
# print(matakuliah)
# print(ambil_matkul)

#STEP
# matakuliah = ['PTI', 'APD','Kalkulus','Diskrit','Bahasa Inggris',
# 'Orsikom','Basis Data']
# print(matakuliah[1:6:3])

# genap = [2, 4, 6, 8, 10]
# ganjil = [1,3,7,9]

# gabungan = genap + ganjil
# print (gabungan)
# matakuliah = ['PTI', 'APD','Kalkulus','Diskrit','Bahasa Inggris', 'Orsikom','Basis Data'] 
# # for i in matakuliah:
# #     print(f'mata kuliah: {i}')

# for index, i in enumerate(matakuliah): 
#     print(index,i)
    
# ///NESTED LIST///
# kelas = [
# ["Ridho", "Lian", "Nabil"], #index 0
# ["Daffa", "Dante", "Santoso"], #index 1
# ["Pernanda", "Riyadi", "Ahnaf"], #index 2
# ]
# # print(kelas[0])
# # print(kelas[0][1])
# # print(kelas[2][1])

# kelas[1].insert(1, "Abdul")#menambahkan di nested list
# print (kelas)

# for i in kelas:
#     for nama in i:
    #    print(nama)
    
# /////TUPLE/////

#mendefinisikan tuple
anggota = ("riyadi", 20, True, 3.96, ["APD",25],("samarinda",12))
print(anggota[4][0])

studyclub = ("Data Science", "Robotics", "Multimedia", "Network")
liststudy=list(studyclub)

tuplestudy= tuple(liststudy)
liststudy[1]= 'WEB'
print(f'Ini tuple: {studyclub}')
print(f'Ini list: {liststudy}')
print(f'Ini tuple lagi: {tuplestudy}')

liststudy.insert = (1, "OOH") 
