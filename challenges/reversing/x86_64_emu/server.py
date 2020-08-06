#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from pwn import *
from unicorn import *
from unicorn.x86_const import *
from sys import stdin, stdout
from termcolor import colored, cprint

# global config
NUM_QUES = 5

def print_banner():
	cprint("""         XXXXX\n        XX  XX\n       XX +  X\n      XXX    X\n        XX   X\n          X  X         XXXXXXX\n          X  X    XXX X      XXX\n          X  X XXX             XX\n          X  X X                XX\n         XX                      X\n         XX                      XX\n          XX              X       X\n           XXX       X    X       X\n              XXXXXX XX  XX  XXXXXX\n                   X  XXXX   X\n                  X          XX\n                 XX           X\n                 X          XXX\n                XX          X\n                X\n             XXXX\n\n██   ██  █████   ██████           ██████  ██   ██ \n ██ ██  ██   ██ ██               ██       ██   ██ \n  ███    █████  ███████          ███████  ███████ \n ██ ██  ██   ██ ██    ██         ██    ██      ██ \n██   ██  █████   ██████  ███████  ██████       ██ \n                                                  \n        ███████ ███    ███ ██    ██ \n        ██      ████  ████ ██    ██ \n        █████   ██ ████ ██ ██    ██ \n        ██      ██  ██  ██ ██    ██ \n        ███████ ██      ██  ██████  \n""", "yellow")
	print "Can you emulate x86_64 code with your brain?\n"
	sleep(2)

def print_flag():
	cprint("Congratulations! Here is your flag: WH2020{x86_64_is_easier_to_read_than_chinese_imo}", "green")

def easy_snippet():
	reg = random.choice(["rax", "rbx", "rcx"])
	return "mov {}, {}\n".format(reg, random.randrange(0, 0x10000000000000000))

def med_snippet():
	op1 = random.choice(["rax", "rbx", "rcx"])
	op2 = random.choice(["rax", "rbx", "rcx", "imm8", "imm16"])
	instr = random.choice(["add", "sub"])
	if op2 in ["rax", "rbx", "rcx"]:
		return "{} {}, {}\n".format(instr, op1, op2)
	else:
		immop = random.randrange(0, 2**int(op2[3:]))
		return "{} {}, {}\n".format(instr, op1, immop)

def gen_answer(snippet):
	mu = Uc (UC_ARCH_X86, UC_MODE_64)
	BASE = 0x400000
	mu.mem_map(BASE, 1024*1024)
	mu.mem_write(BASE, snippet)
	mu.reg_write(UC_X86_REG_RAX, 0)
	mu.reg_write(UC_X86_REG_RBX, 0)
	mu.reg_write(UC_X86_REG_RCX, 0)
	mu.emu_start(0x0000000000400000, 0x0000000000400000+len(snippet))
	rax = mu.reg_read(UC_X86_REG_RAX)
	rbx = mu.reg_read(UC_X86_REG_RBX)
	rcx = mu.reg_read(UC_X86_REG_RCX)
	return (rax, rbx, rcx)

def gen_snippet(qnum):
	"""
	Return x86_64 assembled code snippet and the 
	corresponding values of the rax, rbx and rcx registers
	"""
	difficulty = qnum / 3
	snippet = ""
	if difficulty >= 0:
		for i in xrange(3):
			snippet += easy_snippet()
	if difficulty >= 1:
		for i in xrange(2):
			snippet += med_snippet()
	snippet = asm(snippet)
	answer = gen_answer(snippet)
	return (snippet, answer)

def get_answer(qnum, snippet, answer):
	answer = list(answer)
	difficulty = qnum / 3
	dis = disasm(snippet)
	print "\033[H\033[J"
	cprint("Question {}/{}".format(qnum+1, NUM_QUES), "yellow")
	cprint("[Register start state]", "red")
	print """+-----+--------------------+
| rax | 0x0000000000000000 |
+-----+--------------------+
| rbx | 0x0000000000000000 |
+-----+--------------------+
| rcx | 0x0000000000000000 |
+-----+--------------------+
"""
	cprint("[x86_64 snippet]", "red")
	print dis+'\n'
	
	reg = random.choice(["rax", "rbx", "rcx"])
	cprint("[Register end state]", "red")
	print "+-----+--------------------+"
	for r in ["rax", "rbx", "rcx"]:
		print "| {} | 0x{:016x} |".format(r, answer[["rax","rbx","rcx"].index(r)]) if r != reg else "| {} | {} |".format(r, '?'*18)
	print "+-----+--------------------+"

	stdout.write("Whats the value of {}: ".format(reg))
	x = stdin.readline().strip()
	answer[["rax","rbx","rcx"].index(reg)] = int(x,16) if x.startswith("0x") else int(x)
	
	return answer
	

if __name__ == "__main__":
	context.arch = "amd64"

	print_banner()
	for qnum in xrange(NUM_QUES):
		snippet, answer = gen_snippet(qnum)
		rax, rbx, rcx = get_answer(qnum, snippet, answer)
		if (rax, rbx, rcx) == answer:
			print "Great job! You current score is {}/{}".format(qnum+1, NUM_QUES)
			sleep(0.5)
		else:
			print "Wrong! Try again. This may come handy: http://opensecuritytraining.info/IntroX86-64.html"
			exit()

	print_flag()
