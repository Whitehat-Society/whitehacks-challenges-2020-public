# JIF

Demo client-side pwn challenge meant to be a challenging pwn.

# Learning Objective

Provides a more difficult buffer overflow example that may mimic some real world file format buffer overflows that do not provide interactivity that a usual CTF pwn would have.

# Description (public)

```
I love GIFs, but the format is very space inefficient and the name's pronunciation is ambigious. To fix that I have created **JIF**, my very own animated image file format that is very simple to create!

Challenge Instructions:
Prepare your malicious JIF file and ping the author @Lord_Idiot#1845 on discord to get your turn to demo your exploit! Your malicious JIF file will be run with the command

`./jifviewer ./<your file>.jif`

Your exploit should run the `/win` command on the victim PC to solve this challenge.

JIF Creation Instructions:
Simply create your JIF animated frames as 24-bit BMP images and name them as 0.bmp, 1.bmp, n.bmp ... in order of appearance. Zip these bmp files together and rename the file to <name>.jif and you're done! Teams are encouraged to be as creative as possible with your exploit, advertise your team banner, show-off your favourite song, as long as it does not contain any offensive material, do as you wish!

Hint:
The challenge is not looking for a zip-related attack.
```

# Setup Guide

1. Demo challenge. Not sure.
2. `sample.jif`, `jifviewer`, `Makefile`, `main.c` should be distributed

# Flag

`WH2020{GIF_should_be_pronounced_JIF}`

# Solution

Run `exploit.py` to generate the exploit `exploit.jif`. The bug is a trivial buffer overflow based on the fact that `info_header.biWidth` is only checked for the first frame, and the second frame onwards can have very large `biWidth`, causing a buffer overflow. The main challenge of the exploit is avoiding crashing before `ret` is executed. Afterwards a simple ROP chain can be used to call `system("/win")`
