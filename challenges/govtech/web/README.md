# WhiteHacks SecTech - Web Challenges

WhiteHacks SecTech is a PHP web application demonstrating various vulnerabilities listed amongst OWASP Top 10.

# Learning Objective

We hope the challenges will pique the interest of students in cybersecurity, and to let them experience popular and common web vulnerabilities in the modern world.

# Description (public)
To login to the website, please use the following credentials, `temp_acc:temp_pass`.

## SecTech 1 - LFI

WhiteHacks SecTech is an application for SecTech school staff to login to the system and to view students grades and to generate transcripts. However, could you perhaps view more than transcripts?

## SecTech 2 - XSS

Cross site scripting can come in many forms. In the worst case scenario, it may even allow admin credentials to be stolen. We understand the generation of transcript to be a privileged process in WhiteHacks SecTech. Is it truly secure? Try to print out some cookies!

## SecTech 3 - IDOR

Insecure Direct Object Reference can have severe repercussions for applications. One mitigation technique is to avoid trusting user input. If you are tired, have some cookies with milk?

## SecTech 4 - Insecure Deserialization

Trusting serialized data without verifying them can be precarious. To this end, we ask that you be like the Cookie Monster, attentive and inquisitive.

## SecTech 5 - OSINT

We love how the system archives past student records - after all, data is gold. If you don't find the gold, we suggest you dig deeper and look beyond the surface, specifically the 'root' :)

## SecTech 6 - SSRF

Server Side Request Forgery allows one to make HTTP requests on behalf of the server. Some animals are more equal than the others, just like we think SecTech is more equal to AWS than a normal plebian would be.

# Solution

## SecTech 1 - LFI

When viewing transcript, specify the path of the file to /etc/passwd. It should show you on the last line of the file a reference to /secret_path/lfi_flag.txt. Specify path to /secret_path/lfi.txt.

Flag: `WH2020{Loc@l_F1l3_Inclus10n_buT_N0t_sh3ll}`

## SecTech 2 - XSS

When generating transcript, specify script to `data:;base64,ZG9jdW1lbnQud3JpdGUoZG9jdW1lbnQuY29va2llKQ==`

Flag: `WH2020{XSS_C4N_C4USE_A_W0RLD_OF_P41N}`

## SecTech 3 - IDOR

Navigate to Profile page. Set cookie for user_id to md5 value (2) `c81e728d9d4c2f636f067f89cc14862c`.

Flag: `WH2020{ID0R_D0_N0T_TRUST_US3R_INPUT}`

## SecTech 4 - Insecure Deserialization

Navigate to Admin page. Base64 decode cookie, change admin to true and encode it back. 
Specifically, you may change the value to `YToyOntzOjQ6InVzZXIiO3M6ODoidGVtcF9hY2MiO3M6NToiYWRtaW4iO2I6MTt9`

Flag: `WH2020{Cook!3Ins3cur3Des3r!al!zat!on_Adm!nR!ghts}`

## SecTech 5 - OSINT

Navigate to Past Student Records. You would see various download links.
Navigate to https://sectech-archived-student-records.s3-ap-southeast-1.amazonaws.com/ and you can see backup-notes.txt there.
Read the notes and it should redirect you to @chriswang-sectech. Look up the github commits and you should receive a set of SSH credentials.
Login to the server and key can be found in ~/.aws/credentials.

Flag: `WH2020{CR3dent1als_FiL3_IS_ImPT0rt4nt}`

## SecTech 6 - SSRF

Navigate to rankings page, change ranking-url value to `http://169.254.169.254/latest/user-data`

Flag: `WH2020{EC2UserData-SSRF}`

## Setup

The instance should be deployed in an AWS environment due to the AWS meta-data service.

1. When creating EC2 instance, add `#WH2020{EC2UserData-SSRF}` to the user-data

2. Install docker and docker-composer

3. Launch the docker `magic`
    ```bash
    # Setup
    sudo docker-compose up --build --force-recreate --no-deps

    # Tear Down
    sudo docker-compose down --volumes
    ```

4. Head to http://ip:5000/ and import the sql script found in `web-service/mysql`

5. Bring down the phpmyadmin service

6. Create a public S3 bucket and store all the items inside `aws-setup/s3-files folder` (ignore the contents inside `generate`)

7. Link the S3 bucket

### Others

An AMI with the docker setup is avaliable. Please contact the GovTech team.
