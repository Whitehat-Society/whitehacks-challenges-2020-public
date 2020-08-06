# WhiteHacks 2020

Public repository for Whitehacks 2020 challenges.

# Running the Challenges

You will need Docker and Docker Compose to run the challenges locally. The following should get most challenges running, some other challenges require special setup (which can be found in the respective challenge folders).

```
cd challenges
docker-compose up -d --build
cd web/elearn
docker-compose up -d --build
```

# List of Challenges
- **Crypto**
    - BabyLFSR (Author: prokarius)
    - Concatacollision (Author: prokarius)
    - Who's My Waifu (Author: prokarius)
    - RSA (Author: lordidiot)
    - RSB (Author: lordidiot)
    - RSC (Author: lordidiot)
    - RSD (Author: prokarius)
- **Web**
    - Elearn 1 (Author: winstonho90)
    - Elearn 2 (Author: winstonho90)
    - Elearn 3 (Author: winstonho90)
    - Elearn 4 (Author: winstonho90)
    - Offfully 🍊 (Author: gladiator)
    - Going Postal (Author: waituck)
    - Many Days (Author: waituck)
    - PDF-C 1: Use the Source Luke! (Author: waituck)
    - PDF-C 2: Lookie Its A Cookie (Author: waituck)
    - PDF-C 3: Baby0Day (Author: waituck)
- **Pwn**
    - BofSchool (Author: lordidiot)
    - JIF (Author: lordidiot)
- **Reversing**
    - baby-parser 1 (Author: winstonho90)
    - baby-parser 2 (Author: winstonho90)
    - baby-parser 3 (Author: winstonho90)
    - ducky_say_what_i (Author: winstonho90)
    - ducky_say_what_ii (Author: winstonho90)
    - gdbtutor (Author: lordidiot)
    - x86_64_emu (Author: lordidiot)
    - No F No Respect I (Author: prokarius)
    - No F No Respect II (Author: prokarius)
    - RealGoodGo (Author: gladiator)
- **Misc**
    - talk_to_me (Author: waituck)
    - back_to_the_beginning (Author: winstonho90)
    - blue_alley (Author: winstonho90)
    - dias_mejores (Author: prokarius)
    - little_shrewd_braincells (Author: winstonho90)
    - match_maker (Author: winstonho90)  
    - raising_morale (Author: prokarius)
- **OSINT**
	- Literally Sharing (Author: Prof Ke)
	- Would you check out my any (Author: Prof Ke)
	- Come to SISters (Author: Prof Ke, haojun)
	- “Call” me Shameel1n! A, B, C (Author: haojun)
	- Expose the raoter A, B, C, D (Author: haojun)
	- Trace me like you know me A, B, C, D (Author: Shao, haojun)
	- Sponsors Challenges (GovTech, CSA, CSIT) (Author: Shao, James, haojun)
- **GovTech**
    - WhatTheHXXXIsThis (Author: ragulbalaji)
    - CanYouDecode (Author: hojiefeng)
    - SecTech 1 (Author: kennethleebz)
    - SecTech 2 (Author: kennethleebz)
    - SecTech 3 (Author: kennethleebz)
    - SecTech 4 (Author: kennethleebz)
    - SecTech 5 (Author: tankeehock)
    - SecTech 6 (Author: kennethleebz)
- **CSIT**
    - TheNextLevel 1
    - TheNextLevel 2
    - TheNextLevel 3
- **CYS**
    - 49 53 20 54 48 49 53 20 48 45 58 3f
    - Future Diary
    - Little Matryoshka Doll
- **Stego**
    - Bad Art Gallery A, B (Author: haojun)
    - Find me if you can (Author: haojun)
	- You see me when I see you (Author: haojun)
- **Bonus (Flags shown during talks)**
    - Day 1 Talk 1 (Govtech) (Author: James)
    - Day 1 Talk 2 (CSIT) (Author: James)
	- Day 1 Talk 3 (CSA) (Author: James)
    - Day 1 Workshop 1 (Bryan) (Author: James)
    - Day 1 Workshop 2 (Calvin) (Author: James)
    - Day 2 Talk 1 (Govtech) (Author: James)

# Flag format

All flags should have the format `WH2020{Unguessable_string}`.

