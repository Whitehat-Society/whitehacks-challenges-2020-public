# RSC

RSA challenge that showcases breaking RSA encryption when e is small and the message (m) is unpadded/small.

# Learning Objective

Learn a slightly more advanced attack against RSA compared to the solution of RSB, while showcasing the importance of padding messages in RSA encryption.

# Description (public)

![](bill.png)

```
Download `vals.txt` and decrypt the value of `c` given all the other params.
```

# Setup Guide

1. Provide `vals.txt` to players

# Solution

Solution can be found in [solve.py](solve.py). Because e is small and m is unpadded, m^e is very close to the value of N. Therefore, `eth root of C+xN` will yield the flag m, and x is a very small number that can be bruteforced. In this case x is 35 so the bruteforce is very fast.

# Flag

`WH2020{Pl3as3_r3memBer_to_pAD_ur_RSA_m3ssag3s!}`
