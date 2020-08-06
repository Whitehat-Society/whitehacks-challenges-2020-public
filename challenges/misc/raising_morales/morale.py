from random import uniform, randint, triangular

def solve(girls, time):
    event_queue = []
    for tup in girls:
        event_queue.append((tup[0], tup[2]))
        event_queue.append((tup[1] + time, -tup[2]))

    event_queue.sort()
    best = -1
    curr = 0
    for event in event_queue:
        curr += event[1]
        best = max(best, curr)
    return best


def question(n):
    num_girls = int(2*(1.8**n))
    girls = []
    for i in range(num_girls):
        time1 = uniform(1, 2**n)
        time2 = uniform(1, 2**n)
        if (time1 > time2):
            time2, time1 = time1, time2

        girls.append((time1, time2, int(triangular(1, n**3))))

    time = 1
    for i in range(n):
        time *= uniform(1.4, 1.85)

    print(num_girls, time)

    for tup in girls:
        print(" ".join(map(str, tup)))

    return solve(girls, time)

def main():
    for i in range(1, 21):
        sol = question(i)

        if (int(input()) != sol):
            print("Sorry. Wrong Answer")
            return
        else:
            print("Corrct Answer. Good Job")
            if (i == 13):
                print("Oh congrats, here is the flag for smol testcase:")
                print("WH2020{M0Ra1e_b00st3D}")

    print ("Oh congrats, here is the flag for large testcase:")
    print("WH2020{0pt1m@l_m0r4l3}")


if __name__ == '__main__':
    main()