kuat = sedang = lemah = sangat_lemah = 0
hasil_kategori = [] 
jumlah_uji = int(input('Jumlah kata sandi yang akan diuji: '))
for i in range(jumlah_uji):
    sandi = input(f'Kata sandi ke-{i+1}: ')
    
    skor = 0  

    # Panjang karakter
    if len(sandi) >= 8:
        skor += 2

    # Huruf besar
    huruf_besar = False
    for huruf in sandi:
        if huruf.isupper():
            huruf_besar = True
            break
    if huruf_besar:
        skor += 1

    # Huruf kecil
    huruf_kecil = False
    for huruf in sandi:
        if huruf.islower():
            huruf_kecil = True
            break
    if huruf_kecil:
        skor += 1

    # Angka
    angka = False
    for huruf in sandi:
        if huruf.isdigit():
            angka = True
            break
    if angka:
        skor += 1

    # Simbol 
    daftar_simbol = "!@#$%^&*()"
    simbol = False
    for huruf in sandi:
        if huruf in daftar_simbol:
            simbol = True
            break
    if simbol:
        skor += 2

    # Kategori berdasarkan skor
    if 6 <= skor <= 7:
        kategori = "Kuat"
        kuat += 1
    elif 4 <= skor <= 5:
        kategori = "Sedang"
        sedang += 1
    elif 2 <= skor <= 3:
        kategori = "Lemah"
        lemah += 1
    else:
        kategori = "Sangat Lemah"
        sangat_lemah += 1

    hasil_kategori.append(f"{sandi} - {kategori}") 


for hasil in hasil_kategori:
    print(hasil)
print("Rekapitulasi:")
print(f"Kuat: {kuat}")
print(f"Sedang: {sedang}")
print(f"Lemah: {lemah}")
print(f"Sangat Lemah: {sangat_lemah}")
