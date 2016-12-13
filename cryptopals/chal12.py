import base64
s = "Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK"
s = base64.b64decode(s)
	
import cryptopal_tools
from Crypto.Cipher import AES

key = None

def enc(data):
	global key
	if key == None:
		key = cryptopal_tools.randBytes(16)
	data = cryptopal_tools.padPKCS7(data + s,16)
	cipher = AES.new(key,AES.MODE_ECB)
	return cipher.encrypt(data)

def findBlockSize():
	l = len(enc(b''))
	i = 1
	while True:
		s = ''.join('A' for j in range(i))
		t = enc(s)
		if len(t) != l:
			return len(t) - l
		i +=1 

def findNextBytes(knownBytes,blocksize):
	pad = 'A' * (blocksize - len(knownBytes) % blocksize -1)
	# encrypt and choosing the right block
	u = enc(pad)[0:len(pad)+len(knownBytes)+1]
	for i in range(0,255):
		# samething as bruteforce
		t = enc(pad + knownBytes + chr(i))[0:len(pad)+len(knownBytes)+1]
		if t == u:
			return chr(i)
	return None

if __name__ == '__main__':
	# detect block size
	blocksize = findBlockSize()
	print 'The blocksize is' , blocksize
	# check ECB encoded
	if cryptopal_tools.isECBencoded(enc(cryptopal_tools.randBytes(blocksize)*2),blocksize):
		print 'ECB encoded'
	else :
		print 'Exit'
	# decrypt
	res = ''
	while True:
		b = findNextBytes(res,blocksize)
		if b is None:
			break
		else:
			res += b
	print res