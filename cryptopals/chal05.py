import cryptopal_tools

if __name__ == '__main__':
	s = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"

	print cryptopal_tools.xorstr(s,'ICE',cryptopal_tools.REPEAT).encode('hex')
