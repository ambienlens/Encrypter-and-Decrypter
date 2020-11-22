#DEBAYAN MAJUMDER 2020
#Version 2.2
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