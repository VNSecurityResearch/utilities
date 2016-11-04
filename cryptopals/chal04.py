import cryptopal_tools

file = open("4.txt",'r')
res = ""
score = 0

for line in file:
	if line[-1] == '\n': 
		line = line[:-1]
	curRes,curKey,curScore = cryptopal_tools.solveSingleBytesXOR(line.decode('hex'))
	if score < curScore: res,score = curRes,curScore

print res