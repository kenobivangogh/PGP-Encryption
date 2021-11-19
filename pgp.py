#!/usr/bin/env python3
import gnupg

gpg = gnupg.GPG(gnupghome='/home/kali/.gnupg')
gpg._encoding = 'utf-8'

input_data = gpg.gen_key_input(
        name_email='007kaplankaplan@protonmail.com',
        passphrase='passphrase',
        key_type='RSA',
        key_length='512')

key = gpg.gen_key(input_data)

print(key)
