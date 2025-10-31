def fitur_pembeli():
    print('===== SELAMAT DATANG DI TOKO AGRO SEJAHTERA =====')
    mulai = int(input('Ketik [1] untuk melihat daftar barang yang tersedia: '))
    beli = int(input('Ketik [2] untuk mulai membeli produk: '))


def main():
    pembeli = int(input('Ketik [1] Jika Anda Seorang Pembeli: '))
    petani = int(input('Ketik [2] Jika Anda Seorang Petani: '))
    if pembeli == 1:
        fitur_pembeli()
