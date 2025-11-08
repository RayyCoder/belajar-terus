print('Selamat Datang di RayStore dan Selamat Berbelanja!')
print('Produk yang Tersedia: \nIphone 20 = Rp 20.000 \nMacbook Air M4 = Rp 40.000 \nSosis Kanzler = Rp 35.000')

produk = {
"Iphone 20": 20000,
"Macbook Air M4": 40000,
"Sosis Kanzler": 35000
}

keranjang = {} # Membuat variabel keranjang untuk menampung barang-barang yang ingin dibeli
subtotal = 0 

# Membuat sistem perhitungan
while True:
    barang = input('Masukkan nama produk yang ingin dibeli: ').title() # Membuat variabel "barang" untuk menginputkan nama produk, title digunakan agar inputan user selalu sesuai dengan yang ada di Dictionary
    jumlah = int(input('Beli berapa? ')) # Variabel jumlah untuk menginputkan berapa banyak produk yang ingin dibeli
    total_barang = produk[barang] * jumlah # Menghitung total harga setiap barang sesuai dengan jumlahnya

    # Sistem Keranjang
    if barang in keranjang: # Jika barang sudah pernah ada di keranjang, barang yang sama akan ditambahkan jumlahnya 
        keranjang[barang] += jumlah
    else:
        keranjang[barang] = jumlah # Untuk barang berbeda yang belum pernah masuk keranjang
    
    # Menghitung Subtotal produk yang dibeli
    subtotal += total_barang 

    # Konfirmasi pesanan, apakah sudah cukup atau ingin menambah produk lain
    konfirmasi = input('Masukkan keranjang atau sudah cukup? [keranjang]/[cukup] ').lower()
    if konfirmasi == 'keranjang':
        print('Barang berhasil dimasukkan ke keranjang')
    else:
        break

# Biaya-biaya
ppn = int (subtotal * 12/100)
ongkir = 10000
total_akhir = subtotal + ppn + ongkir

# Mencetak Struk Belanja
print('===== STRUK BELANJA =====')
for barang, jumlah in keranjang.items(): # Menampilkan barang-barang yang ada didalam keranjang
    print(f'{barang} x{jumlah} = Rp {produk[barang] * jumlah}')
print('-----------------------')
print(f'Subtotal : Rp {subtotal}')
print(f'PPN (12%) : Rp {ppn}')
print(f'Ongkir : Rp {ongkir}')
print('-----------------------')
print(f'Total Akhir : Rp {total_akhir}')
print('Terimakasih Telah Berbelanja di RayStore!')