print("""
Nama    : Wisnu Dewa Saputra
NIM     : 182410103009
Prodi   : Informatika
""")
print('PROGRAM PERPANGKATAN')
basis = int(input('Nilai Basis : '))
pangkat = int(input('Nilai pangkat : '))
hasil = 1
for i in range(pangkat):
    hasil *= basis
print(f'Hasil dengan cara 1 : {hasil}')
