# IMPORT CLS/CLEAR TERMINAL
from os import system, name
if name == 'nt':
    _ = system('cls')
else:
    _ = system('clear')

# IMPORT REGISTRASI LOGIN
from Headline import topMessage
from modulOpsi import pilihKarakter

# MAIN PROGRAM
topMessage("SELAMAT DATANG DI KLIKCODEMARET")
pilihKarakter()
