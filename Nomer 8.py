print("""
Nama    : Wisnu Dewa Saputra
NIM     : 182410103009
Prodi   : Informatika
""")
#make character
character = ''
sisi = 8
for i in range(sisi):
    for j in range(sisi):
        if i == 0 or i == sisi-1 or j == 0 or j == sisi-1:
            character +='*'
        else:
            character += ' '
    character += '\n'
#character = u"\u25A1"
potition = 8
for i in range(10):
    if i == potition:
        print(character)
    elif i == 9:
        print('_'*20)
    else:
        print()
inputan = input('Masukan w untuk menaikan kotak : ')
if inputan == 'w'or inputan == 'W':
    potition -= 2
    for i in range(10):
        if i == potition:
            print(character)
        elif i == 9:
            print('_'*20)
        else:
            print()
