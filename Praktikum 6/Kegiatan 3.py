Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Nama = 'Yayes Kasnanda Bintang'
>>> NIM = 'L200190206'
>>> X = '1' + NIM[7:]
>>> a = int(X)
>>> b = len(Nama)
>>> type(a)
<class 'int'>
>>> #Karena data "X" telah berubah menjadi tipe data integer
>>> type(b)
<class 'int'>
>>> #Karena data "Nama" memiliki instruksi "len"
>>> a / b
54.81818181818182
>>> #Karena hasil 1206 dibagi 22 adalah 54.81818181818182
>>> a // b
54
>>> #Karena arti "//" adalah pembagian dengan pembulatan
>>> 10 * (a -999)
2070
>>> #Karena  nilai "a" dikurangi 999 adalah 207, setelah itu dikalikan dengan 10 dan hasilnya adalah 2070
>>> b ** 2
484
>>> #Karena arti "**" adalah perpangkatan
>>> a % b
18
>>> #Karena arti "%" adalah sisa hasil bagi
>>> c = 12.5
>>> type(c)
<class 'float'>
>>> #Karena "12.5" adalah angka desimal
>>> a / c
96.48
>>> #Karena hasil 1206 dibagi 12.5 adalah 96.48
>>> a // c
96.0
>>> #Karena arti "//" adalah pembagian denagn pembulatan
>>> a % c
6.0
>>> #Karena arti "%" adalah sisa hasil bagi
>>> c > b
False
>>> #Karena "c" lebih besar dari "b" bernilai "Salah"
>>> type(c > b)
<class 'bool'>
>>> #Karena data "(c > b)" bertipe data Boolean
>>> a > b and b > c
True
>>> #Karena "Benar dan Benar" hasilnya "Benar"
>>> a > 1100 or b < 10
True
>>> #Karena "Benar atau Salah" hasilnya "Benar"
>>> 
