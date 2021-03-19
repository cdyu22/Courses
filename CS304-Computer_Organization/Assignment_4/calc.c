#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include "calc.h"

//**********************************Prototypes**********************************
//Old Methods: Assignment 2
short get_operand ( char mode );
void print_acc ( short acc, char mode );
char print_menu ( void );
int main ( void );

//New Methods: Assignment 4
unsigned short get_binary_op ( char *bin );
void convert_to_binary ( short acc, char *bin );
void add ( short *acc, char mode );
void subtract ( short *acc, char mode );

//**********************************Main Method*********************************
//The main method, will call other functions and handle valid inputs
int main( void )
{
    //Defaults to decimal mode and accumulator equal to zero
    char mode = 'D';
    short accumulator = 0;

    //Stores the option that the user picks from menu
    char option;

    //Practical boolean, set to zero when user wants to exit program
    int quit = 1;

    //Two bin_str, main_bin is to hold the bin_str that we convert back and
    //forth from the accumulator value to the binary value.
    //bitwise_bin holds a temporary bin_str for bitwise operations
    bin_str main_bin, bitwise_bin;

    //Used for shifts to hold the amount of times we shift the bits
    int shift;

    //While quit is 1, it will loop
    while ( quit )
    {
        //At the start of every loop, print the accumulator and menu
        print_acc( accumulator, mode );
        option = print_menu();

        //Use switch statement to account for all possible valid user options
        switch( option )
        {
          //************************Assignment Two Cases************************
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

          //***********************Assignment Four Cases************************
          //Set mode to B, which later methods will recognize as binary mode
          case 'B':
              mode = 'B';
              printf( "Mode is Binary\n" );
              break;

          //For negation, just need to multiply by -1
          case 'N':
              accumulator *= -1;
              break;

          //Recognize we need to add, call addition method
          case '+':
              add( &accumulator, mode );
              break;

          //Recognize we need to subtract, call addition method
          case '-':
              subtract( &accumulator, mode );
              break;

          //Complement requires going bit by bit and reversing
          case '~':
              //Update main_bin to hold bits corresponding to current acc value
              convert_to_binary( accumulator, main_bin.bin );

              //Loop through the buts, switching 0 to 1 and vice versa
              for ( int i = 0; i < 19; i++ )
              {
                  if ( main_bin.bin[ i ] == '0' )
                      main_bin.bin[ i ] = '1';
                  else if (main_bin.bin[ i ] == '1')
                      main_bin.bin[ i ] = '0';
              }

              //Convert the bits in main_bin to a short value for accumulator
              accumulator = get_binary_op( main_bin.bin );
              break;

          //AND case, go through the two bit strings
          case '&':
              //Convert accumulator and other short value to bit string
              convert_to_binary( accumulator, main_bin.bin );
              convert_to_binary( get_operand( mode ), bitwise_bin.bin );

              //Loop through all of the bits, fill main_bin
              for ( int i = 0; i < 19; i++ )
              {
                  //Pass if i is 4, 9, or 14, as those spaces have ' '
                  if ( i % 5 == 4 )
                      continue;

                  //Case to turn cell value to 1
                  if ( main_bin.bin[ i ] == '1' && bitwise_bin.bin[ i ] == '1' )
                      main_bin.bin[ i ] = '1';

                  //Case to turn cell value to 0
                  else
                      main_bin.bin[ i ] = '0';
              }

              //Convert bin back to short value
              accumulator = get_binary_op( main_bin.bin );
              break;

          //OR case
          case '|':
              convert_to_binary( accumulator, main_bin.bin );
              convert_to_binary( get_operand( mode ), bitwise_bin.bin );

              for ( int i = 0; i < 19; i++ )
              {
                  if ( i % 5 == 4 )
                      continue;

                  //Only difference, set main_bin cell to 1 if either have 1
                  if ( main_bin.bin[ i ] == '1' || bitwise_bin.bin[ i ] == '1' )
                      main_bin.bin[ i ] = '1';

                  else
                      main_bin.bin[ i ] = '0';
              }

              accumulator = get_binary_op( main_bin.bin );
              break;

          //XOR case
          case '^':
              convert_to_binary( accumulator, main_bin.bin );
              convert_to_binary( get_operand( mode ), bitwise_bin.bin );

              for ( int i = 0; i < 19; i++ )
              {
                  if ( i % 5 == 4 )
                      continue;
                  //Only difference, set to 1 if only one of the cells has 1
                  if ( main_bin.bin[ i ] == '0' && bitwise_bin.bin[ i ] == '1'||
                       main_bin.bin[ i ] == '1' && bitwise_bin.bin[ i ] == '0' )
                      main_bin.bin[ i ] = '1';
                  else
                      main_bin.bin[ i ] = '0';
              }

              accumulator = get_binary_op( main_bin.bin );
              break;

          //Left Shift case
          case '<':

              //Get amount of positions to shift and store in shift
              printf( "Enter number of positions to left shift accumulator:" );
              scanf( " %d", &shift );
              printf( " %d\n", shift );

              //Use the in-built C left shift operator
              accumulator = accumulator << shift;
              break;


          //Right Shift case
          case '>':

              //Get amount of positions to shift and store in shift
              printf("Enter number of positions to right shift accumulator:");
              scanf( " %d", &shift );
              printf(" %d\n", shift );

              //Use the in-built C right shift operator
              accumulator = accumulator >> shift;
              break;
        }
    }

    printf("\n");
    return 0;
}

