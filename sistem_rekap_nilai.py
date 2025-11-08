print('===== PROGRAM SISTEM NILAI RAPOR =====')

data_siswa = [] 

jumlah_siswa = int(input('Masukkan Jumlah Siswa: ')) 
for i in range (jumlah_siswa): 
    print(f'Masukkan data untuk siswa ke {i+1}')
    nama_siswa = input('Nama: ')
    mtk = int(input('Nilai Matematika: ')) 
    fisika = int(input('Nilai Fisika: '))
    kimia= int(input('Nilai Kimia: '))
    biologi = int(input('Nilai Biologi: '))
    rata_rata = (mtk + fisika + kimia + biologi)/4  
    data_siswa.append((nama_siswa, rata_rata)) 
print('===== HASIL RATA-RATA NILAI =====')
for nama_siswa, rata_rata in data_siswa: 
    print(f'{nama_siswa} : {rata_rata}')