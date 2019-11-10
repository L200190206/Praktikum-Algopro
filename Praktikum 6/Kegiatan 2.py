##Program Akun
##Dibuat oleh Bintang L200190206
import random
angka = random.randint(0,1000)

Nama = 'Yayes Kasnanda Bintang'
TanggalLahir = '13 Mei 2001'
NamaSingkat = Nama[0] + '.' + Nama[6] + '.' + Nama[15:22]
Username = Nama[0] + TanggalLahir[0:2] + TanggalLahir[7:12]
Password = Nama[15:18] + str(angka)

print(Nama)
print(TanggalLahir)
print(NamaSingkat)
print(Username)
print(Password)
