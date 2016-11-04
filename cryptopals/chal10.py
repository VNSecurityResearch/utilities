import base64
from Crypto.Cipher import AES

if __name__ == "__main__":
	ciphertext = base64.b64decode(open('10.txt','r').read())
	key = b'YELLOW SUBMARINE'
	IV = bytes(chr(0) * 16)
	
	algorithm = AES.new(key,AES.MODE_ECB,IV)
	res = algorithm.decrypt(ciphertext)
	#print res.encode('hex')
	print ciphertext == algorithm.encrypt(res)
	