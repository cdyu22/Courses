#ifndef CALLOUTS_H
#define CALLOUTS_H

/*
Connor Yu
11/8/2020
This program is to set up the callouts.h type
*/

#include "bingo.h"

typedef struct CALLOUT_T{
    BINGO_T letter;
    int number;
}CALLOUT_T;

void init_callouts( char *fn );

char *get_callout_str( CALLOUT_T callout );

CALLOUT_T get_callout( void );

void free_callouts( void );


#endif
