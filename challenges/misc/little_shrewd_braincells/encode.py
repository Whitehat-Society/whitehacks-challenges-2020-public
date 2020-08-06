#!/usr/bin/env python3

from io import BytesIO
import wave

params = ()
data = None
with wave.open('bensound-creativeminds.orig.wav') as f:
    params = f.getparams()
    n = f.getnframes()
    data = BytesIO(f.readframes(n))

print('Loading params', params)

flag = 'WH2020{l1ttl3_b1t_@l50_c@n_f1nd_m3}'
flag = ''.join([bin(ord(ch)).lstrip('0b').rjust(8, '0') for ch in flag])

buf = data.getbuffer()
for i, bit in enumerate(flag):
    buf[i] = (buf[i] & 0b11111110) | int(bit)

with wave.open('bensound-creativeminds.wav', 'wb') as f:
    f.setparams(params)
    f.writeframes(data.getvalue())
