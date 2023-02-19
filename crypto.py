import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

#ENCRYPT
plain_text = input("Ingrese el mensaje a encriptar : ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Mensaje original :\n{plain_text}")
print(f"Mensaje encriptado :\n{cipher_text}")

#DECRYPT
cipher_text = input("Ingrese el mensaje encriptado : ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"Mensaje encriptado :\n{cipher_text}")
print(f"Mensaje original :\n{plain_text}")