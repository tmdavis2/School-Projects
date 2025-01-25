#include <stdio.h>
#include <stdbool.h>

void main()
{    
    int counter = 10;
    while(counter >= 1){
        if(counter % 2 == 0){
            printf("%d\n", counter);
        }
        counter--;
    }

}