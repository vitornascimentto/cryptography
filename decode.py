from cryptography.fernet import Fernet
import os

def apagar(path):  
    dir = os.listdir(path)
    print(dir)

path = '/home/nascimento/Documents/Cryptography'
apagar(path)

name = input()