import random

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

    def __init__(self):
        self.shipgirls = [
            "Aulick", "Beagle", "Benson", "Bulldog", "Cassin", "Comet", "Craven", "Crescent", "Cygnet", "Downes", "Foote", "Foxhound", "Kisaragi", "McCall", "Mikazuki", "Minazuki", "Mutsuki", "Shiranui", "Spence", "Uzuki", "Z20", "Z21",
            "Acasta", "Akatsuki", "Amazon", "Arashio", "Ardent", "Ariake", "Asashio", "Aylwin", "Bache", "Bailey", "Bush", "Dewey", "Echo", "Fletcher", "Forbin", "Fortune", "Fumizuki", "Gridley", "Halsey Powell", "Hamakaze", "Hammann", "Hatakaze", "Hatsuharu", "Hatsushimo", "Hazelwood", "Hobby", "Ikazuchi", "Inazuma", "Isokaze", "Jenkins", "Jersey", "Juno", "Jupiter", "Kagerou", "Kalk", "Kamikaze", "Kimberly", "Kiyonami", "Kuroshio", "Le Mars", "Matsukaze", "Michishio", "Mullany", "Nagatsuki", "Ooshio", "Oyashio", "Radford", "San Juan", "Shiratsuyu",
            "Sims", "Smalley", "Stanly", "Tanikaze", "Thatcher", "Urakaze", "Wakaba", "Yuugure", "Z18", "Z19", "Z36",
            "An Shan", "Ayanami", "Carabiniere", "Chang Chun", "Charles Ausburne", "Cooper", "Fu Shun", "Fubuki", "Glowworm", "Grenville", "Grozny", "Hanazuki", "Harutsuki", "Hibiki", "Javelin", "Kasumi", "L Opiniatre", "Laffey", "Le Temeraire", "Makinami", "Matchless", "Maury", "Minsk", "Musketeer", "Naganami", "Nicholas", "Niizuki", "Nowaki", "Shigure", "Tai Yuan", "Tartu", "Universal Bulin", "Uranami", "Vampire", "Vauquelin", "Yoizuki", "Z1", "Z23", "Z25", "Z35",
            "Eldridge", "Kawakaze", "Le Malin", "Le Triomphant", "Prototype Bulin MKII", "Tashkent", "Yudachi", "Yukikaze", "Z46"
        ]
        # PROOF OF CONCEPT. GENERATE RANDOM a AND b:
        a = random.randrange(len(self.shipgirls))
        b = random.randrange(len(self.shipgirls))
        print(a,b, len(self.shipgirls))
        self.lcg = LCG(a, b, len(self.shipgirls))

    def get_next(self):
        return self.lcg.get_next()

shipgirls = [
            "Aulick", "Beagle", "Benson", "Bulldog", "Cassin", "Comet", "Craven", "Crescent", "Cygnet", "Downes", "Foote", "Foxhound", "Kisaragi", "McCall", "Mikazuki", "Minazuki", "Mutsuki", "Shiranui", "Spence", "Uzuki", "Z20", "Z21",
            "Acasta", "Akatsuki", "Amazon", "Arashio", "Ardent", "Ariake", "Asashio", "Aylwin", "Bache", "Bailey", "Bush", "Dewey", "Echo", "Fletcher", "Forbin", "Fortune", "Fumizuki", "Gridley", "Halsey Powell", "Hamakaze", "Hammann", "Hatakaze", "Hatsuharu", "Hatsushimo", "Hazelwood", "Hobby", "Ikazuchi", "Inazuma", "Isokaze", "Jenkins", "Jersey", "Juno", "Jupiter", "Kagerou", "Kalk", "Kamikaze", "Kimberly", "Kiyonami", "Kuroshio", "Le Mars", "Matsukaze", "Michishio", "Mullany", "Nagatsuki", "Ooshio", "Oyashio", "Radford", "San Juan", "Shiratsuyu",
            "Sims", "Smalley", "Stanly", "Tanikaze", "Thatcher", "Urakaze", "Wakaba", "Yuugure", "Z18", "Z19", "Z36",
            "An Shan", "Ayanami", "Carabiniere", "Chang Chun", "Charles Ausburne", "Cooper", "Fu Shun", "Fubuki", "Glowworm", "Grenville", "Grozny", "Hanazuki", "Harutsuki", "Hibiki", "Javelin", "Kasumi", "L Opiniatre", "Laffey", "Le Temeraire", "Makinami", "Matchless", "Maury", "Minsk", "Musketeer", "Naganami", "Nicholas", "Niizuki", "Nowaki", "Shigure", "Tai Yuan", "Tartu", "Universal Bulin", "Uranami", "Vampire", "Vauquelin", "Yoizuki", "Z1", "Z23", "Z25", "Z35",
            "Eldridge", "Kawakaze", "Le Malin", "Le Triomphant", "Prototype Bulin MKII", "Tashkent", "Yudachi", "Yukikaze", "Z46",
        ]

length = len(shipgirls)
possible = {(x, y) for x in range(1, length) for y in range(1, length)}

gacha = Gacha()

out = []
# Simulate 200 events. 
for i in range(200):
    out.append(gacha.get_next())

# Find at which position numbers have appeared before:
appeared_before = {}
for i in range(len(out)):
    try:
        appeared_before[out[i]].append(i)
    except:
        appeared_before[out[i]] = [i]

    # We have seen these numbers before:
    if len(appeared_before[out[i]]) > 1:
        new_set = set()

        for lcgpair in possible:
            lcg = LCG(lcgpair[0], lcgpair[1], length)
            
            seq = []            

            for _ in range(appeared_before[out[i]][-1] + 1):
                seq.append(lcg.get_next())

            if (seq[appeared_before[out[i]][-1]] == seq[appeared_before[out[i]][-2]]):
                new_set.add(lcgpair)

        possible = new_set

    if len(possible) == 1:
        break

# PROOF OF CONCEPT: This spits out the only possible inputs for A and B
print(possible)
