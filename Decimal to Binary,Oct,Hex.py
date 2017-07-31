num= int(input("Enter number to convert: "))
base= int(input("Enter base to convert to: "))

def dec_to_binocthex(num,base):
    hexmap= {0:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:'A', 11:'B', 12:'C', 13:'D',14:'E',15:'F'}
    result= ""
    quotient= num 
    while quotient > 0:
        remainder= quotient % base
        quotient= quotient // base
        result= str(hexmap[remainder]) + result
    return result

print (dec_to_binocthex(num,base))
