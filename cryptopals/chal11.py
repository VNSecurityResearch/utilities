import cryptopal_tools
from random import randint 
from Crypto.Cipher import AES

def encryption_oracle(data):
	key = cryptopal_tools.randBytes(16)
	if randint(0,1) == 0:
		print 'ECB encoded'
		cipher = AES.new(key,AES.MODE_ECB)
	else:
		print 'CBC encoded'
		IVs = cryptopal_tools.randBytes(16)
		cipher = AES.new(key,AES.MODE_CBC,IVs)
	data = cryptopal_tools.randBytes(randint(5,10)) + data + cryptopal_tools.randBytes(randint(5,10))
	data = cryptopal_tools.padPKCS7(data,16)
	return cipher.encrypt(data)

if __name__ == '__main__':
	pt = ''.join(chr(0) for i in range(40))
	ct = encryption_oracle(pt)
	if cryptopal_tools.isECBencoded(ct,16):
		print 'It is ECB'
	else:
		print 'It is CBC'
