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

n = 702920415766607170773466108765523213222609807958470426429279
e = 65537
c = 471942432444013498766618748088184020223806593029552824676187

# from alpetron (https://www.alpertron.com.ar/ECM.HTM)
p = 757797040104296557573809656933
q = 927584008074066047910168872563
assert p*q == n

# decrypt
phi = (p-1)*(q-1)
d = modinv(e, phi)

print long_to_bytes(pow(c,d,n))
