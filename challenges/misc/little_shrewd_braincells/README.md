# Little Shrewd Braincells

Little Shrewd Braincells is a simple audio file challenge that contains the flag hidden using LSB steganography.

# Learning Objective

After completing this, students will be able to identify common steganography techniques used in WAV files.

# Description (public)

Special Forces have raided a known underworld arms dealer who specialises in dealing in the Dark Web. To recover the funds from his crypto wallet, they require a passphrase to correctly decode the keys. After much digital forensic investigations, they discovered that right before he made any significant transactions, he was known to access a particular music file. Could the secret key be somehow hidden in it?

# Setup Guide

Simply serve the .zip file

# Solution

You can solve for the flag by either:

* Run `decode.py`.
* Using the `stego-lsb` python package, run `stegolsb wavsteg -r -i bensound-creativeminds.wav -o output.txt -n 1 -b 1000`

Flag: `WH2020{l1ttl3_b1t_@l50_c@n_f1nd_m3}`
