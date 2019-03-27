x = int(input())
str = ''
for i in range(x+2):
    if i == 0:
        titik = 2
        for j in range(1,x+1):
            if j == titik:
                str += '.'
                titik +=4
            else:
                str += '*'
    elif i == x+1:
        for j in range(1,x+1):
            if j % 4 == 0:
                str += '.'
            else:
                str += '*'
    else:
        for j in range(1,x+1):
            if j % 2 == 0:
                str+='.'
            else:
                str+='*'
    str+='\n'
print(str)
