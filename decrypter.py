#DEBAYAN MAJUMDER 2020
#Version 1.0
#The basic blueprint of the decrypting algorithm
#This is the driver python script which lets you enter the name of the file,
#and then outputs the formated and modified file in Export Dir.

from encoder import extractFileName
from decoder import *
import os

filePath = input("Enter the path: ")
fileName = extractFileName("/" + filePath)
fileRootPath = extractFilePath("/" + filePath)
fileMetadataPath = "%s%s_metadata.json"%(fileRootPath, fileName[:len(fileName)-10])
rootDir = "Export"
encrptedData = ""
Metadata = ""
doesMetadaExists = os.path.exists("%s%s_metadata.json"%(fileRootPath, fileName[:len(fileName)-10]))
output = []

#CHECKING IF METADATA EXISTS
if doesMetadaExists == False:
    print("File Metadata does not exists! please check again.")
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
    print(len(encrptedData))
    if alorithm == 3:
        for i in  range((len(Metadata) - 3)):
            ch = encrptedData[Metadata[start]:Metadata[end]]
            print(ch)
            print("Start: %s, End: %s"%(Metadata[start], Metadata[end]))
            if ch.isalnum():
                temp = chr(fromHexadecimal(ch))
                output.append(temp)
            else:
                output.append(ch)
            start = start + 1
            end = start + 1
        
    print(output)
