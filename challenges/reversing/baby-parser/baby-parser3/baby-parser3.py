#!/usr/bin/env python3

import os
import zlib
import random
import string
import struct
from io import BytesIO

magic = b'WHITEHACKSV3\x00\x00\x00\x00'

dirpath = os.path.dirname(os.path.realpath(__file__))
files = ['index.html', 'flag.png']
files += [f"../common/{f}" for f in os.listdir(os.path.join(dirpath, '../common'))]

w = BytesIO()
w.write(magic)

# write the TLV
for file in files:
    filepath = f"{dirpath}{os.sep}{file}"
    with open(filepath, 'rb') as f:
        file = os.path.basename(file)
        b = f.read()
        z = zlib.compress(b)
        w.write(struct.pack(f'<{len(file) + 1}sII{len(z)}s', file.encode('utf8') + b'\x00', len(z), len(b), z))

charset = (string.ascii_letters + string.digits).encode()

data_buf = w.getbuffer()[len(magic):]
# otp = [random.choice(charset) for i in range(len(data_buf))]
otp = []
with open('./baby-parser3/otp.key', 'rb') as f:
    otp = list(f.read())
buf = [b ^ otp[i] for i, b in enumerate(data_buf)]
w.getbuffer()[len(magic):] = bytes(buf)

# with open('./build/otp.key', 'wb') as f:
#     f.write(bytes(otp))

os.makedirs('build', exist_ok=True)
with open('./build/baby-parser3.wh', 'wb') as f:
    f.write(w.getvalue())