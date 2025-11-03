from prettytable import PrettyTable
tabel = PrettyTable()

tabel.field_names = ["No.", "Produk", "Jumlah", "Harga"]
tabel.add_row([1, "Pensil", 10, 2000])
tabel.add_row([2, "Buku", 5, 15000])
tabel.add_row([3, "Penghapus", 7, 3000])
print(tabel)

tabel.align["Produk"] = "l"
tabel.align["Jumlah"] = "m" 
tabel.align["Harga"] = "r"

print(tabel)