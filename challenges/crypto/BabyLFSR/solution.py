#! /usr/bin/python3

KEYS = [64, 64, 64, 64]
TAPS = [15564440312192434176, 15564440312192434176, 15564440312192434176, 15564440312192434176]

class LSFR:
    def __init__(self, state, seed, length):
        self.taps = seed
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

    def getNext(self):
        return self.func(list(map(lambda x: x.getNext(), self.lsfr)))

    def decrypt(self, message):
        bits = []
        for char in message:
            out = self.func(list(map(lambda x: x.getNext(), self.lsfr)))
            bits.append(char ^ out)
        enc = []
        while bits:
            enc.append(chr(int(''.join(map(str, bits[0:8])), 2)))
            bits = bits[8:]
        return ''.join(enc)

def main():
    file = open("out.out", "r")
    encrypted = list(map(int, ''.join('{0:08b}'.format(ord(x), 'b') for x in file.read())))
    file.close()

    # Recover first 56 bits: WH2020{
    bits = list(map(int, ''.join('{0:08b}'.format(ord(x), 'b') for x in "WH2020{")))
    first56 = [bits[x] ^ encrypted[x] for x in range(56)]
    state56 = int("".join(map(str, first56)), 2)

    for i in range(256):
        state = state56+i*(2**56)
        a = LSFR(state, TAPS[0], KEYS[0])
        cipher = StreamCipher(lambda l:l[0], a)
        text = cipher.decrypt(encrypted[56:])
        if "101" in text:
            print ("WH2020{" + text)

main()
