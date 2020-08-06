# Concatacollision

Challenging number theory hash collision.

# Learning Objective

It's a difficult number theory to challenge better teams. This shows badlybreak implemented hash algorithm would introduce vulnerabilities.

# Description (public)

```
To print the flag, looks like we need a 2FA token to verify. Although we have no token, our engineers have managed to secure the code of the checking server. I'm sure the check function isn't as secure as they think...

nc whitehacks.ctf.sg 10001
```

# Setup Guide

1. Use the `docker-compose.yml` in the parent directory to deploy the service at port 10001
2. Test the service using netcat and `exploit.py`

# Flag

`WH2020{Numb3r_The0ry_I5_H4rd}`

# Solution

Token's code can be found in [token.py](token.py).
