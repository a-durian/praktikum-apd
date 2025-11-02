# IMPORT DICT N LIST
from dictnlist import Grosir

# FUNGSI LIST GROSIR

def listGrosir():
    print(f"{'No':<4} {'Nama Produk':<30}{'Harga':>12}")
    print("-"*50)
    for i, produk in Grosir.items():
        print(f"{i:<4} {produk['nama']:<30} Rp.{produk['harga']:>9,}")
    print("-"*50)