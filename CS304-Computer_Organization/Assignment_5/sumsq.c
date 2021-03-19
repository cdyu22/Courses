#include <stdio.h>

/*
Sums up all numbers from zero to the integer passed in. This will be run
outer times.
*/
int sumsq( int outer ){
    //Sum is the value that will be stored in memory
    int sum = 0;

    //We then run the middle loop, which loops up until outer
    for ( int middle = 1; middle <= outer; middle++ )

        //We then run the inner loop, which loops until middle
        for ( int inner = 1; inner <= middle; inner++ )

            //Every time inner is run, we add middle to sum
            sum += middle;

    //We return the sum, serves to 'store' it in memory
    return sum;
}

/*
The main program. Calls sumsq a certain amount of times, then prints
out the number and the result in decimal and hex.
*/
void main(){

    //The sum that we 'store,' in this program we print it out, in assembly
    //we commit it to memory
    int sum;

    //We run this loop, default is set to 10
    printf("\n");
    for ( int outer = 1; outer <= 10; outer++ )
    {
        //Run sumsq
        sum = sumsq( outer );

        //Print the number and its result in decimal and hex
        printf( "%2d: %4d %4x \n", outer, sum, sum );
    }
    printf("\n");
}
