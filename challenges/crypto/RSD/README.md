# RSD

When your primes are dependent on each other, you are looking at a world of pain.

# Learning Objective

Do some fun math and break the RSA keys.

# Description (public)

```
Someone sent me this stupid encryption thing which doesn't even work half the time.
Today, I managed to capture all its output when it just happened to work.
```

# Setup Guide

1. Provide `generator.py` and `out.txt` to players

# Solution

If `q = e**-1 (mod p)`, then `qe = 1 (mod p) = xp + 1`, for some `x`.

Multiply both sides by p to get `pqe = (xp**2 + p) = ne` (because `pq = n`).

Then we have a quadratic in terms of p. Solve the quadratic equation by bruteforcing the value of `x`.

Note that `x ~ e` because `q < p` and `qe = xp + 1`. Hence bruteforing the value of `x` is possible.

Solution code is in [solution.py](solution.py)

# Flag

`WH2020{Roses_are_Red__Bad_RSA__ThErE_iS_No_wAr_iN_Ba_sInG_Se}`
