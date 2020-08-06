# Who is my Waifu

Brute force attack on a badly implemented bag style LCG PRNG.

# Learning Objective

LCGs are PRNG with period as large as the modulus, but since they have only 2 params which are limited by the modulus, it is easy to brute force if you know the modulus is small.

# Description (public)

```
Can you guess our waifus?

nc whitehacks.ctf.sg 10002
```

# Setup Guide

1. Use the `docker-compose.yml` in the parent directory to deploy the service at port 10002
2. Test the service using netcat and `exploit.py`

# Flag

`WH2020{L1near_C0ngruenCe_Sh1pGirLS}`

# Solution

Brute force the params. This gives 131\*131 ~ 17k combinations. Arbitrarily assign shipgirls numbers that comes out of the LCG. If a ship girl appears twice in the ouptut, prune the tree of LCG param pairs that do not generate a matching number when generated at the two indices.

Proof of concept solution in [solution.py](solution.py)

Match the shipgirl's names to their index in the shipgirls array and print.

Because I want to limit the number of times you can guess for this challenge, there is a small chance a new ship girl that is not correlated with any number yet is the next waifu. Tough luck if it happens, just spin up a new instance I guess...
