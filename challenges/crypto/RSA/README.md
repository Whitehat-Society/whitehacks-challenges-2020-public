# RSA

Just a challenge to test basic understanding of how to do RSA decryption.

# Learning Objective

Learn how to decrypt RSA encoded messages given all params needed for decryption.

# Description (public)

```
Let's learn the basics of the [RSA cryptosystem](https://simple.wikipedia.org/wiki/RSA_algorithm)

Download `vals.txt` and decrypt the value of `c` given all the other params.
```

# Setup Guide

1. Provide `vals.txt` to players

# Solution

Solution can be found in [solve.py](solve.py). It's just `print long_to_bytes(pow(c,d,n))`.

# Flag

`WH2020{Great_job_welcome_to_crypto}`
