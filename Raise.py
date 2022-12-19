#Penanganan Eksepsi
#error dapay terjadi pada saat runtime, error seperti itu disebut eksepsi
#Fitur
#Membangkitkan eksepsi dengan raise atau dibangkitkan secara paksa dengan perintah RAISE
x = 10 
if x > 5 :
    raise Exception('Should not exceed 5. the value of x was :  {}'.format(x))