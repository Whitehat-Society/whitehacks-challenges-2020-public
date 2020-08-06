# RSB

RSA challenge that requires them to factorise a small public modulus (N) to decrypt the encrypted text.

# Learning Objective

Understand the process of generating decryption exponent (d), and learn the basic assumption of RSA that N must be very large and difficult to factorise in order to have proper encryption.

# Description (public)

```
Let's kick it up a notch. Bob generated these RSA parameters and was certain that his encryption would be unbreakable because his smartest friend (John) couldn't crack it. Is it truly secure?

Download `vals.txt` and decrypt the value of `c` given all the other params.
```

# Setup Guide

1. Provide `vals.txt` to players

# Solution

Solution can be found in [solve.py](solve.py). The value of N is small and can be factorised in a short time by [alpetron](https://www.alpertron.com.ar/ECM.HTM). Decryption key can then be generated once N has been factorised.

# Flag

`WH2020{B1gg3r_primes!}`
