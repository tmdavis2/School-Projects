#include <stdio.h>

//prints put multiplication table
void main() {
    
    for(int i = 10; i <= 100; i+=10){
        printf("%d\n", i);
    }

    for(int i = 1; i < 10; i++){
        for(int j = 1; j < 10; j++){
            printf("%d x %d = %d \t", i, j, (i * j));
        }
        printf("\n");
    }
    
}