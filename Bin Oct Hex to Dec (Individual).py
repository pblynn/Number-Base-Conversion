num= input("Enter Binary number: ")
num1= input("Enter Octal number: ")
num2= input("Enter Hexadecimal number: ")

def bin_to_dec(num):
    number= 0
    num= num[::-1]
    for i in range(0,len(num)):
        number+=((2**i)* int(num[i]))
    return (number)


def oct_to_dec(num1):
    number= 0
    num1= num1[::-1]
    for i in range(0,len(num1)):
        number+=((8**i)* int(num1[i]))
    return (number)

def hex_to_dec(num2):
    hexmap = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, 'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
    number= 0
    num2= num2[::-1]
    for i in range(0,len(num2)):
        number+=((16**i)* hexmap[num2[i]])
    return (number)

print (bin_to_dec(num))
print (oct_to_dec(num1))
print (hex_to_dec(num2))
