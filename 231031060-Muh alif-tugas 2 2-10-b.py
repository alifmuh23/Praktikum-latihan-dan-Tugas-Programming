
print('2 : selisih waktu')

jam1 = int(input("Masukkan jam pertama: "))
menit1 = int(input("Masukkan menit pertama: "))

jam2 = int(input("Masukkan jam kedua: "))
menit2 = int(input("Masukkan menit kedua: "))


total_jam = (jam1 - jam2)
total_menit = (menit1 - menit2)


if total_menit >= 60:
    total_jam += total_menit // 60
    total_menit = total_menit % 60
    



print("selisih waktu: {}:{}".format(total_jam, total_menit))