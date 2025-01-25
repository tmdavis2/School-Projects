#include <stdio.h>
#include <math.h>

double farenheitToCelsius(double f){
    double c = (f - 32) * 5/9;
    return c;
}

int areaRectangle(int width, int height){
    return width * height;
}

double areaCircle(int radius){
    double area = 3.14159265359 * (pow(radius, 2));
    return area;
}

void main(){

    int numbers[] = {10, 20, 30, 40, 50};
    
    // 3.1
    int *ptr = numbers; 
    printf("Second element: %d\n", *(ptr + 1)); 

    // 3.2
    printf("All elements:\n");
    for (int i = 0; i < 5; i++) {
        printf("%d\n", *(ptr + i)); 
    }


    //3.3
    printf("Enter Temperature in Farenheight: ");
    int enteredTemp;
    scanf("%d", &enteredTemp);
    printf("%d degrees Farenheit to Celsius: %.1f\n",enteredTemp, farenheitToCelsius(enteredTemp));

    printf("\nEnter Length and width of a Rectangle: ");
    int width;
    int length;
    scanf("%d", &length);
    scanf("%d", &width);

    printf("Area of recatngle with length %d and witdth %d: %d\n",length, width, areaRectangle(length, width));

    printf("\nEnter Radius of a circle: ");
    int radius;
    scanf("%d", &radius);
    printf("Area of a Circle with radius %d: %f\n",radius, areaCircle(radius));
}