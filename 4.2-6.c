#include <stdio.h>
#include <stdlib.h>


struct House{
    char address[100];
    int price;
    int squareFeet;
    int bedroomNumber;
    int bathroomNumber;
};


void main(){
    FILE *fptr;


    //4.1 and 4.2


    // adding text to the file
    fptr = fopen("hello.txt", "w");
    fprintf(fptr, "\"Hello,\nHow are you?,\nMy name is ...\nWhat's your name?\"");
    fclose(fptr);

    //reading from the file 
    fptr = fopen("hello.txt", "r");
    char myString[100];


    //4.3 and 4.4


    //checks if file exists
    if(fptr != NULL){
        //takes one line
        fgets(myString, 100, fptr);
        printf("%s", myString);

        //prints mu;tiple
        while(fgets(myString, 100, fptr)){
            printf("%s", myString);
        }
        printf("\n");
    }
    else{
        printf("Unable to open file");
    }
    fclose(fptr);

    //prints amount of characters in file
    // FILE* fp;
    // fp = fopen("hello.txt", "r");
    // fseek(fp, 0, SEEK_END);
    // printf("%ld\n", ftell(fp));
    // fclose(fp);


    //4.5


    struct House house1 = {"Spring Meadows", 500000, 3000, 4, 4};
    struct House house2 = {"Daytona Dr", 350000, 2000, 3, 3};
    struct House house3 = {"Harrison st", 400000, 2700, 4, 4};

    printf("Address: %s Price: $%d Square feet: %d Number of Bedrooms: %d Number of Bathrooms: %d\n", house1.address, house1.price, house1.squareFeet, house1.bedroomNumber, house1.bathroomNumber);
    printf("Address: %s Price: $%d Square feet: %d Number of Bedrooms: %d Number of Bathrooms: %d\n", house2.address, house2.price, house2.squareFeet, house2.bedroomNumber, house2.bathroomNumber);
    printf("Address: %s Price: $%d Square feet: %d Number of Bedrooms: %d Number of Bathrooms: %d\n", house3.address, house3.price, house3.squareFeet, house3.bedroomNumber, house3.bathroomNumber);
    //allocate memory
    int students[20];
    printf("%lu\n", sizeof(students));


    //4.6

    int numberOfStudents;
    printf("Enter number of students: ");
    scanf("%d", &numberOfStudents);
    
    int *scores = calloc(numberOfStudents, sizeof(numberOfStudents));

    for(int i = 0; i < numberOfStudents; i++){
        printf("Enter score out of 100 for student %d:", i + 1);
        scanf("%d", &scores[i]);
    }

    fptr = fopen("hello.txt", "a");
    
    
    for(int i = numberOfStudents; i > 0; i--){
        fprintf(fptr, "\n");
        fprintf(fptr, "Score of student %d: %d", i, scores[i-1]);
    }

    free(scores);

    fclose(fptr);
}



