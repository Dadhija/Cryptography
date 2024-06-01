# -*- coding: utf-8 -*-
"""Homework4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1m36Emhdv0Qd4BEe9VFEwCWKvRj8Xodsm
"""

!pip install pycryptodome

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import binascii

UID = 119186367
Last_Name = "Patel"
First_Name = "Dadhija"

def rsa_enc_public(inputblock, keypair):
  encryptor = PKCS1_v1_5.new(keypair.publickey())
  encrypted = encryptor.encrypt(inputblock)
  return encrypted

def rsa_dec_private(cipherblock, keypair):
  decryptor = PKCS1_v1_5.new(keypair)
  decrypted = decryptor.decrypt(cipherblock, None)
  return decrypted


if __name__ == "__main__":

  keyPair = RSA.generate(2048) 
  
  msg = b'A message for encryption'

  ciphertext = rsa_enc_public(msg, keyPair)
  print(binascii.hexlify(ciphertext))

  plaintext = rsa_dec_private(ciphertext, keyPair)
  print(plaintext)