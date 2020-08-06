# README

## Description

Chris Wang, the newest hire for SecTech, receieved an anonymous email saying that his AWS credentials which he uses to perform backups of students results are leaked. However, Chris has no idea how the AWS credentials are being leaked! Being an paranoid employee, Chris sought advice from SecTech's cybersecurity team. However, the team merely brushes him off saying that everything in Cloud is secure! Chris felt worst. He knows that something is up. He remembers that the last thing he did was to write a simple set of instructions to tell the other staff, how to backup important files in the AWS EC2 instance! He left the instructions in the S3 bucket! He was very sure that he did not write the credentials inside the instructions! Can you help him figure out how the leakage happened?

## Solution

S3 bucket contains a "backup-notes.txt" which contains a message Chris left for the staff. In the message, Github is hinted and his Github handle is inside the message. Find the repository which contains the codes using his Github handle. Check for the past commits. The information to reach the target server is inside the past commit. SSH into the server with the provided credentials. Find the AWS credential file in `~/.aws/credentials`.

## Setup

``` bash
sudo docker build -t sshd_service .
sudo docker run -d -p 8822:22 --name sshd_service sshd_service

# ssh chrisw@sec-tech.cf -p 8822
# 7cj5dvv4uhBRLIpMNPeT
# Change the password in the docker file!
```

### Github Repository

Using the given credentials, head to `https://github.com/chriswang-sectech/sectech-backup-scripts`.