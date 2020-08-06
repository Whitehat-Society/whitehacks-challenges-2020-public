from pwn import *

class LCG():
    def __init__(self, a, v, mod): 
        self.a = a
        self.v = v
        self.mod = mod
        self.counter = 0

    def next_bag(self):
        self.v += self.a
        self.value = 1

    def get_next(self):
        if self.counter == 0:
            self.next_bag()
            self.counter = self.mod // 2

        self.value = (self.a * self.value + self.v) % self.mod
        self.counter -= 1
        return self.value

class Gacha():
    def __init__(self, a, b):
        self.lcg = LCG(a, b, len(shipgirls))

    def get_next(self):
        return self.lcg.get_next()

shipgirls = [
    "Aulick", "Beagle", "Benson", "Bulldog", "Cassin", "Comet", "Craven", "Crescent", "Cygnet", "Downes", "Foote", "Foxhound", "Kisaragi", "McCall", "Mikazuki", "Minazuki", "Mutsuki", "Shiranui", "Spence", "Uzuki", "Z20", "Z21",
    "Acasta", "Akatsuki", "Amazon", "Arashio", "Ardent", "Ariake", "Asashio", "Aylwin", "Bache", "Bailey", "Bush", "Dewey", "Echo", "Fletcher", "Forbin", "Fortune", "Fumizuki", "Gridley", "Halsey Powell", "Hamakaze", "Hammann", "Hatakaze", "Hatsuharu", "Hatsushimo", "Hazelwood", "Hobby", "Ikazuchi", "Inazuma", "Isokaze", "Jenkins", "Jersey", "Juno", "Jupiter", "Kagerou", "Kalk", "Kamikaze", "Kimberly", "Kiyonami", "Kuroshio", "Le Mars", "Matsukaze", "Michishio", "Mullany", "Nagatsuki", "Ooshio", "Oyashio", "Radford", "San Juan", "Shiratsuyu",
    "Sims", "Smalley", "Stanly", "Tanikaze", "Thatcher", "Urakaze", "Wakaba", "Yuugure", "Z18", "Z19", "Z36",
    "An Shan", "Ayanami", "Carabiniere", "Chang Chun", "Charles Ausburne", "Cooper", "Fu Shun", "Fubuki", "Glowworm", "Grenville", "Grozny", "Hanazuki", "Harutsuki", "Hibiki", "Javelin", "Kasumi", "L Opiniatre", "Laffey", "Le Temeraire", "Makinami", "Matchless", "Maury", "Minsk", "Musketeer", "Naganami", "Nicholas", "Niizuki", "Nowaki", "Shigure", "Tai Yuan", "Tartu", "Universal Bulin", "Uranami", "Vampire", "Vauquelin", "Yoizuki", "Z1", "Z23", "Z25", "Z35",
    "Eldridge", "Kawakaze", "Le Malin", "Le Triomphant", "Prototype Bulin MKII", "Tashkent", "Yudachi", "Yukikaze", "Z46"
]

def main():
    global conn
    conn = remote('chals.whitehacks.ctf.sg', 10002)

    # Print all the bullshit
    conn.recvline()
    conn.recvline()
    conn.recvline()
    conn.recvline()
    conn.recvline()
    conn.recvline()
    conn.recvline()

    for i in range(4500):
        conn.send("\n")

    out = []
    for i in range(4500):
        #if (i % 500 == 0): print(i)
        conn.recvuntil("waifu is ")
        a = conn.recvline().strip()
        out.append(a)

    # Set up all possible 
    length = len(shipgirls)
    possible = {(x, y) for x in range(1, length) for y in range(1, length)}

    for tup in possible:
        gacha = Gacha(tup[0], tup[1])
        yes = True # Is it still possible?

        mapping = {}
        rev_mapping = {}

        # Match each ship to the output
        for ship in out:
            next_num = gacha.get_next()

            # Check if the ship is correct
            if ship not in mapping:
                mapping[ship] = next_num
                rev_mapping[next_num] = ship
            # Check if the mapping makes sense
            elif mapping[ship] != next_num:
                yes = False
                break
        
        if yes:
            # Then generate 250 ships:
            for i in range(250):
                next_num = gacha.get_next()
                if next_num in rev_mapping:
                    conn.send(rev_mapping[next_num])
                    conn.send("\n")
                else:
                    print("shit, something went wrong")
                    print(panic)

        else:
            continue

        conn.recvuntil("HERE FLAG: ")
        print(conn.recvline()[:-1]) 

if __name__ == '__main__':
    main()