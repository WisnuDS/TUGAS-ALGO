print("""
Nama    : Wisnu Dewa Saputra
NIM     : 182410103009
Prodi   : Informatika
""")
print('Program Faktorial')
bilangan = int(input('Berapa Faktorial : '))
hasil = 1
for i in range(1,bilangan+1):
    hasil *= i
print(f'Hasil dari {bilangan}! adalah {hasil}')
