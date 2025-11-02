def tambahProduk():
    nama_produk_baru = input("\nMasukkan nama produk baru: ")
    harga_produk_baru = input("Masukkan harga produk baru: Rp.")
    try:
        harga_produk_baru = int(harga_produk_baru)
    except ValueError:
        print("\n!! Harga produk harus berupa angka. Silahkan coba lagi. !!\n")
        tambahProduk()
    if nama_produk_baru == "" or nama_produk_baru == " " or  harga_produk_baru == "" or harga_produk_baru == " " :
        print("\n!! Nama atau harga produk tidak boleh kosong. Silahkan coba lagi. !!\n")
    elif harga_produk_baru <= 0:
        print("\n!! Harga produk harus lebih dari 0. Silahkan coba lagi. !!\n")
    id_baru = max(Grosir.keys()) + 1
    Grosir[id_baru] = {"nama": nama_produk_baru, "harga": harga_produk_baru}
    print(f"\nProduk '{nama_produk_baru}' dengan harga Rp.{harga_produk_baru:,} berhasil ditambahkan dengan ID {id_baru}!")
    opsiLagi(menuAdmin, "Tambah produk lagi?", tambahProduk)