# Trace me like you know me

Author: Shao, haojun

This is a 3 part challenge that guide participants through Whitehat website by tracing along with the clues given.

# Description

## Trace me like you know me - A

Could you identify what’s the Registry Domain ID of Whitehats website being hosted on?

http://smuwhitehats.netlify.app 

Submit the IP address with the flag format.
For example, WH2020{1234ABCD-XXYY}

## Trace me like you know me - B

Send me an email and you will be surprised!

Submit the flag as per given.

## Trace me like you know me - C

Due to technical difficulties, this part of the challenge was omitted.

## Trace me like you know me - D

HackerJames, a fellow SMU student who has mad interest in CyberSecurity have always dreamt of joining the Whitehats executive committee, but due to some of his negative personality traits and habit of spilling secrets just to show he knows more than others, Whitehats did not accept him into the Exco team. As such, he holds a slight grudge to the Whitehats team. Someone overheard him telling his friends how he managed to sneak into the Whitehats system and added in his own little surprise in the Whitehats websites @ smuwhitehats.netlify.app, and that he could have done more damage but decided to just control himself to remain as the good guy. Find out what exactly he did and get to the bottom of it.

Submit the flag as per given.

## Trace me like you know me - E

Thank you for tracing all the way like you really know me. As a token of appreciation for your effort and we like to reward you with another flag. Head onto the telebot and select voucher code t.me/WhiteHacks2020_OSINT_BOT and enter this code 84e2e595aafb7179d5e123d9d96fb3d95c457a7954693c70a8a6756f26b912de to claim. 

Submit the flag as per given.


# Solution

## Trace me like you know me - A

Lookup whois on the website domain name and you should be able to find the Registry Domain ID.

Flag: `WH2020{2CB5C0CD0-APP}`

## Trace me like you know me - B

Identify the email in the SMU Whitehats website, send us an email, an auto reply email will be received.

Then, you should explore further in this email, one way is just select the entire email and the flag will be reveal in pieces. Just join them back and you get your flag.

Flag: `WH2020{R>U<5uR9r1$3}`


## Trace me like you know me - D
HackerJamesBest twitter account will be located in Whitehats website (within the source code @ the exco section).
From here you can apply 2 different method, the easiest is use wayback machine on HackerJamesBest twitter page and you will find out URL untouched.

Or decode hspe./bhtp:/atbncmnNPft/siodU with rail fence cipher (if it's familiar to you). Then visit the decoded URL to obtain your flag.

Flag: `WH2020{31ll.U.0uT}`

## Trace me like you know me - E

After input the given token, the flag will be revealed to you.

Flag: `WH2020{M3_@ppr3c!4TE_U2_$.$}`