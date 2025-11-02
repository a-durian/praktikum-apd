# LIST KERANJANG BELANJA
def listKeranjangBelanja():
    print(f"{'No':<4} {'Nama Produk':<30}{'Harga':>12}")
    print("-"*50) 
    if not Keranjang_Belanja:
        print("Keranjang belanja kosong.")
        kembaliKeMenu(menuCustomer)
    else:
        total = 0
        for i, (product_id, jumlah) in enumerate(Keranjang_Belanja.items(), 1):
            nama = Grosir[product_id]['nama']
            harga = Grosir[product_id]['harga']
            subtotal = harga * jumlah
            total += subtotal
            print(f"{i:<4} {nama:<30} {jumlah:>3}  Rp.{subtotal:>9,}")
        print("-"*50)
        print(f"{'Total pembayaran:':<35} Rp.{total:>9,}")
        menuKeranjang()