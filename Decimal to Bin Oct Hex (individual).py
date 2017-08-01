num1= int(input("Enter number to convert to Binary: "))
num2= int(input("Enter number to convert to Hexadecimal: "))
num3= int(input("Enter number to convert to Octal: "))

def dec_to_bin(num1):            #decimal to binary
    
    result= ""
    quotient= num1 
    while quotient > 0:
        remainder= quotient % 2
        quotient= quotient // 2
        result= str(remainder) + result
    return result

def dec_to_hex(num2):            #decimal to hexadecimal
    hexmap= {0:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:'A', 11:'B', 12:'C', 13:'D',14:'E',15:'F'}
    result= ""
    quotient= num2 
    while quotient > 0:
        remainder= quotient % 16
        quotient= quotient // 16
        result= str(hexmap[remainder]) + result
    return result

def dec_to_oct(num3):            #decimal to octal
    result= ""
    quotient= num3 
    while quotient > 0:
        remainder= quotient % 8
        quotient= quotient // 8
        result= str(remainder) + result
    return result

print (dec_to_bin(num1))
print (dec_to_hex(num2))
print (dec_to_oct(num3))


