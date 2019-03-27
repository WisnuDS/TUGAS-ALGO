print("""
Nama    : Wisnu Dewa Saputra
NIM     : 182410103009
Prodi   : Informatika
""")
print('PROGRAM TABUNGAN SE')
is_Lunas = False
deadline = 12
totalBayar = 1500000
kekurangan = 1500000
jumlahTabungan = 0
for minggu in range(1,deadline+1):
    tabungan = int(input(f'Tabungan Minggu {minggu} :'))
    jumlahTabungan += tabungan
    kekurangan = totalBayar - jumlahTabungan
    if jumlahTabungan >= totalBayar:
        is_Lunas = True
        break
    elif minggu%4 == 0 and minggu<12:
        sisaDeadline = deadline - minggu
        saran = kekurangan/(deadline-minggu)
        print('================================================================================')
        print(f'Tabungan Hingga Bulan ini adalah : {jumlahTabungan}')
        print(f'Sisa Deadlinenya adalah : {sisaDeadline} Minggu')
        print(f'Kekurangan Uang SE : {kekurangan}')
        print(f'Kami Menyarankan Tabungan selanjutnya dan seterusnya adalah : {saran}')
        print('================================================================================')
if is_Lunas :
    print('================================================================================')
    print(f'Selamat anda telah memenuhi biaya untuk study excursie dengan waktu pengumpulan {minggu} minggu, anda bisa menutup tabungan anda')
    print('================================================================================')
else:
    print('================================================================================')
    print(f'''Mohon maaf, anda belum bisa mengikuti study excursie kali ini karena dana anda
        untuk study excursie hingga waktu pengumpulan saat ini masih kurang sebesar RP. {kekurangan} .
        Silahkan coba lagi tahun depan, dan lebih hemat dan rajin menabung''')
    print('================================================================================')
