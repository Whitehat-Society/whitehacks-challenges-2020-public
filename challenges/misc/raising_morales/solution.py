from pwn import *

def solve():
    events = []

    dlist = conn.recvline().split()
    n = int(dlist[0])
    t = float(dlist[1])

    for i in range(n):
        girls = conn.recvline().split()
        events.append((float(girls[0]), int(girls[2])))
        events.append((float(girls[1]) + t, -int(girls[2])))

    events.sort()

    best = -1
    curr = 0

    for i in events:
        curr += i[1]
        best = max(best, curr)

    conn.send(str(best))
    conn.send("\n")
    print(best)

def main():
    global conn
    conn = remote('chals.whitehacks.ctf.sg', 11004)

    for i in range(1, 21):
        solve()
        print(conn.recvline())

        if (i == 13 or i == 20):
            print(conn.recvline())
            print(conn.recvline())

if __name__ == '__main__':
  main()