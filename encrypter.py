#DEBAYAN MAJUMDER 2020
#Version 4.0
#Bug Fixes: Added the directory found name & fixed runtime error
#No need to enter the path name manually, just drag n drop in Import Dir.
#Output Directory name can be changed now
#This is the driver python script which lets you enter the name of the file,
#and then outputs the formated and modified file in Export Dir.

#Importing Libraries
from encoder import *
from datetime import date
import os

rootDir = "Import"
filePath = ""
os.makedirs(rootDir, exist_ok=True)

while True:
    noOfFiles = len(os.listdir(rootDir))
    dirs = os.listdir(rootDir)
    isFileFound = False

    if noOfFiles == 1:
        print("%s Found in Directory."%dirs[0])
        filePath = "%s/%s"%(rootDir, dirs[0])
        break
    elif noOfFiles > 1:
        i = 0
        print("Files under %s Directory: "%rootDir)
        for this in dirs:
            print("%s) %s"%(i+1, this))
            i = i + 1
        
        print("Can't find the file? Press Enter to Search the directory again,")
        n = input("or Enter number corresponding to the file name: ")

        if n == "":
            input("Drag n drop the data/file into the import directory and press enter to continue.")
        else:
            filePath = "%s/%s"%(rootDir, dirs[int(n) - 1])
            break
    else:
        print("Dir. is Empty")
        ch = input("Do you want to enter the path? (y/n): ")
        if ch.lower() == "y":
            filePath = input("Enter the path of the file: ")
            break
        elif ch.lower() == "n":
            input("Drag n drop the data into the import dir. and press enter to continue.")


fileName = extractFileName("/" + filePath)
outputDir = "Export"
outputDirParent = fileName + "_Encrypted"
outputFileName = "%s/%s/%s_encrypted.txt"%(outputDir, outputDirParent, fileName)
metadataFileName = "%s/%s/%s_metadata.json"%(outputDir, outputDirParent, fileName)
output = []
metadata = []
tD = str(date.today())
currentDate = "".join([i for i in tD if i != "-"])
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
            temp = toBinary(char)
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
            temp = toOctal(char)
            sizeOf = sizeOf + len(temp)
            metadata.append(str(sizeOf))
            output.append(temp)
        else:
            sizeOf = sizeOf + 1
            metadata.append(str(sizeOf))
            output.append(i)
elif choice == "3":
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
else:
    print("Wrong Input.")
    isWrite = False

if isWrite:   
    print("------------------------------")
    path = os.path.join(outputDir, outputDirParent)
    os.makedirs(path, exist_ok=True)
    with open(outputFileName, "w") as modifiedContent:
        modifiedContent.write("".join(output))
        print("\n--FILE EXPORT SUCCESSFUL--")

    #Modifing the Hidden Attribute to viewable, if metadata already exists
    if(os.path.exists(metadataFileName)):
        os.system("attrib -h %s"%(metadataFileName))

    with open(metadataFileName, "w") as mdFile:
        mdFile.write("[")
        mdFile.write("%s,"%choice)
        mdFile.write("%s,"%currentDate)
        mdFile.write("0,")
        mdFile.write(",".join(metadata))
        mdFile.write("]")
        os.system("attrib +h %s"%(metadataFileName))
        print("--METADATA WRITTEN SUCCESSFULLY--\n")