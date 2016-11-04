import cryptopal_tools

lines = [line.decode('hex') for line in open('8.txt').read().split()]

for line in lines:
	if cryptopal_tools.isECBencoded(line, 16):
		print line.encode('hex')