#include <stdio.h>
#include <stdlib.h>

struct{
    char c;
    short s;
    int n;
} A[4][7];

void main (void){
    printf("%d\n",&A);
    printf("%d\n",&A[1][5].s);
    printf("%d\n",&A[3][6].s);
    printf("%d\n\n",&A[2][2].n);

    printf("%d\n",&A[0][1]);
}
