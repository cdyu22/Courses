#include <stdio.h>
#include <stdlib.h>

#include "cards.h"

/*
Connor Yu
11/8/2020
This program is to set up, update and check the bingo cards
*/

//***************************SETTING UP BINGO CARDS*****************************

//To set up the grid with the values in the file (fn) passed in
static void init_card( int grid[][ 5 ], char *fn ){

    //The value retrieved from the card that will be stored in the grid
    int val;

    //The bingo card file we open, making sure to only read it
    FILE *bingo = fopen( fn, "r" );

    //Loop through rows and columns
    for ( int row = 0; row < 5; row++ )
        for ( int col = 0; col < 5; col++ ){
            //Scan through the file, storing the values in val, then in the grid
            fscanf( bingo, "%d", &val );
            grid[ row ][ col ] = val;
          }
}

//To set up the linked list of cards with the bingo files (fns) passed in
void init_cards( int num_players, CARD_T **list, char *fns[] ){

    //Setting up two CARD_T pointers, card will be used to set up the cards,
    //next_card will be used to allocate memory to the next card
    CARD_T *card, *next_card;

    //Allocate memory for the initial card to card
    card = malloc( sizeof( CARD_T ) );

    //Card is now effectively the 'head' of the linked list, so point list to it
    *list = card;

    //Loop for the amount of players
    for ( int i = 1; i <= num_players; i++ ){

        //Setting up the attributes of each card
        card->player = i;
        init_card( card->grid, fns[ i ] );

        //Setting each cell in char array to 0, all bits in char set to 0
        for ( int k = 0; k < 5; k++ )
            card->called[ k ] = 0;

        //Except for middle cell, need to flip that, so set the row equal to 4
        //Corresponds to first two bits to 0, third bit to 1, four and five to 0
        card->called[ 2 ] = 4;

        //Loop until last player, allocating memory and setting up links
        if ( i < num_players ){
            next_card = malloc( sizeof( CARD_T ) );
            card->next = next_card;
            card = next_card;
          }
        else
            //If last card, then set the pointer to NULL
            card->next = NULL;
    }
}

//**************************UPDATING/CHECKING CARDS*****************************

//To mark in called if a cell in grid has been called
void update_grid( CARD_T *pcard, CALLOUT_T callout ){

    //Loop through all of the rows
    for ( int row = 0; row < 5; row++ )
        //Callout.letter serves as index, if the grid is equal to the number
        if( pcard->grid[ row ][ callout.letter ] == callout.number ){

            /*
            Set the bitwise value. So 16 corresponds to first bit (of 5) being
            flipped, then if it's 8, it's the second bit being flipped to 1, and
            so on. Need to loop through, using letter as an index again, then
            finally adding it to the called char value
            */
            int bitwise = 16;
            for ( int col = 0; col < callout.letter; col++ )
                bitwise /= 2;
            pcard->called[ row ] += bitwise;

            //Break for efficiency, as assumed no identical number
            break;
        }
}

//Checking if there is a winner
int check_grid( CARD_T *pcard ){

    //CHECKING ROWS: If a value is 31, corresponds to all bits being flipped
    for ( int row = 0; row < 5; row++ )
        if ( pcard->called[ row ] == 31 )
          return 1;

    //CHECKING COLUMNS: Need to loop through all cells
    int bitwise = 16;
    //Loop through all columns
    for ( int col = 0; col < 5; col++ ){

        //Loop through all rows
        for ( int row = 0; row < 5; row++ ){
            //If both bits aren't flipped, as bitwise can only ever have 1
            //flipped bit, then the value isn't marked, break
            if ( !( pcard->called[ row ] & bitwise ) )
                break;

            //If it never breaks, and it's the last row, all spots marked
            if ( row == 4 )
                return 1;
        }
        //Every loop need to divide bitwise by 2 to correspond to column bit
        bitwise /= 2;
    }

    //CHECKING DIAGONALS: Can do this manually
    if ( ( pcard->called[ 0 ] & 16 ) && ( pcard->called[ 1 ] & 8 ) &&
         ( pcard->called[ 2 ] & 4  ) && ( pcard->called[ 3 ] & 2 ) &&
         ( pcard->called[ 4 ] & 1  ) )
        return 1;

    if ( ( pcard->called[ 0 ] & 1  ) && ( pcard->called[ 1 ] & 2 ) &&
         ( pcard->called[ 2 ] & 4  ) && ( pcard->called[ 3 ] & 8 ) &&
         ( pcard->called[ 4 ] & 16 ) )
        return 1;

    //If no winner has been found at this point, return 0
    return 0;
}

//Driving method to update the grid and check for winners
int update_cards( CALLOUT_T call_num, CARD_T *list ){

    //Have a pointer to scan through the list
    CARD_T *card = list;

    //Loop if card isn't null, that is we're not at the end of the linked list
    while ( card != NULL ){
        //Update the card's grid with the callout
        update_grid( card, call_num );

        //Check if that card has now won, if so, return 1
        if ( check_grid( card ) )
            return card->player;

        //Go to next card in linked list
        card = card->next;
    }
    return 0;
}

//****************************Printing/Freeing Cards****************************
//Looping through the cards to print them out
void print_cards( CARD_T *list ){

    //Setting up a pointer to loop through the cards
    CARD_T *cards = list;

    //Loop if card isn't null, that is we're not at the end of the linked list
    while( cards != NULL ){

        //Printing out the player number, spaces used to offset
        printf( "\n" );
        printf( "Player %d                               ", cards->player );
        printf( "Callouts Marked\n" );

        printf( " -----------------------------        " );
        printf( " -----------------------------\n" );

        printf( "|  B  |  I  |  N  |  G  |  O  |       " );
        printf( "|  B  |  I  |  N  |  G  |  O  |\n" );

        //Looping through the rows
        for ( int r = 0; r < 5; r++ ){

            //Printing out the original card
            printf( "|-----+-----+-----+-----+-----|       " );
            printf( "|-----+-----+-----+-----+-----|\n" );

            for ( int c = 0; c < 5; c++ ){
                //If it's the middle entry print a *
                if( r == 2 && c == 2 )
                    printf( "|  *  " );
                else
                    printf( "|  %2d ", cards->grid[ r ][ c ] );
            }
            printf( "|       " );

            //Printing out the cells that are marked/called out
            //Set up integer bitwise
            int bitwise = 16;
            for ( int m = 0; m < 5; m++ ){
                //If both the called and bitwise bit have been flipped print *
                if( bitwise & cards->called[ r ] )
                    printf( "|  *  " );
                //If not, just print the regular number
                else
                    printf( "|  %2d ", cards->grid[ r ][ m ] );
                bitwise /= 2;
            }
            printf( "|\n" );
          }
        printf( " -----------------------------         " );
        printf( "-----------------------------\n" );

        //Go to next card
        cards = cards->next;
    }
    printf("\n");
}

//Returning the memory back to the system once complete
void free_cards( CARD_T **list ){

    //To follow structure of previous methods, set up two pointers//
    //one to the start of the list, one to the next card
    CARD_T *card = *list;
    CARD_T *next_card = card->next;

    //Loop while next isn't null, that is, we're not at the end of the list
    while( next_card != NULL ){
        //Return memory
        free( card );

        //Set card to the next card, and have next_card point to the next card
        card = next_card;
        next_card = next_card->next;
    }
}
