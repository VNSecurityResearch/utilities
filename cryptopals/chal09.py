import cryptopal_tools

if __name__ == "__main__":
	x = b'YELLOW SUBMARINE'
	t = cryptopal_tools.padPKCS7(x,20)
	expected = b'YELLOW SUBMARINE\x04\x04\x04\x04'
	print t == expected