x = int(input())
y = int(input())
z = int(input())
for i in range(1,z+1):
    if i % x == 0 and i % y ==0:
        print('ADUH SAKIT ANJING')
    elif i % x == 0:
        print('Aduh')
    elif i % y == 0:
        print('Sakit')
    else:
        print(i)
