# Elearn

WhiteHacks Elearn is a React web application demonstrating various vulnerabilities present in modern javascript web applications.

# Learning Objective

After completing the challenges, participants will have good exposure to security issues surrounding modern web applications, in particular Single Page Applications.

# Description (public)

## Elearn 1 - SQLi?

Recently, WhiteHacks Academy has put in a lot of effort to upgrade its elearn portal to embrace the latest web technologies. One of the end result is a whole new React web application. Everything from the login, to the search filtering are all done under-the-hood without needing a page refresh. This seamless experience has led to the overconfidence of its management to thinking that by upgrading their web stack, they're no longer vulnerable to old school web vulnerabilities such as SQL injection. Prove them wrong.

P.S. username is temp_acc, password is temp_pass

## Elearn 2 - JWT

Another feature of a modern single page application is the lack of session cookies, which WhiteHacks Academy claims it'll prevent session hijacking and session impersonation attacks. Instead, JSON Web Token (JWT) is powering its authentication mechanism. A powerful feature of JWT is its strong digital signatures that prevents any unauthorised tampering of its data. With this, an account will be all but possible, or is it?

P.S. username is temp_acc, password is temp_pass

## Elearn 3 - UNDISCLOSED

Let's talk about the course breakdown of WhiteHacks Elearn. Each course is regarded as a module, which consists of one or more lessons. Each lesson usually has accompanying documents and slides. The thing is, in order for there to be documents for download, there needs to be an interface to upload and edit them. Also, once the document is finalised, it is put out of draft mode and becomes published. When that happens, the document cannot be edited any further besides deleting it. The site administrator insists that he/she has hidden the file editing functionality, and cannot reinstate that under any circumstances. However, your professor has a serious typo he needs to fix, and asks for your help in discovering the way to update a document on the platform.

P.S. username is temp_acc, password is temp_pass

## Elearn 4 - XML

While the website was in the midst of upgrading, a global pandemic strikes, causing all of the IT personnel to work from home. As a result of this disruption, some shortcuts has to be taken in order to meet the deployment deadline. I hear that one of which is a decommissioned standalone Transcript Verification service that was hidden until a plan to migrate that service is discussed. Till this day, it can still be found on the upgraded elearn platform.

# Setup Guide

1. Run `npm install` to install the dependencies.
2. Run `npm run build` to build the web files available in the `./build` directory.
3. Use the `docker-compose.yml` to deploy the service.

# Solution

## Elearn 1

At the search interface after login, execute `' UNION SELECT id, flag FROM flag -- end`

Flag: `WH2020{0Ld_5ch00l_Sql1}`

## Elearn 2

Decode the JWT token and change the `alg` value to `none`. Afterwards, change the `identity` to 3 in order to takeover as `admin` account.

Flag: `WH2020{wh0_s@y5_5ing13_p@g3_@PP_i5nt_w3@k_t0_01d_vu1n5}`

## Elearn 3

Send a PUT request to `/modules/WRIT001/lessons/Lesson 01/documents/Document Flag`.

Flag: `WH2020{@cc35S_15_gr@nt3d_t0_th3_ch0sEn}`

## Elearn 4

Perform a error-based OOB XXE injection. Solution is in `/web/elearn/xxe/solution` folder.

Flag: `WH2020{IS_th15_3v3n_fr0nt3nd_@nym0r3?}`
