import math

def main():
    print ("Red field: ")
    x0 = int(raw_input())
    print ("")
    print ("Black field: ")
    x1 = int(raw_input())
    print ("")

    def xgcd(b, a):
        x0, x1, y0, y1 = 1, 0, 0, 1
        while a != 0:
            q, b, a = b // a, a, b % a
            x0, x1 = x1, x0 - q * x1
            y0, y1 = y1, y0 - q * y1
        return  b, abs(x0), abs(y0)

    gcd, x, y = xgcd(x1,x0)

    if gcd != 1:
        print("Error: -1")
        return

    # print x0*x - x1*y
    if x0*x - x1*y != 1:
        x, y = y, x

    # print x0*x - x1*y
    if x0*x - x1*y == -1:
        x, y = -x, -y

    # print x0*x - x1*y
    if x0*x - x1*y != 1:
        print ("Error: -1")
        return

    increase = y
    dx = x0*x

    # print x0*x - x1*y

    while True:
        increase += dx
        out = str(increase)
        # print (len(out))
        if (len(out) > 2000):
            print "Error: -1"
            break
        if out[0] == "1":
            if len(str(int(out[1:]) * x1 + 1)) + 1 == len(out):
                #print increase
                print "Please enter: ", int(out[1:])*x1+1
                break
            else:
                increase = int("2" + out[1:])
        else:
            nexta = int("1" + len(out) * "0")
            leftovers = nexta % dx
            increase = (nexta - leftovers) + y
            if leftovers < y:
                increase -= dx

main()
