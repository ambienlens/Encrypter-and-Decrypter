#DEBAYAN MAJUMDER 2020
#Version 2.2
#Added the parent file name in the output file for easy finding
#Output Directory name can be changed now
#This is the main driver python script which lets you enter the name of the file,
#and then outputs the formated and modified file in Export Dir.

#Importing Libraries
from encoder import *
from datetime import date
import os

filePath = input("Enter the path of the file: ")
fileName = extractFileName("/" + filePath)
outputDir = "Export"
outputFileName = "%s/%s_encrypted.txt"%(outputDir, fileName)
output = []
metadata = []
tD = str(date.today())
currentDate = "".join([i for i in tD if i != "-"])
copyright = "AMBNTLNSTN_2020"
isWrite = True

with open(filePath) as originalContent:
    code = originalContent.read()

print("------------------------------")
print("CHOOSE THE ENCODING ALGORITHM")
print("1) Binary Encoding, 2) Octal Encoding, 3) HexaDecimal Encoding")
choice = input("Enter Encoding Algoithm Number: ")

temp = 0
sizeOf = 0
if choice == "1":
    for i in code:
        char = ord(i)
        #ASCII FOR A-Z, a-z, 0-9
        if ((char>=65 and char<=90) or (char>=97 and char<=122) or (char>=48 and char<=57)):
            temp = toHexadecimal(char)
            sizeOf = sizeOf + len(temp)
            metadata.append(str(sizeOf))
            output.append(temp)
        else:
            sizeOf = sizeOf + 1
            metadata.append(str(sizeOf))
            output.append(i)
elif choice == "2":
    for i in code:
        char = ord(i)
        #ASCII FOR A-Z, a-z, 0-9
        if ((char>=65 and char<=90) or (char>=97 and char<=122) or (char>=48 and char<=57)):
            output.append(toOctal(char))
        else:
            output.append(i)
elif choice == "3":
    for i in code:
        char = ord(i)
        #ASCII FOR A-Z, a-z, 0-9
        if ((char>=65 and char<=90) or (char>=97 and char<=122) or (char>=48 and char<=57)):
            output.append(toHexadecimal(char))
        else:
            output.append(i)
else:
    print("Wrong Input.")
    isWrite = False

if isWrite:   
    print("------------------------------")
    metaData = " ".join(metadata) + "_" + currentDate + "_" + copyright
    os.makedirs(outputDir, exist_ok=True)
    with open(outputFileName, "w") as modifiedContent:
        modifiedContent.write("".join(output))
        modifiedContent.write("\n\n\n\n\n\n\n\n%s"%metaData)
        print("\n--FILE EXPORT SUCCESSFUL--\n")
