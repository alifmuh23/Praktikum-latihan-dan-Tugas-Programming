nama='Muh Alif'
nim='231031060'
meet='praktikum 4'
prodi='Sistem informasi B'
email='muhalif1788@gmail.com'
tanggal='11 oktober 2023'
sp=40

print()
print(len(nama))
print('-'*sp)
nama.center
print(nama.center(sp))
print(nim.center(sp))
print('\n'*2)
print(prodi.rjust(sp))
print(email.rjust(sp)+ f'\r{tanggal}')
print('-'*sp)

paragraf = '''Halo selamat datang perkenalkan nama
saya {}dengan {} dari {} ini adalah
file {}.'''
p=paragraf.format(nama,nim,prodi,meet)
print(p)
print('-----------8++++++++')
x=9
hasil =x>8
print(x,'hasilnya adalah',hasil)

x=3
hasil =x>8
print(x,'hasilnya adalah',hasil)
print('++++++++8-----------')
x=9
hasil =x<8
print(x,'hasilnya adalah',hasil)
x=3
hasil =x<8
print(x,'hasilnya adalah',hasil)

print('--------4+++++++8---------')
x=9
#cek1=x>4 true
cek1=x>4
#cek2=x<8 true
cek2=x<8
#hasil=cek1 and cek2
hasil=cek1 and cek2
#cetak hasil
print(x,'hasilnya adalah',hasil)
print('+++++++++4--------8++++++++++')
x=2
#cek1=x<4 true
cek1=x<4
#cek2=x>8 true
cek2=x>8
#hasil=cek1 or cek2
hasil=cek1 or cek2
#cetak hasil
print(x,'hasilnya adalah',hasil)
