initial= int(input("Enter base to convert from: "))
final= int(input("Enter base to convert to: "))
string= str(input("Enter number to convert: "))
                  
def number_conversion(string, initial, final):
    if initial ==10:            #if input is already in base 10 (decimal)
        s= int(string)
    else:                       #if input is not in base 10 (hex/oct/bin)
        s= 0
        for char in string:
            if char.isalpha():  #if char is alphabet (hex)
                x=ord(char.lower()) - 87
            elif char.isdigit(): #if char is number (oct/bin)
                x= int(char)
                s= (s**initial) + x #input to base 10 (decimal)
            if final ==10:
                return str(s)
            else:
                digits= []
                while s>0:
                    digits.append(s%final)
                    s= s//final
                new= ''
                for i in range(len(digits)-1,-1, -1):
                    if digits[i] >=10:
                        new+= chr(digits[i]+55)
                    else:
                        new= new + str(digits[i])
                return new
print (number_conversion(string,initial,final))
                    
