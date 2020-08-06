from Crypto.Util.number import *
import time

def check(s, x0, x1):
    print ("Running checks...")
    # time.sleep(1)
    return int(str(int(str(x1) + s) % x0) + s) % x1 == 1

def main():
    print("Welcome to the Concat flag printer.")
    print("You will need your token to complete this final verification step.")

    while True:
        # time.sleep(1)

        x0 = getRandomNBitInteger(128)
        x1 = getRandomNBitInteger(128)

        print("Please key in the following numbers into your token:")
        print("Into the red field: " + str(x0))
        print("Into the black field: " + str(x1))

        print("Please type in the final number as given by your token.")
        
        s = input()
        if s == "-1":
            print ("OK, hang on while we fetch another challenge.")
            continue

        try:
            if check(s, x0, x1):
                print ("Thank you. You have been authenticated. Printing flag:")
                print ("WH2020{<CENSORED>}")
            else:
                print ("Sorry, authentication failed.")
                print ("Please check that you have typed in the correct number as displayed on your token.")
        except:
            print ("Your token should have given you a positive number or -1 if an error was detected.")
            print ("Reconnect and try again.")
        return

if __name__=="__main__":
    main()
