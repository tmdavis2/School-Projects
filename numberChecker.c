#include <stdio.h>
#include <stdbool.h>

void main()
{    
    //checks if number is positive or negative
    int userInputedNum1;
    printf("\nEnter a number:");
    scanf("%d", &userInputedNum1);

    if(userInputedNum1 > 0){
        printf("Positve\n");
    }
    else if(userInputedNum1 == 0){
        printf("Zero\n");
    }
    else{
        printf("Negative\n");
    }


    //checks if the number is even or odd
    int userInputedNum2;

    printf("\nEnter a number:");
    scanf("%d", &userInputedNum1);

    if(userInputedNum1 % 2 == 0){
        printf("Even\n");
    }
    else{
        printf("Odd\n");
    }

}