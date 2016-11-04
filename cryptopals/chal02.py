import cryptopal_tools

if __name__ == '__main__':
	input = "1c0111001f010100061a024b53535009181c"
	xorstring = "686974207468652062756c6c277320657965"
	#print xorstr(xorstring.decode('hex'),input.decode('hex')).encode('hex')
	print cryptopal_tools.xorstr(input.decode('hex'),xorstring.decode('hex')).encode('hex')