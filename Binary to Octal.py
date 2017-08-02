num = input('Number in binary in groups of 3 binary digits: ')
i = len(num)-1
map = {'000':'0','001':'1','010':'2','011':'3','100':'4','101':'5','110':'6','111':'7','1000':'8','1001':'9','1010':'A','1011':'B','1100':'C','1101':'D','1110':'E','1111':'F'}
result = ''

#regroup the numbers in 3 and map
while i >= 0:
    j = 0
    inverse = ''
    while i >= 0 and j < 3:
        inverse = inverse + num[i]
        i -= 1
        j += 1
    real = ''
    for k in range(j):
        real = real + inverse[j-1-k]
    result = result + map[real]

for k in range(len(result)):
    print(result[len(result)-1-k],end = '')

