from Crypto.Cipher import AES
import cryptopal_tools

key = None
IVs = None

def enc(userdata):
	global key,IVs
	if key == None:
		key = cryptopal_tools.randBytes(16)
	if IVs == None:
		IVs = cryptopal_tools.randBytes(16)
	x1 = "comment1=cooking%20MCs;userdata="
	x2 = ";comment2=%20like%20a%20pound%20of%20bacon"
	userdata = userdata.replace(';','%3B').replace('=','%3D')
	params = x1 + userdata + x2
	cipher = AES.new(key,AES.MODE_CBC,IVs)
	return cipher.encrypt(cryptopal_tools.padPKCS7(params,16))

print enc("").encode('hex')