# IF, ELIF, ELSE ADALAH PERCABANGAN LOGIKA
umur = int(input('Masukkan umur anda:   '))
if umur >= 25:                  # IF Mengecek kondisi pertama
   print('Kamu sudah dewasa')
elif umur >= 18:                # ELIF Mengecek kondisi tambahan
   print('Kamu sudah remaja')
else:                     # ELSE Jalan terakhir jika kondisi sebelumny false
   print('Kamu masih anak-anak')
