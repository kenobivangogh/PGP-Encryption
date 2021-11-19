#!/usr/bin/env python3
import gnupg

gpg = gnupg.GPG(gnupghome='/home/kali/.gnupg')

path = '/home/kali/PycharmProjects/pgp'
ptfile = '/msg.txt.encrypted'

with open(path + ptfile, 'rb') as f:
    status = gpg.decrypt_file(f, passphrase='passphrase', output=path+ptfile+".decrypted")

print(status.ok)
print(status.stderr)
