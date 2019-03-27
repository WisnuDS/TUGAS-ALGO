print("""
Nama    : Wisnu Dewa Saputra
NIM     : 182410103009
Prodi   : Informatika
""")
print('Program Segitiga')
print("""
Pilih salah satu
1. Segitiga Normal
2. Segitiga Terbalik
""")
pilihan = input('Silahkan pilih menu yang anda inginkan sesuai dengan nomor : ')
if pilihan == '1':
    baris = int(input('Banyak baris : '))
    for i in range(1,baris+1):
        print('*'*i)
else :
    baris = int(input('Banyak baris : '))
    for i in reversed(range(1,baris+1)):
        print('*'*i)
