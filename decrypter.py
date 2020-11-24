#DEBAYAN MAJUMDER 2020
#Version 2.2
#Added all the modules of encryption
#The program gets to recognise the Algorithm used to encrypt the program
#This is the driver python script which lets you enter the name of the file,
#and then outputs the formated and modified file in Export Dir.

from encoder import extractFileName
from decoder import *
import os

filePath = input("Enter the path: ")
fileName = extractFileName("/" + filePath)
fileName = fileName[:len(fileName)-10]
fileRootPath = extractFilePath("/" + filePath)
fileMetadataPath = "%s%s_metadata.json"%(fileRootPath, fileName)
rootDir = "Export"
outputDirParent = fileName + "_Decrypted"
outputFileName = "%s/%s/%s_decrypted.txt"%(rootDir, outputDirParent, fileName)
encrptedData = ""
Metadata = ""
doesMetadaExists = os.path.exists("%s%s_metadata.json"%(fileRootPath, fileName))
output = []
isWrite = True

#CHECKING IF METADATA EXISTS
if doesMetadaExists == False:
    print("File Metadata does not exists! please check again.")
    isWrite = False
else:
    #READING THE ENCRYPTED DATA
    with open(filePath) as encryptedFile:
        encrptedData = encryptedFile.read()
    
    #READING THE METADATA
    with open(fileMetadataPath) as encryptedFileMetadata:
        Metadata = extractMetadata(encryptedFileMetadata.read())

    alorithm = Metadata[0]
    currentDate = Metadata[1]

    start = 2
    end = start + 1
    temp = 0
    if alorithm == 1:
        for i in  range((len(Metadata) - 3)):
            ch = encrptedData[Metadata[start]:Metadata[end]]
            #print(ch)
            #print("Start: %s, End: %s"%(Metadata[start], Metadata[end]))
            if ch.isalnum():
                temp = chr(fromBinary(ch))
                output.append(temp)
            else:
                output.append(ch)
            start = start + 1
            end = start + 1
    elif alorithm == 2:
        for i in  range((len(Metadata) - 3)):
            ch = encrptedData[Metadata[start]:Metadata[end]]
            #print(ch)
            #print("Start: %s, End: %s"%(Metadata[start], Metadata[end]))
            if ch.isalnum():
                temp = chr(fromOctal(ch))
                output.append(temp)
            else:
                output.append(ch)
            start = start + 1
            end = start + 1
    elif alorithm == 3:
        for i in  range((len(Metadata) - 3)):
            ch = encrptedData[Metadata[start]:Metadata[end]]
            #print(ch)
            #print("Start: %s, End: %s"%(Metadata[start], Metadata[end]))
            if ch.isalnum():
                temp = chr(fromHexadecimal(ch))
                output.append(temp)
            else:
                output.append(ch)
            start = start + 1
            end = start + 1
    else:
        print("Wrong Input!!")
        isWrite = False
    
#WRITING TO FILE
if isWrite:
    path = os.path.join(rootDir, outputDirParent)
    os.makedirs(path, exist_ok=True)
    with open(outputFileName, "w") as decryptedFile:
        decryptedFile.write("".join(output))
        print("\n--FILE EXPORT SUCCESSFUL--")
