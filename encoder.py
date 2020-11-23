#DEBAYAN MAJUMDER 2020
#Version 3.0
#THIS PYTHON SCRIPT HAS THREE FUNCTIONS WHICH HELPS TO RETURN THE EQUIVALENT
#OF THE NUMBER PASSED. 
#THE SCRIPT CONVERTS DECIMAL TO THREE DIFFERENT BASES

#METHOD FOR CONVERTING DECIMAL TO BINARY
def toBinary(n):
    values = [64, 32, 16, 8, 4, 2, 1]
    output = []
    sum = 0
    i = 0
    while True:
        if(sum == n):
            break
        else:
            temp = sum + values[i]
            if(temp <= n):
                sum = sum + values[i]
                output.append("1")
                i = i + 1
            else:
                output.append("0")
                i = i + 1
    
    return "".join(output)

#METHOD FOR CONVERTING DECIMAL TO HEXADECIMAL
def toHexadecimal(n):
    output = [] 
    i = 0
    while(n != 0):
        temp = 0
        temp = n % 16
        if(temp < 10): 
            output.append(chr(temp + 48)) 
            i = i + 1
        else: 
            output.append(chr(temp + 55)) 
            i = i + 1
        n = int(n / 16)
    
    output.reverse()
    return "".join(output)

#METHOD FOR CONVERTING DECIMAL TO OCTAL
def toOctal(n):
    output = []
    while n!=0:
        output.append(str(n % 8))
        n = int(n/8)
    
    output.reverse()
    return "".join(output)

#METHOD TO EXTRACT FILE NAME FROM A PATH PASSED
def extractFileName(path):
    i = 0
    j = 0
    for this in path:
        if this == "/":
            j = i
        elif this == ".":
            break
        i = i + 1

    return path[j+1:i]