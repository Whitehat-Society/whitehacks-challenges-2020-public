# No F No Respects 2

2 Part challenge on reversing x86 code.

# Learning Objective

Reverse engineering of assembly with a small CP twist.

# Description (public)

```
The token they gave me runs so slowly. I managed to get out the code that is running on the device, could you help me?

Now that you have my password, the program should start generate the flag. Enter the flag as output by the program as the flag submission.

Note: This is the same binary as No F No Respects 1.
```

# Setup Guide

Serve `output`.

# Flag

`WH2020{834448324}`

# Solution

This is a basic CP problem: Find the number of odd numbers below the given input such that the digit F doesn't appear. Since we are dealing with base 16, for a given digit at position k != 0 counting from the back, the number of numbers is given by 7\*15\*\*(k-1). Solution code is in [solution.py](solution.py)

Things to look out for:

- A-F encodes for 0-5 and not 0xA-0xF.
- You need to mod 2\*\*32 since we used an int.
