#list for the binary form for all numbers from n to m
print("Think of a number from 1 to 31.")

binary = []  
for i in range(1,32):
    s = ''
    j = i
    while j != 0:   #convert to binary 
        s = s + str(j%2)
        j = j >> 1
    binary.append(s)   
b = 0
j = 31

number = 0
while j != 0:   
    b += 1
    j = j //2 
    
for i in range(b):
    for j in range(1,31):
        if i < len(binary[j-1]) and binary[j-1][i] == '1':   
            print(j, end = ' ')
    f = input('Is your number here?(Y/N)')
    if f == 'Y':   #calculate the number based on the binary form
        number += 2**i
        print(number)
print('Your number is: ', number)
