#include <stdio.h>

void main() {
    int num1;
    int num2;

    printf("Enter two numbers: ");

    scanf("%d", &num1);
    scanf("%d", &num2);

    int *ptr1 = &num1;
    int *ptr2 = &num2;

    int total = *ptr1 + *ptr2;
    printf("Total: %d\n", total);
}