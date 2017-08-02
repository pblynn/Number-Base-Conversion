while True:
    try:
        n = int(input("Enter lower limit: "))  
        m = int(input("Enter higher limit: "))
    except ValueError:
        print("Please input a numerical value. Try again. ")
        continue

#list for the binary form for all numbers from n to m
binary = []  
for i in range(int(n),int(m)+1):
    s = ''
    j = i
    while j != 0:   #converts to binary 
        s = s + str(j%2)
        j = j//2
    binary.append(s)   
b = 0
j = int(m)

number = 0
while j != 0:   
    b += 1
    j = j//2 
    
for i in range(b):
    for j in range(int(n),int(m)+1):
        if i < len(binary[j-int(n)]) and binary[j-int(n)][i] == '1':
            print(j, end = ' ')
    f = input('Is your number here?(Y/N)')
    if f == 'Y':   #calculate the number based on the binary form
        number += 2**i
        print(number)
print('Your number is: ', number)
