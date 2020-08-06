from Crypto.Util.number import long_to_bytes, bytes_to_long
from Crypto.Util import number

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

p = number.getPrime(100)
q = number.getPrime(100)
n = p*q
phi = (p-1)*(q-1)
e = 65537
m = bytes_to_long("WH2020{B1gg3r_primes!}")
d = modinv(e, phi)
c = pow(m, e, n)

print "p = {}".format(p)
print "q = {}".format(q)
print "n = {}".format(n)
print "e = {}".format(e)
print "d = {}".format(d)
print "c = {}".format(c)
print long_to_bytes(pow(c,d,n))
