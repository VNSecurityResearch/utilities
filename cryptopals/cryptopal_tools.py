def padPKCS7(a,k):
	ch = k - (len(a)%k)
	return a + (bytes(chr(ch)) * ch)

def padRepeat(a,k):
	res = ""
	for i in range(0,k):
		res += a[i%len(a)]
	return res

def reversePKCS7(a):
	return a[:-ord(a[len(a)-1])]

# MODE
PKCS7 = 0
REPEAT = 1

def padding(a,b,mode):
	if (mode == REPEAT):
		return a,padRepeat(b,len(a))
	elif len(a) > len(b):
		return a, padPKCS7(b,len(a))
	else:
		return padPKCS7(a,len(b)), b

def xorstr(a,b,mode=PKCS7):
	a, b = padding(a,b,mode)
	return ''.join([chr(ord(x)^ord(y)) for (x,y) in zip(a,b)]);

freq = {
	'E' : 12.02,
	'T' : 9.10,
	'A' : 8.12,
	'O' : 7.68,
	'I' : 7.31,
	'N' : 6.95,
	'S' : 6.28,
	'R' : 6.02,
	'H' : 5.92,
	'D' : 4.32,
	'L' : 3.98,
	'U' : 2.88,
	'C' : 2.71,
	'M' : 2.61,
	'F' : 2.30,
	'Y' : 2.11,
	'W' : 2.09,
	'G' : 2.03,
	'P' : 1.82,
	'B' : 1.49,
	'V' : 1.11,
	'K' : 0.69,
	'X' : 0.17,
	'Q' : 0.11,
	'J' : 0.10,
	'Z' : 0.07,
	' ' : 5.00
}

def CheckLegitString(s):
	res = 0
	for i in s:
		c = i.upper()
		if c in freq:
			res += freq[c]
	return res

def solveSingleBytesXOR(s):
	res = ""
	cur_score = 0
	key = 0
	for i in range(0,256):
		temp = ''.join([ chr(i^ord(j)) for j in s])
		if (CheckLegitString(temp) > cur_score):
			cur_score = CheckLegitString(temp)
			res = temp
			key = i
	return res,key,cur_score

def isECBencoded(data, block_size):
	block_count = len(data)/block_size
	for i in range(block_count):
		for j in range(i+1,block_count):
			if data[i*block_size:(i+1)*block_size] == data[j*block_size:(j+1)*block_size]:
				return True
	return False