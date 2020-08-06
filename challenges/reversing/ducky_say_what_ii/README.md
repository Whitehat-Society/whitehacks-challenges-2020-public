# Ducky Say What? II

Ducky Say What II is a miscellaneous challenge that involves understanding and decoding of the Ducky Script Language. It is a continuation of Ducky Say What I

# Learning Objective

After completing this challenge, participants will be able to perform reversing on unknown inject.bin files extracted from USB Rubber Ducky drives to figure out what it does

# Description (public)

WhiteHacks Inc. has discovered an attempted social engineering attack. The Incident Response team has worked swiftly to shut the attack down and now they're requesting you to aid them in the investigation. They have managed to provide a binary dump from a thumbdrive used in the attack. Find out what it does.

# Setup Guide

Simply serve inject.bin

# Flag

`WH2020{dUCky_5Ay_Th@t_y0u'r3_g00d}`

# Solution

1. Use the Decoder feature on [DuckToolkit](https://ducktoolkit.com) to discover a bunch of fake flags as well as some hex strings including one starting with `d3d3`.
    * The decoded dump also hints at the libraries needed to decode the flag (`binascii` and `base64`)
2. Solve for the flag using `base64.b64decode(binascii.unhexlify(x[::-1]).decode())` where `x` is the encoded flag.