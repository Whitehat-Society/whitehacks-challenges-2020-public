# Talk To Me

Talk to me is a simple challenge to get students to connect to a networked service using pwntools or other programming language socket constructs.

# Learning Objective

After completing this, participants will have a good sense of how to parse inputs from a network service.

## Expected Difficulty 

3/10 - some programming and API lookup required

# Description (public)

```
I hope you'll talk to me... it's getting kind of lonely here. You'll need to speak my language though.

nc chals.whitehacks.ctf.sg:11001
```

# Setup Guide

1. Run `make` to compile the binary
2. Use the `docker-compose.yml` in the parent directory to deploy the service at port 11001
3. Test the service using netcat and `exploit.py`

# Flag

`WH2020{hUm4n$_@r3_t0O_sl0W}`

# Solution

Annotated solution can be found in [exploit.py](exploit.py)
