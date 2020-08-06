import sys
from Crypto.Util import number
from Crypto.Util.number import long_to_bytes, bytes_to_long

def egcd(a, b):
	if a == 0:
		return (b, 0, 1)
	else:
		g, y, x = egcd(b % a, a)
		return (g, x - (b // a) * y, y)

def modinv(a, m):
	g, x, y = egcd(a, m)
	if g != 1:
		raise Exception('modular inverse does not exist')
	else:
		return x % m

while True:
	try:
		p = number.getPrime(934)
		q = number.getPrime(934)
		n = p*q
		phi = (p-1)*(q-1)
		e = 5
		m = bytes_to_long("WH2020{Pl3as3_r3memBer_to_pAD_ur_RSA_m3ssag3s!}")
		d = modinv(e, phi)
		c = pow(m, e, n)
		break
	except:
		continue

if pow(m, e) < n:
	print >> sys.stderr, "{}".format(n/pow(m,e))
	raise Exception("haiz")
else:
	print >> sys.stderr, "{}".format(pow(m,e)/n)


print "p = {}".format(p)
print "q = {}".format(q)
print "n = {}".format(n)
print "e = {}".format(e)
print "d = {}".format(d)
print "c = {}".format(c)
print long_to_bytes(pow(c,d,n))
