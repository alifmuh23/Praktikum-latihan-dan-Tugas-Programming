import os
os.system('clear')

a = True

while a:
    jawab = input ('Apakah ingin lanjutkan? (y/n)')
    if jawab == 'y':
        os.system('clear')
        print('Selamat datang Lagi!')
    elif jawab == 'n':
        print('Sampai ketemu lagi :D')
        a = False
    else:
        os.system('clear')
        print('jangan aneh-aneh deh :.)')
        a = True