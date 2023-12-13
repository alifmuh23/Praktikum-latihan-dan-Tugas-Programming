nim = [2,3,1,0,3,1,0,6,0]
print(nim)
# akses item
print('item indeks 0:',nim[0])
print('item indeks 3:',nim[3])
print('item indeks terakhir:',nim[len(nim)-1])
# akses indeks negatif
print('item indeks terakhir:',nim[-1])
print('item indeks pertama:',nim[-len(nim)])
print('item indeks 3: [-6] ',nim[-6])
print('item indeks 5: [-4] ',nim[-4])
print('item indeks -7: [2] ',nim[2])
print('item indeks 2: [-7] ',nim[-7])
# akses indeks batas
print(f'item indeks 1,2,....: {nim[1:]}')
print(f'item indeks 3,4,....: {nim[3:]}')
print(f'item indeks 0,1,2,3: {nim[:4]}')
print(f'item indeks 0: {nim[:1]}')
print(f'item indeks semua: {nim[:]}')
print(f'item indeks [:8]: {nim[:-1]}')
print(f'item indeks [:4]: {nim[:-5]}')
# pengirisan
print(f'item indeks 1,2: {nim[1:3]}')
print(f'item indeks []: {nim[3:3]}')
print(f'item indeks 2,3,4: {nim[2:5]}')
print(f'item indeks [1:8]: {nim[1:-1]}')
print(f'item indeks [2:7]: {nim[2:-2]}')
# Nested List
kelas = [('Sains Terpadu',3),
         ('Cinta',2)]
print(kelas)
kelas.append(('Pancasila',2))
kelas.append(('Prog',3))
kelas.append(('Agama',2))
print(kelas)
# tambahkan matkul 4 dan 5 dan sksnya

# Mata kuliah 1: Matkul1 dengan 2 sks
print(f'Mata kuliah 1: {kelas[0][0]} dengan {kelas[0][1]} sks')
# Mata kuliah 2: Matkul2 dengan 3 sks
print(f'Mata kuliah 2: {kelas[1][0]} dengan {kelas[1][1]} sks')
# Mata kuliah 3: Matkul3 dengan 2 sks
print(f'Mata kuliah 3: {kelas[2][0]} dengan {kelas[2][1]} sks')
# Mata kuliah 4: Matkul4 dengan .. sks
print(f'Mata kuliah 4: {kelas[3][0]} dengan {kelas[3][1]} sks')
# Mata kuliah 5: Matkul5 dengan .. sks
print(f'Mata kuliah 5: {kelas[4][0]} dengan {kelas[4][1]} sks')
print()
data = [('Muh Alif',2023,'Aktif'),
        (76,98,89,97,99),
        [3,2,2,3,2],
        ('S1-Reguler','Sistem Informasi B','Ganjil')]

# Nama mahasiswa: Muh Alif
print(f'Nama mahasiswa: {data[0][0]}')
# Inisial Muh Alif: MA
print(f'Muh alif: {data[0] [0] [0]}{data[0] [0] [4]}')
# NIM Muh Alif: 2310310060
hasil = [str(elemen)for elemen in nim]
a = ''.join(hasil)
print(f'NIM {data[0][0]}: {a}')
# Program Muh Alif: S1-Reguler Sistem Informasi B
print(f'Program {data[0][0]}:{data[3][1]}')
# Angkatan Muh Alif: Ganjil-2023
print(f'Angkatan {data[0][0]}:{data[3][2]}-{data[0][1]}')
# Total sks Muh Alif adalah: 12
print(f'Total sks {data[0][0]} adalah:{sum(data[2])}')
# Jumlah Nilai Muh Alif: 5
print(f'Jumlah Nilai {data[0][0]}:{len(data[1])}')
# Nilai tertinggi Muh Alif: 99
print(f'Nilai Tertinggi {data[0][0]}:{max(data[1])}')
# Nilai terendah Muh Alif: 76
print(f'Nilai terendah {data[0][0]}:{min(data[1])}')
# Rata-rata nilai Muh Alif: 91.8
x_bar = sum(data[1])/len(data[1])
print(f'Rata-rata niilai {data[0][0]}:{x_bar}')