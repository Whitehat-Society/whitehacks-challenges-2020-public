# Match Maker

Match Maker is a simple network service that students can connect to and perform adjacent memory reads beyond the limit.

# Learning Objective

After completing this, students will learn to think beyond the give size limit provided by the service. Also, some scripting skills can be attained from iteratively and incrementally guessing the flag output.

# Description (public)

I challenge you to guess the flag without relying on any output.

# Setup Guide

1. Use the `docker-compose.yml` in the parent directory to deploy the service at port 11001
2. Test the service using netcat and `exploit.py`

# Flag

`WH2020{a_M@tch_mad3_iN_h3AvEn}`

# Solution

Annotated solution can be found in [exploit.py](exploit.py)
