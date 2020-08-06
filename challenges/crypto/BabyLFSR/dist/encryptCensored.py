#! /usr/bin/python3
import random

KEYS = [64, 64, 64, 64]
TAPS = [15564440312192434176, 15564440312192434176, 15564440312192434176, 15564440312192434176]

class LSFR:
    def __init__(self, state, taps, length):
        self.taps = taps
        self.state = state
        self.length = 2**length

    def getNext(self):
        out = 0
        xored = self.taps & self.state
        while xored > 0:
            if xored % 2 == 1:
                out = 1 - out
            xored //= 2
        self.state = (self.state*2 + out)%self.length
        return out

class StreamCipher:
    def __init__(self, func, *args):
        self.lsfr = list(args)
        self.func = func

    def encrypt(self, string):
        bits = []
        key = []
        for char in string:
            out = self.func(list(map(lambda x: x.getNext(), self.lsfr)))
            bits.append(char ^ out)
            key.append(out)
        enc = []
        while bits:
            enc.append(chr(int(''.join(map(str, bits[0:8])), 2)))
            bits = bits[8:]
        return ''.join(enc)

def main():
    # Unbruteforcable 256 bit key muahahaha
    seed = random.randrange(2**sum(KEYS))

    # Seeding
    a = LSFR(seed % 2**KEYS[0], TAPS[0], KEYS[0]); seed //= 2**KEYS[0]
    b = LSFR(seed % 2**KEYS[1], TAPS[1], KEYS[1]); seed //= 2**KEYS[1]
    c = LSFR(seed % 2**KEYS[2], TAPS[2], KEYS[2]); seed //= 2**KEYS[2]
    d = LSFR(seed % 2**KEYS[3], TAPS[3], KEYS[3]); seed //= 2**KEYS[3]

    flag = "WH2020{<CENSORED>}"
    flag = map(int, ''.join('{0:08b}'.format(ord(x), 'b') for x in flag))

    cipher = StreamCipher(lambda l:l[0]^l[1]^l[2]^l[3], a, b, c, d)
    file = open("out.out", "w")
    file.write(cipher.encrypt(flag))
    file.close()

main()
