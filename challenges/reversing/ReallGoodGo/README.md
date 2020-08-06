[//]: # (Here's a template you can use for a readme file)

# Real Good Go

# Learning Objective: 

Identifying hardcorded strings in a Go binary. 

# Description (public): 
```
I heard C programs are too easy to reverse, so I wrote this program in Go. Can you find the flag?
```

# Setup Guide: 
Serve `main`.

# Flag: WH2020{G0_R3v3s1ing_1s_FuN_Isnt_it}

# Solution:
1. Open challenge file in IDA
2. Find parts where strings are being called and stored. (Can also look at some runtime functions for tell tale signs)
3. Eyeball for flag which is coded in the binary (in parts).