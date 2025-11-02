from Adds.dictnlist import Grosir, Riwayat_Transaksi
from Modular.OpsiKembali import kembaliKeMenu
from Menu_Customer.Menu import menuCustomer
# FUNGSI MENU TRANSAKSI

def menuTransaksi():
    if not Riwayat_Transaksi:
        print("Belum ada transaksi.")
        kembaliKeMenu(menuCustomer)
    else:
        for t_idx, transaksi in enumerate(Riwayat_Transaksi, 1):
            print(f"\nTransaksi {t_idx}:")
            print(f"{'No':<4} {'Nama Produk':<30}{'Jumlah':>8}{'Subtotal':>14}")
            print('-'*60)
            total_t = 0
            for j, (product_id, jumlah) in enumerate(transaksi.items(), 1):
                nama = Grosir.get(product_id, {}).get('nama', '<produk dihapus>')
                harga = Grosir.get(product_id, {}).get('harga', 0)
                subtotal = harga * jumlah
                total_t += subtotal
                print(f"{j:<4} {nama:<30}{jumlah:>8} Rp.{subtotal:>11,}")
            print('-'*60)
            print(f"{'Total transaksi:':<46} Rp.{total_t:>8,}\n")
        kembaliKeMenu(menuCustomer)