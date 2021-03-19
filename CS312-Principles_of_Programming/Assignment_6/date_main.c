#include <stdio.h>
#include <stdlib.h>
#include "date.h"

//by Connor Yu
//10/28/2020
//This program is to drive the main project to compare dates

int main(){

    //Variables for main, three dates and a string to print out
    DATE_T * d1, d2, d3;
    char format_str[ 30 ];

    d1 = malloc(sizeof(DATE_T));

    //First Initializations
    init_date_1( d1 );
    init_date( &d2, 30, 12, 1999 );
    init_date( &d3, 1, 1, 2000 );

    //Formatting all of the dates to format_str and printing them out
    format_date( *d1, format_str );
    printf( "\nd1: %s", format_str );
    format_date( d2, format_str );
    printf( "\nd2: %s", format_str );
    format_date( d3, format_str );
    printf( "\nd3: %s\n\n", format_str );

    //******************************COMPARISON ONE******************************
    //Check if d1 less than d2, print out true or false depending on result
    printf( "d1 < d2? %s\n", date_less_than( *d1, d2 ) ? "TRUE" : "FALSE" );
    printf( "d2 < d3? %s\n", date_less_than( d2, d3 ) ? "TRUE" : "FALSE" );

    //******************************COMPARISON TWO******************************
    //Increment d2's day, format string and compare
    next_day( &d2 );
    format_date( d2, format_str );
    printf( "\nnext day d2: %s\n", format_str );

    printf( "d2 < d3? %s\n", date_less_than( d2, d3 ) ? "TRUE" : "FALSE" );
    printf( "d2 = d3? %s\n", date_equal( d2, d3 ) ? "TRUE" : "FALSE" );
    printf( "d2 > d3? %s\n", date_less_than( d3, d2 ) ? "TRUE" : "FALSE" );

    //****************************COMPARISON THREE******************************
    //Increment d2's day, format string and compare
    next_day( &d2 );
    format_date( d2, format_str );
    printf( "\nnext day d2: %s\n", format_str );

    printf( "d2 = d3? %s\n", date_equal( d2, d3 ) ? "TRUE" : "FALSE" );

    //*****************************LEAP YEAR CHECK******************************
    //Checking to see if next_day correctly calculates leap_year for 1529
    init_date( d1, 28, 2, 1529 );
    format_date( *d1, format_str );
    printf( "\ninitialized d1 to %s\n", format_str );
    next_day( d1 );
    format_date( *d1, format_str );
    printf( "next day d1: %s\n\n", format_str );

    //Checking to see if next_day correctly calculates leap_year for 1460
    init_date( d1, 28, 2, 1460 );
    format_date( *d1, format_str );
    printf( "initialized d1 to %s\n", format_str );
    next_day( d1 );
    format_date( *d1, format_str );
    printf( "next day d1: %s\n\n", format_str );

    //Checking to see if next_day correctly calculates leap_year for 1700
    init_date( d1, 28, 2, 1700 );
    format_date( *d1, format_str );
    printf( "initialized d1 to %s\n", format_str );
    next_day( d1 );
    format_date( *d1, format_str );
    printf( "next day d1: %s\n\n", format_str );

    //Checking to see if next_day correctly calculates leap_year for 1600
    init_date( d1, 28, 2, 1600 );
    format_date( *d1, format_str );
    printf( "initialized d1 to %s\n", format_str );
    next_day( d1 );
    format_date( *d1, format_str );
    printf( "next day d1: %s\n\n", format_str );

    return EXIT_SUCCESS;
}
