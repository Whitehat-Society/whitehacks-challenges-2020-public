#include <stdio.h>
#include <fcntl.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>

/* gcc ./crackme.c -o crackme.bin -g */

char secret_key[] = "<REDACTED FROM SOURCE>";
void initialisation(){
	setvbuf(stdout, 0, 2, 0);
}

int main(){
	initialisation();

	/* stage one */
	puts("[Stage 1]");
	if(getuid() != 0){
		puts("You are not root, fail stage 1!");
		return -1;
	}
	else{
		puts("Stage 1 pass. Welcome root!");
	}

	/* stage two */
	puts("[Stage 2]");
	char buf[100];
	memset(buf, '\x00', 100);
	printf("Give me the secret key: ");
	fgets(buf, 99, stdin);
	buf[strlen(buf)-1] = '\x00'; // remove trailing newline
	if(strcmp(buf, secret_key) != 0){
		puts(buf);
		puts("You do not know the secret_key, fail stage 2!");
		return -1;
	}

	/* win */
	int fd = open("flag.txt", O_RDONLY);
	char flag[100];
	memset(flag, '\x00', 100);
	read(fd, flag, 100);
	printf("Congratulations, here is the flag: %s", flag);
	
	return 0;
}
