# Game tebak angka
import random

angka_rahasia = random.randint(1, 10)
tebakan = 1

print('Saya memikirakan angka antara 1 sampai 10. bisa tebak?')

while tebakan != angka_rahasia    # Akan terus mengulang hingga jawabannya == angka_rahasia
    tebakan = int(input('Masukkan tebakanmu:    '))

if tebakan < angka_rahasia:
    print('Terlalu rendah! coba lagi')
elif tebakan > angka_rahasia:
    print('Terlalu tinggi! coba lagi')
else:
    print('Selamat! kamu berhasil menebaknya')
