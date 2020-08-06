# Challenge Title

Future Diary

# Learning Objective

Learn about the dangers of IOT and botnets along with a bit of Osint and github 

# Description (public)

Gasai Yuno has attacked several organisations including GitHub, Twitter, Reddit, Netflix, AirBnb and also took down the DNS services of Dyn using her powerful IOT malware. 

She has given up the life of crime for Yukiteru and has posted the source code for the malware online on a famous hacking forum.

It seems like the forum requires a account to login,but maybe someone uploaded the details and the code has been committed onto a version control platform? 

A little octocat told us that the forum post was uploaded on 30th September 2016, hopefully that will help. She left us a encoded secret message in the comment on line 26 of table.h, let us know what is it?

The flag is the comment. Remember to wrap the flag in WH2020{} i.e. WH2020{.manga}


# Setup Guide

Just display the description

# Flag

WH2020{.anime}

please make it case insensitive

# Solution

Google search DNS services of DNS service provider Dyn and find the out that the description is referring to mirai botnet, find out that there is a github and that it contains source code at https://github.com/jgamblin/Mirai-Source-Code/blob/master/ForumPost.txt 

go to https://github.com/jgamblin/Mirai-Source-Code/blob/3273043e1ef9c0bb41bd9fcdc5317f7b797a2a94/mirai/bot/table.h and look at line 26










