import os
os.system('clear')

pwd_benar = 'si23b'
a = True
i = 0
limit = 3
while a:
    i += 1
    pwd = input('Masukkan password: ')
    if pwd == pwd_benar:
        print('Selamat anda login')
        a = False 
    else:
         if i == limit:
          a= False
          print('Kesempatan anda habis')
         elif i+1 == limit:
          print('kesempatan anda sisa 1 kali') 
         else:    
           print('Kesempatan anda sisa 2 kali')