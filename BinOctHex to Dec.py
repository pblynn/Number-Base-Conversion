base= int(input("Enter base of number to convert from: "))
num= input("Enter number to convert from: ")


def binocthex_to_dec(num,base):
    hexmap = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, 'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
    number= 0
    num= num[::-1]
    for i in range(0,len(num)):
        number+=((base**i)* hexmap[num[i]])
    return (number)

print (binocthex_to_dec(num,base))
