#! /usr/bin/python
from Crypto.Cipher import ARC4
from Crypto.Hash import SHA256
from Crypto import Random
def enc(key,p):
		return ARC4.new(key).encrypt(p)
def dec(key,msg):
		return ARC4.new(key).decrypt(msg)
def main():
		key = 'this is a real key'
		p = 'aloha, good night ha!'
		nonce=Random.new().read(16)
		key +=nonce
		key = SHA256.new(key).digest() #key is no more than 256bytes
		print("plaintext is:  " + p)
		print("encryto key ==>  " + key)
		print("ciphertext is:  " +enc(key,p))
		print("After decrypto:  " +dec(key,enc(key,p)))
if __name__=='__main__':
		     main()