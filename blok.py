#Setiap kode program yang memungkinkan terjadinya eksepsi, maka perlu untuk ditempatkan di dalam blok TRY
#Ketika ada kesalahan maka kode diblok except akan dieksekusi, sebaliknya jika tidak maka akan diabaikan

#contoh penggunaan TRY EXCEPT
try :
    with open('file.log') as file :
        read_data = file.read()
except FileNotFoundError as fnf_error:
    print(fnf_error)

#apabila file.log tidak ditemukan maka akan muncul pesan error dibawah