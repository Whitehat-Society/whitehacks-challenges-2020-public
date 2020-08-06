# Expose the raoter

Author: haojun

This is a 4 part challenge that allow participant to find out the common router username and password. Also, by interacting with a pseudo router in the telebot give them a feel of reading through device logs and find insights from those log entries.

# Description

## Expose the raoter - A

Do you know what’s the common default IP address when we first setup any raoter? (Just submit 2 IP addresses)

Please submit your answer in this ascending format:

For example, WH2020{1.1.0.1, 1.1.1.1}

## Expose the raoter - B

I recently found a raoter left unattended at my void deck. The model is ASUS RT-AC88U. Perhaps do you know the username and password to such a router?

Please submit your answer in this format.

For example, WH2020{username, password}

## Expose the raoter - C

This is where you can access my router t.me/WhiteHacks2020_OSINT_BOT, since you have figured out the username and password. Are you able to find out the owner of the raoter?

Please submit your answer in this format:

For example, WH2020{Jues Faul}

## Expose the raoter - D

Are you able to find anything else in the raoter?

Submit the flag as per given.


# Solution

## Expose the raoter - A

Use google search and you are able to find the common default IP address for router.

Flag: `WH2020{192.168.0.1, 192.168.1.1}`

## Expose the raoter - B

Using such router database https://www.routerpasswords.com/asus-router-password/ will help you to find out the common credentials to the device.

Flag: `WH2020{admin, admin}`

## Expose the raoter - C

After "login", the telebot will send a list of information one after another from 15 to 20 lines. Depending on the RNG, the owner's names will appear in this header “ownthisraoter[8888]:”. Extract the name correctly and you found your flag.

Flag: `WH2020{Ted Jennings}`

## Expose the raoter - D
Also, in that list of information after revealing the owner name, depends on the RNG it reveal a flag in this header “flag[XXXXX]:”.

The reason of using RNG here is to simulate an interesting event one after another that the router picks up from the network traffic.

Flag: `WH2020{R@07ER+3XP0$E-$3R1E5}`
