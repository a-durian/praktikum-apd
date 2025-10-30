from modular.autentikasi import login
from modular.create import tambah_data_siswa
print("Selamat datang di aplikasi!")
# Menggunakan modul login
if login("admin", "123"):
    print("Login berhasil!")
    # Menggunakan modul create
    tambah_data_siswa({"nama": "Budi", "nilai": 90})
else:
    print("Login gagal!")