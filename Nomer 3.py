print("""
Nama    : Wisnu Dewa Saputra
NIM     : 182410103009
Prodi   : Informatika
""")
print('Program No 3')
n = int(input('Banyak Nilai N : '))
total =0
for i in range(n):
    bilangan = int(input('Masukan Bilangan : '))
    total += bilangan
rata = total/n
print(f'Jumlah : {total}')
print(f'Rata-rata : {rata}')
if rata < n :
    print('Nilai rata-rata lebih kecil dibanding inputan')
else:
    print('Nilai rata-rata lebih besar dibanding inputan')
