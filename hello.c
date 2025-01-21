#include <stdio.h>

//converts farenheight to celsius
void main() {
    int num;
    printf("\nEnter a temperature in farenheight: ");
    scanf("%d", &num);
    num = ((num - 32) * 5) / 9;
    printf("Tempertaure in celsius: %d\n", num);
}