#DEBAYAN MAJUMDER 2020
#Version 2
#Added support of executing both script from one script
#This is the driver python script which lets you decide between encrypting
#and decrypting and then executing the corresponding scripts

import os

print("--ENCRYPTER & DECRYPTER--")
print("ENTER 1 FOR ENCRYPTING & 2 FOR DECRYPTING --")
user_choice = input("Enter your purpose: ")

if user_choice == "1":
    os.system("encrypter.py")
elif user_choice == "2":
    os.system("decrypter.py")
else:
    print("Wrong Input")
