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

    p = 1210382616638311811127671002945040396700250788514059942029480193728254971290446230978162950231780412350968403235477880179558020526743536345582938762142564355204550634837515892169614110995886000109021922032156152086217522186641285891
    q = 1038230773348892538759982476705146359078984500073224899609220832759702042276483362086750444186117589693310218670793259204196636823452580437561436667417123325560636400972822202219962000226723847731166893443771105427635735671266228137
    n = 1256656480120450597072003081650664247724680264297536167141726306997142058813860712447498826449451514352875011768202001668178501530482872870615464922095824146502601180079982667001473444407850861123511536903340611829437862912575888515400255728038035391942435700006309694619049809051715181593028933225306263279801681907232318764723173740565723029660057614708655761208626229572919039715738878236340790655662803118743086409128997507998047948092769887723393691045315067
    d = 919901386253475983401749539442971899567474406632648865606371741759841751269430940280210348356844253456212742102568575509998571014134453147626703415075883479725259025242287397306902059903488434049148477020196594863790675866659141438756836461842605655983454302680419135793374174667894557241624969942271529883821394786783575922788881637277189395170303224612400741354047935634909960504905747776466599200655225679414623760025494006615084593224809204459203327492889151

    #return p, q, n, d, e

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
