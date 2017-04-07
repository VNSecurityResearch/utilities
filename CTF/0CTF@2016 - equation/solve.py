import base64,math

line = open('mask.txt','r').read()
def convert_file(a):
	result = []
	i = 0
	while (i < len(a)):
		if a[i].encode('hex') == '02':
			length = int(a[i+1].encode('hex'),16)
			value = int(a[i+2:i+2+length].encode('hex'),16)
			result.append(value)
			print value
			i += 2 + length
		else: 
			i += 1
	return tuple(result)
dp, dq, qinv = convert_file(base64.b64decode(line))
e = int(b'010001',16)

# Fermat algorithm
def is_prime(num):
    if num == 2:
        return True
    if not num & 1:
        return False
    return pow(2, num-1, num) == 1

def recover_rsa(dp,dq,qinv,e):
	results = []
	d1p = dp * e - 1
	for k in range(3, e):
		if d1p % k == 0:
			hp = d1p // k
			p = hp + 1
			if is_prime(p):
				d1q = dq * e - 1
				for m in range(3, e):
					if d1q % m == 0:
						hq = d1q // m
						q = hq + 1
						if is_prime(q):
							if (qinv * q) % p == 1 or (qinv * p) % q == 1:
								results.append((p, q, e))
								print(p, q, e)
	return results

p,q,e = recover_rsa(dp,dq,qinv,e)[0]

from Crypto.Util.number import *

def egcd(a,b):
	u,u1 = 1,0
	v,v1 = 0,1
	while(b):
		q = a // b
		u, u1 = u1, u - q * u1
		v, v1 = v1, v - q * v1
		a, b = b, a - q * b
	return u

def get_d(p,n,e):
	q = n / p
	phi = (p - 1) * (q - 1)
	d = egcd(e, phi)
	if d < 0:
		d += phi
	return d

f = open('flag.enc','rb').read()
n = p*q
ct = bytes_to_long(f)
d = get_d(p,n,e)
pt = pow(ct,d,n)
print long_to_bytes(pt)