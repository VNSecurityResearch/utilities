import base64
import cryptopal_tools
from Crypto.Cipher import AES

file = open('7.txt','r')
key = b'YELLOW SUBMARINE'

data = base64.b64decode(''.join(line.strip() for line in file))

algorithm = AES.new(key,AES.MODE_ECB)
print cryptopal_tools.reversePKCS7(algorithm.decrypt(data))
