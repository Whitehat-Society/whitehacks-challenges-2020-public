# Raising Morales (PPC)

Competitive Programming Challenge.

# Learning Objective

Challenge CP problem. Maybe some googling might help? The concept is based off /alehouse on Kattis.

# Description (public)

```
Nat H. Tennek looks over the damage report of his shipgirls from their recent sorties. All these shipgirls would need to rest in the docks it seems... Since he is allowed one break of some duration, he can use this time to go to the docks and interact with the recovering shipgirls, raising their morales.

Given the shipgirl's schedules (the time they enter and leave the docks), help Nat H. Tennek figure out the maximum number of shipgirls he can interact with.

The first line of each test case consists of the number of shipgirl groups and the amount of time off Nat H. Tennek has.

The next n lines consists of 3 numbers: the time the group of shipgirls enter the docks, the time they exit the dock, and the number of girls in the group.

All times are represents the number of years since the start of epoch time. Output on a single line the maximum number of shipgirls Nat H. Tennek can interact by visiting the docks once during his time off.

Sample In 1:
4 0.2
0.0 1.7 1
1.2 1.7 4
1.9 2.4 2
2.0 3.0 4

Sample Out 1:
7

Explanation 1:
Enter the docks from t = 1.7 - 1.9 to meet the first 3 groups of ship girls (1 + 4 + 2 = 7).

Sample In 2:
4 0.2
0.0 1.7 1
1.2 1.7 4
1.9 2.4 2
2.0 3.0 6

Sample Out 2:
8

Explanation 2:
Enter the docks from t = 2.3 - 2.5 to meet the last 2 groups of ship girls (2 + 6 = 8).


Your code will be tested on multiple test cases. There are 2 flags:
- 1. Solve for n < 4200
- 2. Solve for n < 255000

nc chals.whitehacks.ctf.sg 11004
```

# Setup Guide

1. Use the `docker-compose.yml` in the parent directory to deploy the service at port 11004
2. Test the service using netcat

# Flag

- Flag 1 (Small Testcase): `WH2020{M0Ra1e_b00st3D}`
- Flag 2 (Large Testcase): `WH2020{0pt1m@l_m0r4l3}`

# Solution

Event queue CP. Solution is also coded alongside [morale.py](morale.py).
