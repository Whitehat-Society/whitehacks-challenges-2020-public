print("Enter the password as in part 1")
a = input()
b = [(7*15**i) % 2**32 for i in range(len(a)-1)]
b.reverse()

out = 0

for i in range(len(a)-1):
    char = ord(a[i]) - ord('A')
    out += char * b[i]

out += (ord(a[-1]) - ord('A')) // 2 + 1

out %= 2**32
if out > 2**31:
    out = -(2**32 - out)
  
print(f"WH2020{{{out}}}")
