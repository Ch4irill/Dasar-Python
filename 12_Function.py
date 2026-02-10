# Function adalah kumpulan kode yang diberi nama, lalu bisa dipanggil kapan saja dalam program
def sapa(nama, umur): # Posisi variabel harus sesuai dengan outputnya
    print(f'Halo {nama} kamu berumur {umur}') # Menampilkan teks saja
sapa('Akbar', 20)
sapa('Dirga', 10)

# kelebihan return nilainya bisa dipakai kembali
def tambah(a, b):
    return a + b # Mengembalikan nilai ke tempat function itu dipanggil

hasil = tambah(1, 2) # Variabel hasil menerima nilai
print(hasil)
if hasil >= 3:
    print('benar')
else:
    print('salah')
