# Isi saldo tapi punya hutang
saldo_awal = input("saldo sekarang: ")
deposit = input("ingin deposit berapa: ")
hasil = int(saldo_awal) + int(deposit)

print("saldo akhir: " + str(hasil))

print('Hutang kamu: Rp 50.000')
print('saldo kamu sekarang Rp 5.000')
saldo_awal = 5000
deposit = int (input('Nominal deposit: '))
saldo_akhir = saldo_awal + deposit

Hutang = 50000
sisa_hutang = Hutang - saldo_akhir

if Hutang < int(saldo_akhir):
    print(f'deposit sukses, saldo kamu sekarang Rp {saldo_akhir}') 
elif Hutang == int(saldo_akhir):
    print('saldo 0')
else:
    print('deposit gagal, kamu masih punya hutang')
    print(f"hutang sekarang sisa: {sisa_hutang} rupiah")

# Syarat Pendaftaran
print('Syarat Pendaftaran')
usia = int(input('Berapa usia kamu? '))

if usia >= 18 and usia <=40:
    print('Selamat kamu boleh mendaftar')
elif usia >= 40 and usia <50:
    print('Kamu sudah tua tetapi masih boleh mendaftar')
elif usia >= 50:
    print('Kamu terlalu tua untuk mendaftar')
elif usia <=4:
    print('Kamu masih terlalu kecil untuk mendaftar')
else:
    print('Kamu belum boleh mendaftar')

# Konfirmasi kenyang lapar
respon = input('Apakah kamu lapar? (Iya/Tidak): ')

if respon == 'iya':
    print('Yasudah cepat makan sana')
    
# else:
    print('Mantap udah kenyang')
    pertanyaan = input('Abis makan apa? ')
    respon2 = input(f'Mantappp, enak ga {pertanyaan} nya? (enak/ga enak): ')
    if respon2 == 'enak':
        respon3 = input(f'Wih enak ya {pertanyaan} nya, beli dimana tuh?: ')
        if respon3 == 'rahasia':
            print('iya deh kalo ga mau kasi tau')
        else:
            print(f'Oke deh nanti aku beli di {respon3} juga buat makan malem')
    else:
        print('Waduh, yaudah jangan beli disana lagi')
