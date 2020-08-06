# Back to the Beginning

Back to the Beginning is a simple audio file challenge that contains the spoken flag.

# Learning Objective

After completing this, students will be able to identify common audio techniques to obfuscate important information and confuse adversaries.

# Description (public)

A secret agent managed to record the confidential conversation between the game masters and the challenge creators. When you try to listen to it however, it does not sound like any language you know. Nonetheless, we do not have much time. Quick, uncover the flag and submit it before it's too late!

P.S. Combine the keywords together with an underscore to form the flag. If you hear `apple orange coconut`, the flag will be `WH2020{apple_orange_coconut}`.

# Setup Guide

Simply serve the .mp3 file

# Solution

Using `ffmpeg -i back_to_the_beginning.mp3 -af areverse back_to_the_beginning.fixed.mp3` and listen to it.
Alternatively, you can use Audacity to reverse the soundtrack and retrieve the flag.

Flag: `WH2020{the_end_is_the_beginning}`
