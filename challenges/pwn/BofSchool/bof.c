#include <stdio.h>

/* gcc -fno-stack-protector ./bof.c -o bof */
char flag[] = "WH20{Real_flag_will_be_here}                                                   ";
void win(){
	puts(flag);
}

int main(){
	char buf[32];
	gets(buf);
	return 0;
}
