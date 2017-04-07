'''from Crypto import Cipher

p = 14388938207215931867
q = 8870679236659621067

n = p*q
print 'N =', n

phi = (p-1)*(q-1)

def gcd(a,b):
	return a if b == 0 else gcd(b,a%b)

e = 1508
while e < phi:
	if gcd(e,phi) == 1:
		break
	e += 1

print 'e =', e

import gmpy2

d = gmpy2.invert(e,phi)

print 'd =', d

print (d*e)%phi

f = open('/Users/minhtt159/message.enc','r').read()

print f.encode('hex')
'''

s = 'Pham'
t = 'Minh'
v = 'Hanh'

def strxor(a,b):
	return ''.join(chr(ord(x)^ord(y)) for (x,y) in zip(a,b)).encode('hex')

print strxor(s,t), strxor(t,v), strxor(v,s)
'''

import string

alphabet = string.ascii_lowercase

print alphabet

s = 'imissyou'

for i in s:
	print (alphabet.index(i) + 1),



