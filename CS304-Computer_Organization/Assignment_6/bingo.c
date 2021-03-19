#include <stdio.h>

#include "bingo.h"
#include "cards.h"
#include "callouts.h"

/*
Connor Yu
11/8/2020
This program is to drive the main project to play bingo with a do-while loop
*/

void main( int argc, char *argv[] ){


    //**************************Setting up Bingo Cards**************************
    //Setting up the linked list of bingo cards
    CARD_T *b_cards = NULL;

    //All entries in command line are players except two
    int num_players = argc - 2;

    //We pass the last entry into init_callouts, decrement as 0-based
    init_callouts( argv[ --argc ] );

    //Initialize the bingo cards, passing in the linked list, players and cards
    init_cards( num_players, &b_cards, argv );


    //************************Preparing for do-while Loop***********************
    //Print the cards to show initial layout
    print_cards( b_cards );

    //Follows if a winner has been found, 1 if found, 0 if not
    int winner = 0;

    //Tracks if we need to print out cards or not
    int print_counter = 1;

    //Holds a copy of the callout for printing and referencing
    CALLOUT_T called;

    do{
        //Get the callout and store it in called
        called = get_callout();

        //Print the callout retrieved
        printf( "callout: %s\n\n", get_callout_str( called ) );

        //Update cards, marking if necessary, and checking for a winner
        winner = update_cards( called, b_cards );

        //When print_counter is 5  with no winner, print cards and reset counter
        if ( ( print_counter == 5 ) && !winner ){
            print_cards( b_cards );
            print_counter = 0;
        }

        //Increment print_counter every loop
        print_counter++;

    //Loop until a winner is found
    }while( !winner );

    printf( "\nPlayer %d: BINGO!\n", winner );

    //Print out final card set
    print_cards( b_cards );

    //Return the memory allocated to the cards and callouts to the system
    free_cards( &b_cards );
    free_callouts();
}
