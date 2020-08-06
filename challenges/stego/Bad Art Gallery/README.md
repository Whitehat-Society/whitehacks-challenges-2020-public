# Bad Art Gallery

Author: haojun

There are different techniques to represent text such as binary to text. Also, metadata could be one of the area to hide information from plain sight as well.

# Description

## Bad Art Gallery - A

Recently I went to an art gallery and saw this piece which doesn’t make sense. Could you identify what this piece of art is trying to portray?
https://ibb.co/CzNFkhr

Submit the flag as what you have found.

## Bad Art Gallery - B

Since you have solved the first art piece, by now you should have discovered a link.
Could you identify what’s in this piece as well?

Submit the flag as what you have found.

# Solution

## Bad Art Gallery - A

Download the picture from the website link given.

Investigate in the IPTC metadata and under special instructions, you will see the binary version of the text.

Decode it and you found your flag.

Flag: `WH2020{N3KK0Y4(P1ck M3)}`

## Bad Art Gallery - B

In the same picture, under IPTC keywords or under properties > tags, there is a link to https://pastebin.com/yiDFhsPt

If you recognise the output, it's using ROT13 with ROT47 variant to encode the message.

Therefore, to decode use the same method and you found your flag.

Flag: `WH2020{1t'3 M3(P1ck M3)}`
