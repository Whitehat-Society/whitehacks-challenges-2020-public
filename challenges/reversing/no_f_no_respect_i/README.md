# No F No Respects 1

2 Part challenge on reversing x86 code.

# Learning Objective

Reverse engineering of assembly with a small CP twist.

# Description (public)

```
The token they gave me runs so slowly. I managed to get out the code that is running on the device, could you help me?

Im sorry, I can't give you my password, but Im sure you can figure it out. The flag for this challenge is WH2020{<my password>}.

Note: This is the same binary as No F No Respects 2.
```

# Setup Guide

Serve `output`.

# Flag

`WH2020{FEEDDADACEBEEF}`

# Solution

Reverse the code to find out the password checks. 2 ways: Notice that the password is 14 characters from A-F. Either bruteforce (6\*\*14 = 78B = ~3 minutes), work the math (it's 3 xor equations) or use z3.
