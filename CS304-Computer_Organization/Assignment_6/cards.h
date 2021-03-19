#ifndef CARDS_H
#define CARDS_H

/*
Connor Yu
11/8/2020
This program is to set up the cards.h type
*/

#include "callouts.h"

typedef struct CARD_T{
    int player;
    int grid[ 5 ][ 5 ];
    char called[ 5 ];
    struct CARD_T *next;
}CARD_T;

static void init_card( int grid[][ 5 ], char *fn );

void init_cards( int num_players, CARD_T **list, char *fns[] );

void update_grid( CARD_T *pcard, CALLOUT_T callout );

int check_grid( CARD_T *pcard );

int update_cards( CALLOUT_T call_num, CARD_T *list );

void print_cards( CARD_T *list );

void free_cards( CARD_T **list );

#endif
