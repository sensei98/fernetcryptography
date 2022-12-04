from cryptography.fernet import Fernet
import os
import time

key = Fernet.generate_key()
crypt_key = Fernet(key)
ospath = os.path.dirname(
    os.path.abspath(__file__))


def Encryptfile():
    with open(ospath + '/example.csv', 'rb') as csv:
        rawcsv = csv.read()  # reading csv file

    encrypted = crypt_key.encrypt(rawcsv)

    with open(ospath + '/enc_example.csv', 'wb') as encryptedcsv:
        encryptedcsv.write(encrypted)  # saving encrypted csv as another csv


def Decryptfile():
    with open(ospath + '/enc_example.csv', 'rb') as encryptedfile:
        encrypted = encryptedfile.read()
    decrpyted = crypt_key.decrypt(encrypted)  # reading encrypted csv file

    with open(ospath + '/dec_example.csv', 'wb') as decrypted_file:
        decrypted_file.write(decrpyted)  # decrypting into a new csv file


print("Enrypting csv file.......")
Encryptfile()

time.sleep(2)  # two seconds delay between tasks

print("Decrypting csv file.......")
Decryptfile()

time.sleep(1)
print("--Done--")
