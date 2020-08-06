# gdbtutor

Interactive tutorial of gdb similar in concept to the equivalent in vim, [vimtutor](http://www2.geog.ucl.ac.uk/~plewis/teaching/unix/vimtutor).

# Learning Objective

Provides an introduction to common gdb commands and concepts like breakpoints, changing register values, printing disassembly and more.

# Description (public)

```
You’ve heard of [vimtutor](http://www2.geog.ucl.ac.uk/~plewis/teaching/unix/vimtutor), now let me introduce you to gdbtutor!

`nc whitehacks.ctf.sg 12002`
```

# Setup Guide

1. Use the docker-compose.yml in the parent directory to deploy the service at port 12001
2. Test the service by connection to `nc whitehacks.ctf.sg 12002`, follow all instructions and the flag should be given.

# Flag

`WH2020{The_beginnings_of_a_gdb_master}`

# Solution

Connect to the service and follow every command that is shown, flag should be given after following everything.
