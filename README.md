# Penanganan Eksepsi
 error dapat terjadi pada saat runtime, error seperti itu disebut eksepsi
Fitur
 '''Membangkitkan eksepsi dengan raise atau dibangkitkan secara paksa dengan perintah RAISE'''
x = 10 
if x > 5 :
    raise Exception('Should not exceed 5. the value of x was :  {}'.format(x))

# Setiap kode program yang memungkinkan terjadinya eksepsi, maka perlu untuk ditempatkan di dalam blok TRY
 Ketika ada kesalahan maka kode diblok except akan dieksekusi, sebaliknya jika tidak maka akan diabaikan

# contoh penggunaan TRY EXCEPT
 try :
    with open('file.log') as file :
        read_data = file.read()
 except FileNotFoundError as fnf_error:
    print(fnf_error)
 #  apabila file.log tidak ditemukan maka akan muncul pesan error dibawah

# ada 4 method dalam membuka file : 
 # 'r' as Read nilai default, membuka file untuk membaca dan error jika tdak ada
 # 'a' as Add membuka file untuk ditambahkan, membuat file jika tidak ada
 # 'w' as Write membuka file untuk ditulis , membuat file jika tidak ada
 # 'x' as Create membuat file yang ditentukan , mengembalikan kesalahan jika file tersebut tidak ada


# file open
 # f = open("Demofile.txt") atau
 # f = open ("Demofile.txt", "rt")

# file Read
 # Syntax fileObject.read()

 f = open("C:/Lab1/test.txt", "w")

 f.write('Whoops! i have deteled the content!')
 f.close

 f = open("C:/Lab1/test.txt", "r")

 data = f.read()
 print(data)

 f.close()
 ## selalu tutup atau close dengan f.close() agar tidak terjadi hal yang tidak diinginkan kedepan

![gambar](Screenshot/Screenshot%20(8).png)
![gambar](Screenshot/Screenshot%20(9).png)
![gambar](Screenshot/Screenshot%20(10).png)
![gambar](Screenshot/Screenshot%20(11).png)
![gambar](Screenshot/Screenshot%20(12).png)
![gambar](Screenshot/Screenshot%20(13).png)


