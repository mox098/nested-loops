num = int(input("Enter a decimal number: "))

if num == 0:
    print("Binary equivalent: 0")
else:
    binary = ""

    while num > 0:        
        remainder = num % 2

        temp = ""          
        i = 0 
        while i < 1:        
            temp = str(remainder) + temp
            i += 1

        binary = temp + binary
        num = num // 2

    print("Binary equivalent:", binary)