#DEBAYAN MAJUMDER 2020
#Version 3.4
#Bug FIxes: Json conversion was problematic
#Added method for metadata formatting
#THIS PYTHON SCRIPT HAS THREE FUNCTIONS WHICH HELPS TO RETURN THE EQUIVALENT
#OF THE NUMBER PASSED.
#THE SCRIPT CONVERTS THREE DIFFERENT BASES TO DECIMAL

#METHOD FOR CONVERTING BINARY TO DECIMAL
def fromBinary(n):
    output = 0
    exp = len(n) - 1
    for i in n:
        if i == "1":
            output = output + 2**exp * 1
        else:
            output = output + 2**exp * 0
        exp = exp - 1
    return output

#METHOD FOR CONVERTING HEXADECIMAL TO DECIMAL
def fromHexadecimal(n):
    output = 0
    exp = len(n) - 1
    for i in n:
        if (i == "A") or (i == "B") or (i == "C") or (i == "D") or (i == "E") or (i == "F"):
            output = output + 16**exp * int(ord(i) - 55)
        else:
            output = output + 16**exp * int(i)
        exp = exp - 1
    return output

#METHOD FOR CONVERTING OCTAL TO DECIMAL
def fromOctal(n):
    output = 0
    exp = len(n) - 1
    for i in n:
        output = output + 8**exp * int(i)
        exp = exp - 1
    return output

#METHOD TO EXTRACT FILE PATH FROM A GIVEN PATH
def extractFilePath(path):
    i = 0
    j = 0
    for this in path:
        if this == "/":
            j = i
        elif this == ".":
            break
        i = i + 1

    return path[1:j+1]

#CONVERTING THE STRING INSIDE JSON FILE TO A LIST
def extractMetadata(jsonFile):
    output = []
    s = 0
    for this in jsonFile:
        ch = ord(this)
        if ch >= 48 and ch <= 57:
            s = s*10 + int(this)
        elif ch == 44 or ch == 93:
            output.append(s)
            s = 0
    
    return output