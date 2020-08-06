# TheNextLevel 

CSIT Reverse-Engineering (RE) challenge.
TheNextLevel is a 3 level challenge designed to cater towards participants of different reverse engineering profiency. 
It involves RE-ing the executable, thenextlevel.exe, and obtaining the flags from 3 different levels, each with increasing difficulty.

# Learning Objective
## Level 1
- RE concepts on switch cases and numeric operations
- RE concepts on tracing executable’s mainCRTstartup to key functions for solving the challenge

## Level 2
- RE concepts on C++ object memory allocations
- RE concepts on Data Structure allocations and manipulations for Arrays and Linked List
- Involves allocating user inputs into an array, parsing an array containing jumbled Nodes, initialising and allocating a Linked List, traversing and comparing the answer Linked List.

## Final Level
- RE concepts on Windows API usages, and Cryptographic Hashing and Decryption of encrypted data block through APIs

# Description (public)

When one level is not enough, one strives onwards to attain the final level. Embrace your passion and lunge into the depths of cyber. Go forth, challenge TheNextLevel, and retrieve the hidden flags. 

\*Download thenextlevel.exe into a virtual machine (Windows recommended) and use a disassembler to reverse engineer the exe.  

# Setup Guide

Download thenextlevel.exe and reverse engineer the executable to find the flag.

# Flag
## Level 1
`WH2020{p@$$i0n@TeAb0UtT3cHn010gIe5?}`
## Level 2
`WH2020{J0inC5It!}`
## Level 3
`WH2020{C5iTCh@LLeNgE2020}`

# Solution
- Use a disassembler of your choice to decompile this C++ binary.

## Level 1
1. Find mainCRTStartup and trace to the main function of the binary
2. Understand the input and output involved, and find the setup for the first level
3. Stage 1 involves keying a correct input, followed by tracing through a switch case which the value will solve the equation numerically
4. With the correct answer, a hint to the final level would be revealed, along with the secret code approach CSIT virtual booth for the level 1 flag

User Input Answer: T
Secret Code Hint: L34rN @nd Gr0w T0g3th3R

## Level 2
1. More inputs are required from the observation in the level 2 setup function (A total of 10 inputs)
2. From the function that parses the input, it can be observed that these 10 inputs must be greater than 0 and lesser than 10, and they are all unique digits
3. 10 c++ objects (Nodes for Linked List) were created with a fixed value in them and arranged into an array of the specific order.
4. Using the 10 digits, the node corresponding to the array index would be retrieved and linked to the next digit's node, forming a linked list with the input
5. An answer linked list can be found with the right sequence of nodes
6. The input set and the answer set would be compared by traversing the two linked lists
7. With the correct answer sequence, a hint to the final level would be revealed, along with the flag for level 2

User Input Answer: 6 4 1 2 0 7 5 9 3 8

## Final level
1. By RE-ing the setup and the functions involved in the final level, Windows APIs usages for WinCrypt cryptographic functions can be observed.
2. The passphrase will come from the user input and hashed by SHA-256 algorithm.
3. The 32-bytes long digest would be used as the key to the AES-256 decryption of the encrypted data
4. There will be a riddle hint printed to the participant for this level and the solution to the riddle is the passphrase
5. Both level 1 and level 2 answers would be used along with the passphrase together as the key to complete the final level
6. The final flag for this challenge would be obtained after completion

User Input Answer: S3ri0UsP@s5i0N
