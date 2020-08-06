# Blue Alley

Blue Alley is a OSINT-based challenge for identifying images whose pixels have been overlaid on top of each other.

# Learning Objective

After completing this challenge, students will be able to better search Google for identifying traits of characters in the challenge image. Also, some programming skills can be honed when calculating part of the flag

# Description (public)

Now here's a challenge for you fans of games and anime. A popular gacha side-scrolling video game that involves anthropomorphized battleships has recently concluded its anime adaptation. There are 3 characters whose designs are overlaid on top of one another. Find out their identities. Also, while you're at it, figure out the SHA256 values of the first 3 Chinese words of their pledges, and interweave each character into a single string. There should be no whitespaces of any sort when performing the hashing. Append it to the flag together with the character names separated by underscores.

The flag is the name of the characters in alphabetical order lowercase separated by underscores. If the characters are `apple`, `orange`, and `mango`, and the hashes of their pledges are `aaaaaa`, `bbbbbb`, and `cccccc` respectively, the flag shall be `WH2020{apple_mango_orange_acbacbacbacbacbacb}`.

# Setup Guide

Serve output.png

# Solution

Flag: `WH2020{akashi_ayanami_laffey_02deccc4087ace83359dcc083546bd5e5e8113497c43911df8023432876b4267f2a5215a6b9d101eb86eabc25796306e2b90dee27e8384fa81605cc81b15d9d36586a14559e1de79410ed5f988b972c751ed8586af6f608079d624a707a90a75}`