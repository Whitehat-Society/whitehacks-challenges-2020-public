#include<stdio.h>

char password[256];

int check(int in){
    while (in){
        if ((in & 0xF) == 15){
            return 0;
        }
        in >>= 4;
    }
    return 1;
}

int first(){
    printf("Please enter your password: ");
    scanf("%s", password);

    printf("Finished processing. The password: %s you entered is ", password);

    if (password[14] != '\0') return 1;

    for (int i = 0; i < 14; i++){
        if (password[i] < 'A') return 1;
        if (password[i] > 'F') return 1;
    }

    int test;
    
    test = 0;
    for (int j = 0; j < 14; j++){
        int to_add = password[j] - 'A';
        test = test << 0;
        test = test ^ to_add;
    }
    if (test != 4) return 1;

    test = 0;
    for (int j = 0; j < 14; j++){
        int to_add = password[j] - 'A';
        test = test << 1;
        test = test ^ to_add;
    }
    if (test != 52117) return 1;

    test = 0;
    for (int j = 0; j < 14; j++){
        int to_add = password[j] - 'A';
        test = test << 2;
        test = test ^ to_add;
    }
    if (test != 289197077) return 1;

    printf("correct! Submit this as your first flag: WH2020{%s}\n", password);
    return 0;
}

int second() {
    printf("Now generating part 2's flag. This may take a long while...\n");
    long long end = 0;
    for (int i = 0; i < 14; i++) end = (end << 4) + (password[i] - 'A');

    int out = 0;
    long long count = 1;

    while (count <= end){
        out += check(count);
        count += 2;
    }

    printf("Here: finished processing is your flag for part 2: WH2020{%d}", out);

    return 0;
}

int main(){
    if (first()){
        printf("wrong, please try again.\n");
        return 0;
    }
        
    second();
    return 0;
}