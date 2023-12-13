print('praktikum-3\n')

print('NAMA  :MUH ALIF')
print('NIM   :231031060')
print('Prodi :SISTEM INFORMASI B')
###################################
a=True
b=False
print('\n============NAND============')
hasil=not (a and a)
print(a,'nand',a,'adalah =',hasil)
hasil=not (a and b)
print(a,'nand',b,'adalah =',hasil)
hasil=not (b and a)
print(b,'nand',a,'adalah =',hasil)
hasil=not (b and b)
print(b,'nand',b,'adalah =',hasil)

print('\n============NOR============')
hasil=not (a or a)
print(a,'nor',a,'adalah =',hasil)
hasil=not (a or b)
print(a,'nor',b,'adalah =',hasil)
hasil=not (b or a)
print(b,'nor',a,'adalah =',hasil)
hasil=not (b or b)
print(b,'nor',b,'adalah =',hasil)
 
print('\n============NXOR============')
hasil=not (a ^ a)
print(a,'nxor',a,'adalah =',hasil)
hasil=not (a ^ b)
print(a,'nxor',b,'adalah =',hasil)
hasil=not (b ^ a)
print(b,'nxor',a,'adalah =',hasil)
hasil=not (b ^ b)
print(b,'nxor',b,'adalah =',hasil)

# INI OPERATOR MEMBERSHIP
print('\n=========== IN ============')
nama ='MUH ALIF'
test ='UH'#ISI DENGAN DUA HURUF YANG ADA DI NAMA
cek = test in nama
print(test,'ada di',nama,'adalah=',cek)
test ='HU'#ISI DENGAN DUA HURUF YANG ADA DI NAMA
cek = test in nama
print(test,'ada di',nama,'adalah=',cek)

test1='A'
test2='I'
test3='U'
test4='E'
test5='O'
cek =test1 in nama
print(test1,'ada di',nama,'adalah=',cek)
cek=test2 in nama
print(test2,'ada di',nama,'adalah=',cek)
cek=test3 in nama
print(test3,'ada di',nama,'adalah=',cek)
cek=test4 in nama
print(test4,'ada di',nama,'adalah=',cek)
cek=test5 in nama
print(test5,'ada di',nama,'adalah=',cek)

# TUGAS LANJUTAN KODE
#dengan cara yang sama buat operator not in


# INI operator BITWISE
print('\n')
a= 25#tanggal lahir
b= 6 # bulan lahir
a +=60
b +=80
print('============AND============')
print('nilai',a,'biner adalah   =',format(a,'09b'))
print('nilai',b,'biner adalah   =',format(b,'09b'))
print('-------------------------------AND')
c = a & b
print ('Nilai',a,'&',b,'biner adalah=',format(c,'09'))

print('========OR=======')
# TUGAS BUAT OR
print('========XOR=======')
# TUGAS BUAT XOR
print('\n========NOT=======')
c =~a
print('nilai',a,'biner adalah  =',format(a,'09b'))
print('nilai not',a,'biner adalah  =',format(c,'09b'))
# tugas lanjutkan untuk not b
c =~b
print('nilai',b,'biner adalah  =',format(b,'09b'))
print('nilai not',b,'biner adalah  =',format(c,'09b'))
print('\n========Left Shift=======')
c =~a<<2
print('nilai',a,'biner adalah  =',format(a,'09b'))
print('nilai not',a,'<<2 biner adalah  =',format(c,'09b'))

c =~b<<2
print('nilai',b,'biner adalah  =',format(b,'09b'))
print('nilai not',b,'<<2biner adalah  =',format(c,'09b'))

print('\n========Right Shift=======')
c =~a>>2
print('nilai',a,'biner adalah  =',format(a,'09b'))
print('nilai not',a,'>>2 biner adalah  =',format(c,'09b'))

c =~b>>2
print('nilai',b,'biner adalah  =',format(b,'09b'))
print('nilai not',b,'>>2biner adalah  =',format(c,'09b'))

print('=========NOT AND===========')
#TUGAS BUAT UNTUK NAND

print('=========NOT OR===========')
#TUGAS BUAT UNTUK NOR
print('=========NOT XOR===========')
#TUGAS BUAT UNTUK NXOR
print('=========NOT <<2===========')
#TUGAS BUAT UNTUK C=~(A<<2)
#TUGAS BUAT UNTUK C=~(B<<2)
print('=========NOT >>2===========')
#TUGAS BUAT UNTUK C=~(A>>2)
#TUGAS BUAT UNTUK C=~(B>>2)
