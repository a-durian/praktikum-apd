"""
data_dictlist.py
Menyimpan struktur data global yang digunakan oleh program:
- `Grosir`: dictionary produk (id -> {nama, harga})
- `Keranjang_Belanja`: dictionary sementara untuk keranjang (product_id -> jumlah)
- `Riwayat_Transaksi`: list berisi snapshot keranjang untuk setiap transaksi
"""

# DICTIONARY PRODUK
Grosir = {
    1: {"nama": "Roti Tawar", "harga": 12000},
    2: {"nama": "Konohamie Mi Instan Goreng", "harga": 3200},
    3: {"nama": "Konohamie Mi Instan Kari Ayam", "harga": 3200},
    4: {"nama": "Geng-Geng Wafer Chocolate", "harga": 9900},
    5: {"nama": "Silver King", "harga": 25000},
    6: {"nama": "Lolari Sweat", "harga": 8000},
    7: {"nama": "Bad Day", "harga": 13000},
    8: {"nama": "Konohamilk", "harga": 14000},
    9: {"nama": "Youzone", "harga": 16000},
    10: {"nama": "Beras 5KG", "harga": 77000}
}

Keranjang_Belanja = {}  # product_id -> jumlah
# Riwayat_Transaksi menyimpan snapshot sebagai struktur:
# {"waktu": datetime, "items": {product_id: jumlah, ...}}
Riwayat_Transaksi = []  # list of transaksi snapshot