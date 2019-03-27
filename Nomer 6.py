print("""
Nama    : Wisnu Dewa Saputra
NIM     : 182410103009
Prodi   : Informatika
""")
str=""
for i in range(0,7):
    for j in range(0,7):
        if (j == 1 or j == 5 or (i == 2 and (j == 2 or j == 4)) or (i == 3 and j == 3)):
            str=str+"* "
        else:
            str=str+"  "
    str=str+"\n"
print(str)
