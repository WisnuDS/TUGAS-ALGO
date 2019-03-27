print("""
Nama    : Wisnu Dewa Saputra
NIM     : 182410103009
Prodi   : Informatika
""")
print('Inputkan Angka, jika ingin tahu rata-rata maka input "="')
jumlah = 0
jumlahInput = 0
while True:
    print('>',end='')
    inputan = input()
    if inputan == '=':
        break
    else:
        inputan = int(inputan)
        jumlahInput+=1
        jumlah += inputan
rata = jumlah/jumlahInput
print(rata)
