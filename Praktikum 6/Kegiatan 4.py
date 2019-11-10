Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Nama = 'Yayes Kasnanda Bintang'
>>> NIM = 206
>>> Tinggi = 1.68
>>> Berat = 55
>>> TahunLahir = 2001
>>> Aku = (TahunLahir, Berat, Tinggi, NIM, Nama)
>>> Data = [TahunLahir, Berat, Tinggi, NIM, Nama]
>>> type(Aku)
<class 'tuple'>
>>> #Karena data "Aku" ditulis dalam tanda kurung
>>> Aku[0]
2001
>>> #Karena objek pertama dalam data "Aku" adalah "TahunLahir", dan data dalam "TahunLahir" adalah 2001
>>> a = NIM % 4; Aku[a]
1.68
>>> #Karena 206 dibagi 4 sisa 2, maka objek ke 2 dalam data "Aku" adalah "Tinggi" dan hasilnya 1.68
>>> type(Aku[a])
<class 'float'>
>>> #Karena data dalam "a" ditulis dalam bentuk desimal
>>> Aku[a:4]
(1.68, 206)
>>> #Karena 4 objek utama dalam "Aku" adalah data "Tinggi", "NIM"
>>> type(Aku[4])
<class 'str'>
>>> #Karena urutan data ke 4 dalam data "Aku" adalah "NIM", Nilai dari "NIM" adalah 206 bertipe data String
>>> Aku[0] = 'ok'
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    Aku[0] = 'ok'
TypeError: 'tuple' object does not support item assignment
>>> #ERROR karena data bertipe "Tuple" tidak dapat diubah
>>> type(Data)
<class 'list'>
>>> #Karena data dalam "Data" ditulis dalam kurung siku
>>> type(Data[4])
<class 'str'>
>>> #Karena urutran data ke 4 dalam "Data" adalah "Nama", dan "Nama" bertipe data String
>>> Data[4][5]
' '
>>> #Karena urutan data ke 4 dalam "Data" adalah "Nama", dan karakter ke 5 dalam "Nama" adalah "spasi"
>>> Data [4][a:6]
'yes '
>>> #Karena urutan data ke 4 dalam "Data" adalah "Nama", dan karakter ke 2 sampai 6 adalah "yes "
>>> Data[0] = 'ok'; Data
['ok', 55, 1.68, 206, 'Yayes Kasnanda Bintang']
>>> #Karena data pertama diubah menjadi "ok" dan, program menampilkan seluruh objek dalam "Data"
>>> Data [-a]
206
>>> #Karena menampilkan data ke 2 dari kanan yaitu "NIM" yang nilainya 206
>>> range(a)
range(0, 2)
>>> #Karena variabel a adalah 2, jadi "range[a]" adalah range(0, 2) yang memiliki objek/indeks 0 sampai 2
