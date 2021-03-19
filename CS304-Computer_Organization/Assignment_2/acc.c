#include <stdio.h>
#include <ctype.h>
#include <string.h>

//Prototypes
short get_operand ( char mode );
void print_acc ( short acc, char mode );
char print_menu ( void );
int main ( void );

//**********************************Main Method*********************************
//The main method, will call other functions and handle valid inputs
int main( void ){
    //Defaults to decimal mode and accumulator equal to zero
    char mode = 'D';
    short accumulator = 0;

    //Stores the option that the user picks from menu
    char option;

    //Practical boolean, set to zero when user wants to exit program
    int quit = 1;

    //While quit is 1, it will loop
    while ( quit ){

        //At the start of every loop, print the accumulator and menu
        print_acc( accumulator, mode );
        option = print_menu();

        //Use switch statement to account for all possible user options
        switch(option){

          case 'O':
              //Set mode and inform user of the change
              mode = 'O';
              printf( "Mode is Octal\n" );
              break;

          case 'H':
              mode = 'H';
              printf( "Mode is Hexadecimal\n" );
              break;

          case 'D':
              mode = 'D';
              printf( "Mode is Decimal\n" );
              break;

          //User chose to clear accumulator
          case 'C':
              //Set accumulator to zero and loop again
              accumulator = 0;
              break;

          //User chose to set accumulator
          case 'S':
              //Store accumulator value
              accumulator = get_operand( mode );
              break;

          //User chose to quit the program
          case 'Q':
              //Set practical boolean to zero
              quit = 0;
              break;
        }
    }
    printf("\n");
    return 0;
}

//******************************get_operand Method******************************
//When user chooses to set accumulator, takes in value considering current mode
short get_operand ( char mode ){

    //The value we will return
    short int acc;

    //Switch statement to allow for every mode.
    //They ask for the designated value, take it and store it, then echo it back
    switch( mode ){

      //Hexadecimal Case
      case 'H':
          printf( "Enter hex value: " );
          //Take in value
          scanf( "%hX", &acc );
          //Echo print
          printf( "%hX\n", acc );
          break;

      //Octal Case
      case 'O':
          printf( "Enter octal value: " );
          scanf( "%ho", &acc );
          printf( "%ho\n", acc );
          break;

      //Decimal Case
      case 'D':
          printf( "Enter decimal value: " );
          scanf( "%hd", &acc );
          printf( "%hd\n", acc );
          break;
    }

    return acc;
}

//*******************************print_acc Method*******************************
//Printing out the accumulator and all of its values
void print_acc( short acc, char mode ){

    printf( "\n****************************************\n" );

    //Need unique input mode string for every mode
    switch( mode ){

      //Hexadecimal Case
      case 'H':
          printf( "* Accumulator:         Input Mode: Hex *\n" );
          break;

      //Octal Case
      case 'O':
          printf( "* Accumulator:         Input Mode: Oct *\n" );
          break;

      //Decimal Case
      case 'D':
          printf( "* Accumulator:         Input Mode: Dec *\n" );
          break;
    }

    //Interpret the bits for hexadecimal with 4 digits
    printf( "*   Hex     :  %04hX                    *\n", acc );

    //Interpret the bits for octal with 6 digits
    printf( "*   Octal   :  %06ho                  *\n", acc );

    //Interpret the bits for decimal, left justification
    //Can have max amount of 6 digits: -32768
    printf( "*   Decimal :  %-6hd                  *\n", acc );

    printf( "****************************************\n\n" );
}

//******************************print_menu Method*******************************
//Prints out all the options and returns a valid input
char print_menu( void ){

    //Will only look at first entry, allows for longer strings for echo printing
    char input[ 10 ];

    //All valid inputs stored in char array. Seven cells to allow \n as well
    char valid_input[ 7 ] = "OHDCSQ";

    //The char that we will return, will equal some value in valid_input
    char option;

    //Variable that will serve as a boolean changed to 0 when valid input found
    int is_valid = 1;

    //Loop that stops when a valid option is selected
    while(is_valid){
        //The list of all options from the menu
        printf( "Please select one of the following options: \n\n" );
        printf( "O  Octal Mode\n" );
        printf( "H  Hexadecimal Mode\n" );
        printf( "D  Decimal Mode\n\n" );
        printf( "C  Clear Accumulator\n" );
        printf( "S  Set Accumulator\n\n" );
        printf( "Q  Quit\n\n" );
        printf( "Option: " );

        //Waiting for user's chosen option, store it in input
        scanf( "%s", input );

        //Then, after they input it, echo print it back
        printf( "%s\n", input );

        //Will look at first entry in input
        //Make uppercase to allow for both upper and lowercase
        option = toupper( input[ 0 ] );

        /*
         * Check to see if the input is valid. If it is not, then we loop again,
         * looping until a valid option is found.
         */
        if ( strlen( input ) > 1 || !strchr( valid_input , option )){
            printf( "\nInvalid option: %s\n\n", input );
        }
        //If a valid option is found, flip it to zero, loop will stop
        else{
            is_valid = 0;
        }
    }
    //Return the valid option when valid option is input
    return option;
}
