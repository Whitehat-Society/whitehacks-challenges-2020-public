# BabyLFSR

Badly implemented LFSR touting high security.

# Learning Objective

Demonstrates how a badly designed LFSR system can be broken by known plantext attack and brute force.

# Description (public)

```
My 256 bit key is unbreakable.

Note: The flag's text is an intellegible message. For extra verification, the string 101 should appear in the flag.
```

# Setup Guide

Serve `encryptCensored.py` and `out.out` in `dist`.

# Flag

`WH2020{Same_Key_Length_XOR_LFSR_Is_Not_Proper_LFSR_101}`

# Solution

Solution can be found in [solution.py](solution.py). Since we have LFSR that are being XOR'ed together, and they are of the same length, we can essentially treat them as only one single LFSR. Knowing the first 7 characters of the flag, you can simply reverse the state of the agglomerated LFSR and brute force the last bit.
