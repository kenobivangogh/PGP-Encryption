#!/usr/bin/env python3
import gnupg

gpg = gnupg.GPG(gnupghome='/home/kali/.gnupg')

path = '/home/kali/PycharmProjects/pgp'
ptfile = '/msg.txt'

with open(path + ptfile, 'rb') as f:
    status = gpg.encrypt_file(f,
                              recipients=['007kaplankaplan@protonmail.com'],
                              output=path+ptfile+".encrypted")

print(status.ok)
print(status.stderr)