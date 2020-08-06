#include <stdio.h>
#include <stdlib.h>

void main() {
    char ch;
    FILE *fp = fopen("/flag.txt", "r");
    if (fp) {
        while((ch = fgetc(fp)) != EOF) {
            printf("%c", ch);
        }
        fclose(fp);
    } else {
        puts("Challenge is broken, contact @waituck on discord");
    }
}