# PDF Converter

Node.js security things. Find and exploit a 0-day.

# Learning Objective

Students will learn how to search for vulnerabilities in existing code bases and exploit them.

## PDF-C: Use the Source Luke!

### Description (public)

```
I made my own OCR service for PDFs! There's more to this service than meets the eye though: can you find and query the hidden functionality in my code and retrive the first flag?

Thankfully, you managed to recover the source code of the application before it went private on GitHub. The source code of the application can be found in website.zip. (you do not have to look up GitHub to solve any challenges in this series)

PLEASE DO NOT UPLOAD ANY SENSITIVE DATA ON THE SERVER, IT WILL BE COMPROMISED!

Visit the challenge at http://chals.whitehacks.ctf.sg:13003/
```

### Flag

`WH2020{r3Ad_th3_s0urc3}`

## PDF-C: Lookie Its A Cookie

### Description (public)

```
I hope the circuit breaker period made you a better baker, because you are going to have to bake your own cookies. Can you retrieve the second flag?

Visit the challenge at http://chals.whitehacks.ctf.sg:13003/
```

### Flag

`WH2020{sw33_h3ng_bAk3ryy}`

## PDF-C: Baby0Day (Demo)

### Description (public)

```
Drats! Hackers managed to deface my website and I have no idea how they managed to do it. They say the devil is in the details, and you may have to look really deep to find the bug.

If you manage to exploit the vulnerability, run the /getinfo binary which will contain instructions on the next steps in reporting the vulnerability. If you are successful in the demo session, we'll give you the flag! 

Visit the challenge at http://chals.whitehacks.ctf.sg:13003/
```

### Flag

`WH2020{d0nT_y0u_w0rry_mY_chilD_pr0c3s5}`

# Setup Guide

1. Use the `docker-compose.yml` in the parent directory to deploy the service at port 13002
2. Test the service using netcat and `exploit.py`
3. Serve `dist/website.zip`


# Solution

Found in solution folder. For part 3, refer to Jiayang's writeup [here](https://github.com/IRS-Cybersec/ctfdump/blob/master/Whitehacks%202020/web/Baby0Day/README.md) for a full explanation.