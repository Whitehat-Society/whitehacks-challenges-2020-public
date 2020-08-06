#!/usr/bin/env python3

import os
import struct
from io import BytesIO

magic = b'WHITEHACKSV1\x00\x00\x00\x00'

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
        w.write(struct.pack(f'<{len(file) + 1}sI{len(b)}s', file.encode('utf8') + b'\x00', len(b), b))

os.makedirs('build', exist_ok=True)
with open('./build/baby-parser1.wh', 'wb') as f:
    f.write(w.getvalue())