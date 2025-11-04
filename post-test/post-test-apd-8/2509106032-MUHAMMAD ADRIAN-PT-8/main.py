"""
main.py
Entrypoint sederhana untuk menjalankan aplikasi KlikCodemaret.
Memanggil `pilihKarakter` setelah membersihkan terminal dan menampilkan header.
"""

from os import system, name

def clear():
    """Bersihkan terminal (cross-platform: Windows / Unix)."""
    _ = system('cls' if name == 'nt' else 'clear')

from helperss import topMessage
from karakter import pilihKarakter

if __name__ == "__main__":
    clear()
    topMessage("SELAMAT DATANG DI KLIKCODEMARET")
    pilihKarakter()
