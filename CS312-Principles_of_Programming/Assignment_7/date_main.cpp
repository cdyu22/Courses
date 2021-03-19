#include <iostream>
#include <string>
#include "date.hpp"

//Prototype for the helper function
std::string helper_boolean( bool foo );

/*
by Connor Yu
11/4/2020
This program is to drive the main project to compare dates
*/
int main(){

    //Variables for main, three dates and a std::string to print out
    Date *d1;
    Date d2( 30, 12, 1999 );
    Date d3( 1, 1, 2000 );
    std::string str;

    //String to hold either true or false to print out
    std::string bool_helper;

    //Use new operator to allocate memory
    d1 = new Date();

    //Formatting all of the dates to str and printing them out
    d1->format( str );
    std::cout << "\nd1: " << str << "\n";
    d2.format( str );
    std::cout << "d2: " << str << "\n";
    d3.format( str );
    std::cout << "d3: " << str << "\n\n";

    //******************************COMPARISON ONE******************************
    //Checking the initial comparisons of d1, d2, and d3

    //call lessThan method
    std::cout << "d1 < d2? " << helper_boolean( d1->lessThan( d2 ) ) << "\n";
    //call lessThan method
    std::cout << "d2 < d3? " << helper_boolean( d2.lessThan( d3 ) ) << "\n\n";

    //******************************COMPARISON TWO******************************
    //Increment d2's day, format std::string and compare

    //call nextDay method
    d2.nextDay();
    d2.format( str );
    std::cout << "next day d2: " << str << "\n";

    //call overloaded < method
    std::cout << "d2 < d3? " << helper_boolean( d2 < d3 ) << "\n";

    //call overloaded == method
    std::cout << "d2 = d3? " << helper_boolean( d2 == d3 ) << "\n";

    //call overloaded > method
    std::cout << "d2 > d3? " << helper_boolean( d2 > d3 ) << "\n\n";

    //****************************COMPARISON THREE******************************
    //Increment d2's day, format std::string and compare

    //call overloaded ++(postfix)
    d2++;
    d2.format( str );
    std::cout << "next day d2: " << str << "\n";

    //call overloaded == method
    std::cout << "d2 = d3? " << helper_boolean( d2 == d3 ) << "\n\n";

    //*****************************LEAP YEAR CHECK******************************
    //CHECKING 1529
    //call set method
    d1->set( 28, 2, 1529 );
    d1->format( str );
    std::cout << "initialized d1 to " << str << "\n";
    //call nextDay method
    d1->nextDay();
    d1->format( str );
    std::cout << "next day d1: " << str << "\n\n";

    //CHECKING 1460
    //call set method
    d1->set( 28, 2, 1460 );
    d1->format( str );
    std::cout << "initialized d1 to " << str << "\n";
    //call overloaded ++ (prefix)
    ++( *d1 );
    d1->format( str );
    std::cout << "next day d1: " << str << "\n\n";

    //CHECKING 1700
    //call set method
    d1->set( 28, 2, 1700 );
    d1->format( str );
    std::cout << "initialized d1 to " << str << "\n";
    //call overloaded ++ (prefix)
    ++( *d1 );
    d1->format( str );
    std::cout << "next day d1: " << str << "\n\n";

    //CHECKING 1600
    //call set method
    d1->set( 28, 2, 1600 );
    d1->format( str );
    std::cout << "initialized d1 to " << str << "\n";
    //call overloaded ++ (postfix)
    ( *d1 )++;
    d1->format( str );
    std::cout << "next day d1: " << str << "\n\n";
}


std::string helper_boolean( bool foo ){
    if ( foo )
        return "TRUE";
    return "FALSE";
}
