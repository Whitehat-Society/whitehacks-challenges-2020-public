from Crypto.Util.number import *
import sympy

# Totally not from geekforgeeks
def modinv(a, m): 
    m0 = m 
    y = 0
    x = 1
  
    if (m == 1) : 
        return 0
  
    while (a > 1) : 
  
        # q is quotient 
        q = a // m 
  
        t = m 
  
        # m is remainder now, process 
        # same as Euclid's algo 
        m = a % m 
        a = t 
        t = y 
  
        # Update x and y 
        y = x - q * y 
        x = t 
  
  
    # Make x positive 
    if (x < 0) : 
        x = x + m0 
  
    return x 

def decod(k):
    o = ""
    while k > 0 :
        o = chr(k%256) + o
        k = k >> 8
    return o

def encod(s):
    o = 0
    for i in s:
        o = o * 256 + ord(i)
    return o

def RSAEncrypt(p, n, e):
    return pow(encod(p), e, n)

def RSADecrypt(c, n, d):
    return decod(pow(c, d, n))

def setup():
    e = 2**13 - 1 # You think it is 65537, BUT IT'S ME! 8191!

    while True:
        # Generate primes
        p = q = 4
        while not sympy.isprime(p):
            p = getRandomNBitInteger(768)
        while not sympy.isprime(q):
            q = getRandomNBitInteger(768)

        # Set up decryption keys, do the mod inverse thing
        # TODO: Check if this code is working correctly
        q = modinv(e, p)
        tot = (p-1)*(q-1)
        d = modinv(e, tot)

        # Don't forget n
        n = p*q

        # For some reason, q is sometimes not a prime...
        if sympy.isprime(q):
            break
        else:
            print("q is not prime! Regenerating RSA constants")

    return p, q, n, d, e

def main():
    p, q, n, d, e = setup()

    # Make sure encrypt(decrypt("somestring")) works:
    while (RSADecrypt(RSAEncrypt("somestring", n, e), n, d) != "somestring"):
        print("RSA check fail...")
        p, q, n, d, e = setup()

    while True:
        print("What do you want to do?")
        action = input()

        if (action == 'encrypt'):
            print ("What is your message: ")
            plain = input()

            c = RSAEncrypt(plain, n, e)

            print ("Here it is:")
            print (f"n = {n}")
            print (f"e = {e}")
            print (f"c = {c}")
        if (action == 'decrypt'):
            print ("What is the ciphertext number?: ")
            c = input()
            
            plain = RSADecrypt(int(c), n, d)

            print ("Here it is:")
            print (plain)

        if (action == "quit"):
            print ("Goodbye!")
            break

if __name__ == "__main__":
    main()
