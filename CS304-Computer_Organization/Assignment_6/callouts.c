#include <stdio.h>
#include <stdlib.h>

#include "callouts.h"

/*
Connor Yu
11/8/2020
This program is to set up the callouts from the file, and getting them
*/

//The global static variable num_array, holds all of the callouts
static CALLOUT_T *num_array;

//************************************SETUP*************************************
//Reading in the callouts from the file fn
void init_callouts( char *fn ){

    //Tracks the total amount of callouts read in
    int cells = 0;

    //The file that we opn, making sure to only read it
    FILE *fd = fopen( fn, "r" );

    //The character array that holds the callout as a string
    char str[ 5 ];

    //Scan through the file, if it returns 1 (not at the end), increment cells
    while ( fscanf( fd, "%s", str ) == 1 )
        cells++;

    //Return to the beginning of the text file
    fseek( fd, 0, SEEK_SET );

    //Allocate space to num_array, can do this as it is a pointer
    num_array = malloc( sizeof( CALLOUT_T ) * cells );

    //Will temporarily hold the letter and number of the callouts
    char letter_holder;
    int number_holder;

    //Loop through all of the cells
    for( int i = 0; i < cells; i++ ){

        //Scan the file, and put the variables in their temporary holders
        fscanf( fd, "%c%d ", &letter_holder, &number_holder );

        //Switch statement to put the corret BINGO_T enum type in letter
        switch ( letter_holder ){
            case 'B':
                num_array[ i ].letter =  B;
                break;

            case 'I':
                num_array[ i ].letter = I;
                break;

            case 'N':
                num_array[ i ].letter = N;
                break;

            case 'G':
                num_array[ i ].letter = G;
                break;

            case 'O':
                num_array[ i ].letter = O;
                break;
          }

        //Now put the number in number_holder
        num_array[ i ].number = number_holder;
    }
}

//Return a character array with the correct letter and number
char *get_callout_str( CALLOUT_T callout ){

    //Make it static, or else we can't return it
    static char str[ 5 ];

    //Put them, using sprintf, into str, and return str
    sprintf( str, "%c%d", "BINGO"[ callout.letter ], callout.number );
    return str;
}

//Get the next callouts
CALLOUT_T get_callout( void ){

    //Use a static integer for index, so it exists between calls
    static int index = -1;

    //Increment index
    index++;

    //Return that callout, started index at -1 so first callout returned is 0th
    return num_array[index];
}

//Freeing the memory once done with the program
void free_callouts(void){
    //Done with the program, return the memory alloacted to num_array
    free(num_array);
}
