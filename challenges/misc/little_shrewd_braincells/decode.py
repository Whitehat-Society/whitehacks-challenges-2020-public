#!/usr/bin/env python3

from io import BytesIO
import wave
import string
from zipfile import ZipFile

song = None
with ZipFile('bensound-creativeminds.zip') as f:
    song = BytesIO(f.read('bensound-creativeminds.wav'))

params = ()
data = None
with wave.open(song) as f:
    params = f.getparams()
    n = f.getnframes()
    data = BytesIO(f.readframes(n))

print('Loading params', params)

buf = data.getbuffer()
buf[:] = bytes([b & 0b1 for b in buf])

bits = [''.join(map(str, buf[i:i+8])) for i in range(0, len(buf), 8)]
flag = ''
try:
    for b in bits:
        ch = chr(int(b, 2))
        if ch not in string.printable:
            break
        flag += ch
except:
    pass

print('Flag:', flag)
