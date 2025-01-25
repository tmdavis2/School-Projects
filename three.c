#include <stdio.h>

void main() {
    double num1 = 1;
    int num2 = 2; 
    char letter1 = 'A';

    double *ptr1 = &num1;
    int *ptr2 = &num2;
    char *ptr3 = &letter1;

    printf("Address of num1: %p\n", ptr1);
    printf("Address of num2: %p\n", ptr2);
    printf("Address of letter1: %p\n", ptr3);
    printf("\n");
    printf("Value of num1: %f\n", *ptr1);
    printf("Value of num1: %d\n", *ptr2);
    printf("Value of num1: %c\n", *ptr3);
    printf("\n");
    printf("Size of num1: %ld\n", sizeof(num1));
    printf("Size of num2: %ld\n", sizeof(num2));
    printf("Size of letter1: %ld\n", sizeof(letter1));
}