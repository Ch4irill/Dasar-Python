# Enter pin
print('loops')

pin = int(input('Masukkan pin atm kamu:	'))
while pin != 1234:
	pin = int(input('Pin salah, coba lagi:	'))

print('pin diterima')
# Enter pin dengan kesempatan
print('3 kali percobaan')

pin = int(input('Masukkan pin atm kamu:	'))
kesempatan = 3
while pin != 1234 and kesempatan > 0:
	pin = int(input('Pin salah, coba lagi:	')) 
	kesempatan -=1
	if pin == 1234:
		print('pin benar')
	else:
		print('Atm anda terblokir')
