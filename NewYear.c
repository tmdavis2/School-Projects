#include <stdio.h>
#include <stdbool.h>
#include <unistd.h>

void main()
{    
    int counter = 10;

    while(counter >= 1){
        printf("%d\n", counter);
        counter--;
        sleep(1);
    }

    printf("Happy New Year!\n");
}