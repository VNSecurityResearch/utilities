import cryptopal_tools

if __name__ == '__main__':
	input = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736".decode('hex')
	print cryptopal_tools.solveSingleBytesXOR(input)