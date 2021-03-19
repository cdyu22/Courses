#include <stdio.h>

/*
by Connor Yu
due 11/13/2020
A program to output various facts about numbers (square, cube, factorial, etc)
*/
int abs( int n ){
    // If negative, just subtract n from n twice
    if ( n < 0 )
        return ( n - n - n );
    else
        // If it's positive we're done
        return n;
}

int mult( int x, int y ){
    int val = 0;
    //Just need to add x up y times
    for ( int i = 0; i < y; i++ )
        val += x;
    return val;
}

int rfact( int n ){
    if ( n == 1 )
        return 1;
    //If we're not at 1, then multiply it by the factorial of one less than n
    return mult( n, rfact( n - 1 ) );
}

int main(){
    //Values that we're going to be calculating with
    int arr[ 4 ] = {-3, -10, 7, 0};

    //Will keep track of the bits we flip
    int status_byte = 0;

    //Will keep track of the previous calculations
    int absolute, square, cube, fact;

    //Print new line to offset
    printf("\n");

    //Num will hold the actual value
    int num;

    //i serves as a way to work through the array
    int i = 0;
    while ( arr[ i ] ){

        num = arr[ i ];

        //Calculate and print out the values
        printf( "%d\n", num );
        printf( "%#010x\n", num );

        absolute = abs( num );
        printf( "%#010x\n", absolute );

        square = mult( absolute, absolute );
        printf( "%#010x\n", square );

        cube = mult( square, absolute );
        printf( "%#010x\n", cube );

        fact = rfact( absolute );
        printf( "%#010x\n", fact );

        status_byte = 0;

        //Go through the checks, adding if they pass the conditions
        if( absolute % 2 == 1 )
            status_byte += 1;

        if ( num < 0 )
            status_byte += 2;

        if ( fact > square )
            status_byte += 4;

        if ( fact > cube )
            status_byte += 8;

        printf( "%#010x\n", status_byte );

        //Increment i
        i++;
    }
    printf( "\n" );
}
