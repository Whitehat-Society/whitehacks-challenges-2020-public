#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <string.h>
#include <unistd.h>
#include <time.h>

#define BUFSIZE 128
#define FLAGSIZE 128
#define TEST_LEN 16

void handle_alarm(int sig)  {
    puts("");
    puts("Are you talking to me manually? I am a robot, and you humans are too slow!");
    puts("Bye bye human :)");
    exit(-1);
}

void readflag() {
    char buf[FLAGSIZE];
    FILE *f = fopen("/flag", "r");
    fgets(buf, FLAGSIZE, f);
    puts(buf);
    fflush(stdout);
}

int main() {
    char buf[BUFSIZE];
    char test[TEST_LEN + 1];

    setvbuf(stdin, NULL, _IONBF,0);
    setvbuf(stdout, NULL, _IONBF,0);

    signal(SIGALRM, handle_alarm);

    srand(time(NULL));

    for(int i = 0; i < TEST_LEN; i++) {
        test[i] = 'a' + rand() % 26;
    }
    test[TEST_LEN] = '\x00';

    puts("You figured out a way to talk to me!");
    sleep(1);
    printf("Just to be sure, can you say '%s' in 1 second?\n", test);
    alarm(2);
    printf("Repeat what I said without the quotes: ");
    scanf("%127s", buf);

    if (strcmp(buf, test) == 0) {
        puts("Yay! You understand me! Here's a gift for you: ");
        readflag();
    } else {
        puts("It seems you made a mistake. Maybe you should pay attention when you talk to me.");
    }  
   
    return 0;
}
