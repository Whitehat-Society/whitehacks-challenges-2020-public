# x86\_64: Emu

Quiz like challenge asking players to emulate x86\_64 instructions in their head.

# Learning Objective

Learn basic x86\_64 instructions like `mov`, `add`, `sub`.

# Description (public)

```
Did you know the emu is the second fastest running bird, running at speeds of up to 48 km/h.

How fast can you emulate x86_64 code?

`nc whitehacks.ctf.sg 12003`
```

# Setup Guide

1. Use the docker-compose.yml in the parent directory to deploy the service at port 12003
2. Test the service by connection to `nc whitehacks.ctf.sg 12003`

# Flag

`WH2020{x86_64_is_easier_to_read_than_chinese_imo}`

# Solution

Connect to the service and emulate the instructions for 5 rounds. Should be solvable within a minute or two.
