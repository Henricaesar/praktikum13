#ada 4 method dalam membuka file : 
#'r' as Read nilai default, membuka file untuk membaca dan error jika tdak ada
#'a' as Add membuka file untuk ditambahkan, membuat file jika tidak ada
#'w' as Write membuka file untuk ditulis , membuat file jika tidak ada
#'x' as Create membuat file yang ditentukan , mengembalikan kesalahan jika file tersebut tidak ada


#file open

#f = open("Demofile.txt")

#/ f = open ("Demofile.txt", "rt")

#file Read
#Syntax fileObject.read()

f = open("C:/Lab1/test.txt", "w")

f.write('Whoops! i have deteled the content!')
f.close

f = open("C:/Lab1/test.txt", "r")

data = f.read()
print(data)

f.close()

#selalu tutup atau close dengan f.close() agar tidak terjadi hal yang tidak diinginkan kedepan

