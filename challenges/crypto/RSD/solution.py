n = 1256656480120450597072003081650664247724680264297536167141726306997142058813860712447498826449451514352875011768202001668178501530482872870615464922095824146502601180079982667001473444407850861123511536903340611829437862912575888515400255728038035391942435700006309694619049809051715181593028933225306263279801681907232318764723173740565723029660057614708655761208626229572919039715738878236340790655662803118743086409128997507998047948092769887723393691045315067
e = 8191
c = 343292776895766888536083165351571730259730847918073317720388964013126703879113072037337018621254488725392807393703102067179576752962271235265003850560159896570099387748975815369717320538910649490423861836151069785424337613650101432092061245157827793583837044758877052640267613461602073836793757063314846174582455147237978374748983176551367801974611709632446290708494931592678353919903470747849541699038339713277417890971635019860750612131243547422949513961547785
p = -1
q = -1

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

def RSADecrypt(c, n, d):
    return decod(pow(c, d, n))

# Totally not copied 
def nth_root(x, n):
    # Start with some reasonable bounds around the nth root.
    upper_bound = 1
    while upper_bound ** n <= x:
        upper_bound *= 2
    lower_bound = upper_bound // 2
    # Keep searching for a better result as long as the bounds make sense.
    while lower_bound < upper_bound:
        mid = (lower_bound + upper_bound) // 2
        mid_nth = mid ** n
        if lower_bound < mid and mid_nth < x:
            lower_bound = mid
        elif upper_bound > mid and mid_nth > x:
            upper_bound = mid
        else:
            # Found perfect nth root.
            return mid
    return mid + 1

def quad(a, b, c):
    orig = b*b - 4*a*c
    det = nth_root(orig, 2)
    if det**2 != orig:
        return -1

    if (det - b) % (2*a) != 0:
        return -1

    p = (-b + det)/(2*a)
    return p

# xp**2 + p - ne = 0

for x in range(1,10000):
    p = quad(x, 1, -n*e)
    if (p == -1):
        continue
    
    if (n % p != 0):
        continue

    q = n / p # Happens at x = 7026
    break

tot = (p-1)*(q-1)
d = modinv(e, tot)

print(RSADecrypt(c, n, d))
