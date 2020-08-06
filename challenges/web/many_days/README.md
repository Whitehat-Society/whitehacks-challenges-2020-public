# Many Days

Exploiting a known n-day in an insecure website component.

# Learning Objective

Students will learn how to research and craft their own JS ACE exploits.

# Description (public)

```
Tim started a new web service to help convert YAML to JSON. However, he was informed by his security team that he was using insecure components, and they linked him to the following advisory.

https://www.npmjs.com/advisories/813

However, Tim doesn't believe his security team (bad Tim!). Can you craft a working exploit and show us that you managed to pwn the system by running the `/readflag` binary on the system?

P.S. This is an example of an N-day vulnerability, where the security issue/vulnerability is already known for some or many days (hence the term N-day) but there may or may not be working exploits for this. If you managed to successfully exploit this, then you would have exploited your first N-day!

Visit the challenge at http://whitehacks.ctf.sg:13002/
```

# Setup Guide

1. Use the `docker-compose.yml` in the parent directory to deploy the service at port 13002
2. Test the service using netcat and `exploit.py`
3. Serve `dist/website.zip`

# Flag

`WH2020{first_0f_mAnY_N_dAyz}`

# Solution

Annotated exploit script is available in `exploit.py`.