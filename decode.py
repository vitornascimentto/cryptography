from cryptography.fernet import Fernet
import os

def apagar(path):  
    dir = os.listdir(path)
    print(dir)

path = '/home/nascimento/Documents/Cryptography'
apagar(path)

name = input()

data = []
with open('{}.txt'.format(name), 'r') as arq:
	text = arq.readlines()
	for line in text:
		data.append(line)

key = data[0].encode('utf-8')
password = data[1].encode('utf-8')

f = Fernet(key)
print(f.decrypt(password).decode('utf-8'))