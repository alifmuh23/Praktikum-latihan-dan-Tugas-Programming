import os
def judul():
    os.system("cls")
    print("Program menghitung volume dan luas permukaan ".center(45))
    print("Bangun ruang balok".center(45))
    print()

def inputan():
    p = float(input("masukkan panjang : "))
    l = float(input("masukkan lebar : "))
    t = float(input("masukkan tinggi : "))
    return p,l,t

def hitung(p,l,t):
    vol = p*l*t
    luas_surf = 2*(p*l + p*t + l*t)
    luas_non_tutup = luas_surf - p*l
    return vol,luas_surf,luas_non_tutup

def tampilan(pesan,nilai):
    print(f"nilai {pesan} : {nilai}")

def pilihan():
    pilih = input("apakah lanjutkan [y/n]")
    if pilih == "y":
        a = True
    else:
   
        a = False
        print("terima kasih!")
    return a

def main():
    judul()                                                 #judul
    p,l,t = inputan()                                       #inputan
    vol,luas_surf,luas_non_tutup = hitung (p,l,t)           #hitung

    #tampilan
    tampilan("volume",vol)
    tampilan("luas permukaan",luas_surf) 
    tampilan("luas permukaan tanpa tutup",luas_non_tutup)
    a = pilihan()                                           #pilihan
    return a


a = True
while a:
    a = main()

    