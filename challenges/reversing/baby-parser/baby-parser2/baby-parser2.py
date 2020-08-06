#!/usr/bin/env python3

import os
import zlib
import struct
from io import BytesIO

magic = b'WHITEHACKSV2\x00\x00\x00\x00'

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

os.makedirs('build', exist_ok=True)
with open('./build/baby-parser2.wh', 'wb') as f:
    f.write(w.getvalue())