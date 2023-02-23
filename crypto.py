import random
import string
import modulo_Mina

def encrypt(text):

    if modulo_Mina.test(text) == 'class "str"':
        chars = " " + string.punctuation + string.digits + string.ascii_letters
        chars = list(chars)
        key = chars.copy(); random.shuffle(key)
        cipher_text = ""

        for letter in text:
            index = chars.index(letter)
            cipher_text += key[index]

    else:
        cipher_text = TypeError

    return cipher_text

def decrypt(text):

    if modulo_Mina.test(text) == 'class "str"':
        chars = " " + string.punctuation + string.digits + string.ascii_letters
        chars = list(chars)
        key = chars.copy(); random.shuffle(key)
        plain_text = ""
    
        for letter in text:
            index = key.index(letter)
            plain_text += chars[index]

    else:
        plain_text = TypeError

    return plain_text