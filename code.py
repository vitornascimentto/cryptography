from cryptography.fernet import Fernet

description = input('Description: ')
password = input('Password: ').encode('utf-8')

key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(b'%s'%password)

key = key.decode('utf-8')
token = token.decode('utf-8')

with open('{}.txt'.format(description), 'w') as data:
    data.write(f'{token}\n{key}')