//******************************get_operand Method******************************
//When user chooses to set accumulator, takes in value considering current mode
short get_operand ( char mode )
{
    //The value we will return
    short acc;

    //The two bin_str that are used for taking in a binary string in 'B' mode
    bin_str binary_str, input;

    //Switch statement to allow for every mode.
    //They ask for the designated value, take it and store it, then echo it back
    switch( mode )
    {

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

      //*****************************Assignment 4*******************************
      //Binary Case
      case 'B':
          /*
          The problem with placing the bit string into input.bin is that there
          are no spaces in the input and, if input is less than 16, we need to
          pad zeroes into the bit string
          */
          printf( "Enter binary value: " );

          //Need to take the input as a string (char array), and put it in input
          scanf( "%s", input.bin );

          //Figure out the length of the bit string that was input
          int length = strlen( input.bin );

          //Echo print the input string
          for ( int j = 0; j < length; j++ )
              printf( "%c", input.bin[ j ] );

          //Serves to pad in the zeroes and the spaces
          //Will maintain the cell that we're placing the bit in
          int length_pointer = 0;

          //Records the amount of zeroes we need to pad into the bit string
          int zeroPad = 16 - length;

          //Use a for loop to fill the binary_str
          for ( int i = 0; i < 19; i++ )
          {
              //If the cell is in 4, 9, or 14, place a space and loop again
              if ( i % 5 == 4 )
              {
                  binary_str.bin[ i ] = ' ';
                  continue;
              }

              //If there are still zeroes we need to pad, place a zero in
              //and decrement zeroPad
              if ( 0 < zeroPad )
              {
                  binary_str.bin[ i ] = '0';
                  zeroPad--;
              }

              //If we have gotten through all of the zeroes and no space is
              //required place the corresponding input bin bit into binary_str
              else
              {
                  binary_str.bin[ i ] = input.bin[ length_pointer ];

                  //Increment length_pointer
                  length_pointer++;
              }
          }
          printf("\n");

          //Convert the valid binary_str to a short value
          acc = get_binary_op( binary_str.bin );
          break;
    }

    return acc;
}

