import itertools

def hammingDistance(a,b):
	return sum([bin(ord(i)^ord(j)).count('1') for (i,j) in zip(a,b)])


def findKeyLength(s):
	res = len(41)
	for k in range(2,40):
		blocks = [s[i:i+k] for i in range(0,len(s),k)]
		pairs = list(itertools.combination(blocks,2))
		

file = open('chal6.inp','r').read()
file = base64.b64decode(file)

#test
x = "this is a test"
y = "wokka wokka!!!"
print hammingDistance(x,y)
#done

length = findKeyLength(file)

print key, chal5.solvePaddingXOR(key,file)


