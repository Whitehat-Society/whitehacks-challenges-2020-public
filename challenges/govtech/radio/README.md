# WhiteHacks Radio Challenges

Radio & Related

# Learning Objective

Give students a challenge into the fringes of technology and upcoming areas of cyber security. Radio is one of these exciting frontiers.

# Description (public)

## WhatTheHXXXIsThis - SIGINT

You, a hobbyist, are introduced to the wonderful world of radio by way of an software defined radio (SDR). You hop on the electromagnetic waves and notice a weird signal, you save the audio recording of the signal for further decoding.

Hmm maybe this will coming in handy https://www.sigidwiki.com/wiki/Database

Paid Hint: Here's a good tool https://en.wikipedia.org/wiki/Fldigi

## CanYouDecode - SIGINT

Concurrently, you notice that a new signal has popped up, but to your dismay, it is transmitting in an unknown mode.

Paid Hint: Here's a good tool https://github.com/jopohl/urh

# Solution

## WhatTheHXXXIsThis - SIGINT

raw.txt message is transmitted using https://en.wikipedia.org/wiki/Hellschreiber (HELL), player needs to identify this correctly by looking at the waterfall diagram to identify the patterns.

Flag: `WH2020{URFR33THEINST4NTYOUWANTTOREEE}`

## CanYouDecode - SIGINT

Open in urh, select FSK mode and set noise to 0, autodetect parameters and select ASCII.

Flag: `WH2020{I_C4N_D3C0D3_TH15_f233121sdqg7k9plosp}`