//*******************************print_acc Method*******************************
//Printing out the accumulator and all of its values
void print_acc( short acc, char mode )
{
    printf( "\n****************************************\n" );

    //Need unique string for first line of accumulator for every mode
    switch( mode )
    {
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

      //Binary Case
      case 'B':
          printf( "* Accumulator:         Input Mode: Bin *\n" );
    }

    //Need to initialize a binary string
    bin_str bin_string;

    //Convert the accumulator to a binary string
    convert_to_binary( acc, bin_string.bin );
    printf( "*   Binary  :  " );

    //Then print out the binary string
    for ( int i = 0; i < 19; i++ )
        printf( "%c", bin_string.bin[ i ] );

    printf( "     *\n" );

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
char print_menu( void )
{
    //Will only look at first entry, allows for longer strings for echo printing
    char input[ 10 ];

    //All valid inputs stored in char array. Seventeen cells to allow \n as well
    char valid_input[ 17 ] = "BOHDCSQ&|^~<>+-N";

    //The char that we will return, will equal some value in valid_input
    char option;

    //Variable that will serve as a boolean changed to 0 when valid input found
    int is_valid = 1;

    //Loop that stops when a valid option is selected
    while( is_valid )
    {
        //The list of all options from the menu
        printf( "Please select one of the following options: \n\n" );
        printf( "B  Binary Mode             ");
        printf( "&  AND with Accumulator           ");
        printf( "+  Add to Accumulator\n");

        printf( "O  Octal Mode              " );
        printf( "|  OR  with Accumulator           " );
        printf( "-  Subtract from Accumulator\n" );

        printf( "H  Hexadecimal Mode        " );
        printf( "^  XOR with Accumulator           " );
        printf( "N  Negate Accumulator\n" );

        printf( "D  Decimal Mode            " );
        printf( "~  Complement Accumulator\n\n" );

        printf( "C  Clear Accumulator       " );
        printf( "<  Shift Accumulator Left\n" );
        printf( "S  Set Accumulator         " );
        printf( ">  Shift Accumulator Right\n\n" );
        printf( "Q  Quit \n\n" );
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
        if ( strlen( input ) > 1 || !strchr( valid_input , option ))
            printf( "\nInvalid option: %s\n\n", input );

        //If a valid option is found, flip it to zero, loop will stop
        else
            is_valid = 0;

    }

    //Return the valid option when valid option is input
    return option;
}

//****************************Assignment Four Methods***************************
//Convert bin str to short; return value.
unsigned short get_binary_op ( char *bin )
{
    //The binary_op that we'll return. It's unsigned, so we can't return a
    //negative number. The bits will get reinterpreted, if needed, as negative
    //if we pass it to a regular short.
    unsigned short binary_op = 0;

    //So we start at 2 to the 15th, which is the max value we can add
    int adder = 32768;

    //Loop through the binary string passed in
    for ( int i = 0; i < 19; i++ )
    {
        //If the cell doesn't have a 0 or 1, continue
        if ( bin[ i ] != '0' && bin[ i ] != '1' )
            continue;

        //If there's a 1, add the adder value, doing nothing if there's a zero
        if ( bin[ i ] == '1' )
            binary_op += adder;

        //For every valid loop, divide the adder by 2
        adder /= 2;
    }

    //Return the binary_op, it will reinterpret the bits if passed to a short
    return binary_op;
}

//Convert acc to binary str for output
void convert_to_binary ( short acc, char *bin )
{
    //Intrpret the acc as unsigned
    unsigned short value = ( unsigned short ) acc;

    //Checker will compare the value to the checker
    unsigned short checker = 32768;

    //Loop through the bin
    for ( int i = 0; i < 20; i++ )
    {
        //If the cells are 4, 9, or 14, input a space and continue
        if ( i % 5 == 4 )
        {
            bin[ i ] = ' ';

            //The only place valid binary strings are created, so place \0
            if ( i == 19 )
                bin[ i ] = '\0';

            continue;
        }

        //If the checker is less than value, put a 1 and subtract the checker
        //value from the current value
        if ( checker <= value )
        {
            value = value - checker;
            bin[ i ] = '1';
        }

        //If not, then put a zero
        else if ( checker > value )
            bin[ i ] = '0';

        //Every valid loop, need to divide checker by 2
        checker /= 2;
    }
}

//The addition function. It takes the accumulator value and mode
//Takes accumulator value by reference, operations will change value passed in
void add ( short *acc, char mode )
{
    //Waits for user input to get the value the user wants to add
    short adder = get_operand( mode );

    //Adds the two together
    short result = adder + *acc;

    //Detect if the two operands were positive, and the result is negative
    if ( 0 < adder && 0 < *acc && result < 0 )
          printf( "Positive Overflow\n" );

    //Detect if the two operands were negative, and the result is positive
    if ( adder < 0 && *acc < 0 && 0 < result )
          printf( "Negative Overflow\n" );

    //Set the accumulator equal to the result
    *acc = result;
}

//The subtraction function. It takes the accumulator and mode
void subtract( short *acc, char mode )
{
    //Waits for user input to get the value the user wants to detract
    short detractor = get_operand( mode );

    //Multiply the detractor by negative one, then do the same operations as add
    detractor *= -1;

    short result = detractor + *acc;
    if ( 0 < detractor && 0 < *acc && result < 0 )
        printf( "Positive Overflow\n" );
    if ( detractor < 0 && *acc < 0 && 0 < result )
        printf( "Negative Overflow\n" );
    *acc = result;
}
