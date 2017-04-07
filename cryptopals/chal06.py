import itertools
import base64

def hammingDistance(a,b):
	return sum([bin(ord(i)^ord(j)).count('1') for (i,j) in zip(a,b)])

def findKeyLength(s):
	res = len(41)
	for k in range(2,40):
		blocks = [s[i:i+k] for i in range(0,len(s),k)]
		pairs = list(itertools.combination(blocks,2))
		

file = open('6.txt','r').read()
file = base64.b64decode(file)

#test
x = "this is a test"
y = "wokka wokka!!!"
print hammingDistance(x,y)
#done

output = open('6_b64decode.txt','w')
output.write(file)

xortool 6_b64decode.txt -l 29 -o 
key = Terminator X3a Bring the noise