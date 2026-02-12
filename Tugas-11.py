# List toko
toko = ['Telur',
        'Kue',
        'Bayam',
        'Apel',
        'Bawang',
        'Ayam']

print(toko)
print(toko[2 : 4]) # Menampilkan Kue & Bayam mulai dari 2 dan berhenti sebelum index 4

toko.append('Labu') # Menambahkan di akhir list
toko.insert(0, 'Nanas') # Menambahkan di posisi tertentu

toko.remove('Ayam') # Menghapus dengan string
toko.pop(1) # Menghapus dengan index

print(toko)
