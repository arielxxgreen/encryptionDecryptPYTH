import random
import string

print("Below is my first BASIC Encryp/Decryp Algo")

#Lists out all of the different charachters neccesary to make puntuation
chars = " " + string.digits + string.ascii_letters + "!" + "@" + "#" + "$" +"%" +"^"+"&"+"*"
#seperates each charachter into its own item within a list or array
charsList = list(chars)
#in order for the user to keep up with the assignment of each encrption once we shuffle
encryptionKey = charsList.copy()

#shuffleeee
random.shuffle(encryptionKey)

#ENCRYPTION

def encrypt(userInp):
    encryption = ""
    for letter in userInp:
        for i in range(len(charsList)):
            if letter == charsList[i]:
                encryption += encryptionKey[i]

    return encryption


def decrypt(userInp):
    decryption = ""
    for letter in encryption:
        for i in range(len(encryptionKey)):
            if letter == encryptionKey[i]:
                decryption += charsList[i]

    return decryption

#Printing Encrypted Message
userInp = str(input("What is the secret to life?: "))
encryption = encrypt(userInp)
print("Encrypted Message: " + encryption)


#Printing Decrypted Message
decryption = decrypt(userInp)
print("Decrypted Message: " + decryption)
print(" ")
print (charsList)
print (encryptionKey)