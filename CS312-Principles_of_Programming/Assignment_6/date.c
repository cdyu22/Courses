#include "date.h"
#include <stdio.h>
#include <time.h>


//by Connor Yu
//10/28/2020
/*This program allows us to create objects that represent dates compare the
dates, print them out, and increment them (go to the next day)*/


//*****************************Date Initializations*****************************
//The first init type, we can pass in our own specific day, month and year
void init_date( DATE_T *date , int day, int month, int year ){

    //Simply goes through datet and sets its fields
    date->day = day;
    date->month = month;
    date->year = year;
}

//The second init type, just pass in a date_t, sets it equal to current date
void init_date_1( DATE_T *date ){

    //Get the current date and time, then store to be retrieved later
    time_t current_time = time( NULL );
    struct tm storage = *localtime( &current_time );

    //Set day of DATE_T object to current day
    date->day = storage.tm_mday;

    //Increment, as it goes from 0 to 11
    date->month = storage.tm_mon + 1;

    //Add 1900, as it stores years since 1900
    date->year = storage.tm_year + 1900;
}


//*****************************Comparison Functions*****************************
//Check if two DATE_T objects are representing the same date
int date_equal( DATE_T date1, DATE_T date2 ){

    //If they have the same year, month and day then return true
    if ( ( date1.day == date2.day ) && ( date1.month == date2.month ) &&
         ( date1.year == date2.year ) )

        //Return true (1) if they are equal
        return 1;

    else
        //Return false (0) if they are not equal
        return 0;
}

//Check if date1 comes before date2
int date_less_than( DATE_T date1, DATE_T date2 ){

    //If the year of date1 is after that of date2, then return false (0)
    if ( date1.year > date2.year )
        return 0;

    //If the year of date1 is before that of date2, return true (1)
    if ( date1.year < date2.year )
        return 1;

    //If the year of date1 and date2 are equal, similarly check the months
    if ( date1.year == date2.year ){

        //Repeat same procedure conducted with years, but with months
        if ( date1.month > date2.month )
            return 0;
        if ( date1.month < date2.month )
            return 1;

        //If the months are the same, check the days
        if ( date1.month == date2.month ){

              //If the day is before date2, then return true(1)
              if ( date1.day < date2.day )
                  return 1;
              if ( date1.day >= date2.day )
                  return 0;
        }
    }
}


//********************************Output String*********************************
//Returns a string corresponding to the integer of the month
static char *month_str( int month ){
    //Return char array in months corresponding to int passed in, enter
    //switch statement based on number

    switch (month){
        case 1:
            return "January";

        case 2:
            return "February";

        case 3:
            return "March";

        case 4:
            return "April";

        case 5:
            return "May";

        case 6:
            return "June";

        case 7:
            return "July";

        case 8:
            return "August";

        case 9:
            return "September";

        case 10:
            return "October";

        case 11:
            return "November";

        case 12:
            return "December";
    }
}

//Formats the fields of date into the string passed in (by reference)
void format_date( DATE_T date, char *str ){
    //Put month string, day and year into str
    sprintf( str, "%s %d, %d", month_str( date.month ), date.day, date.year );
}

//********************************Increment Day*********************************
//Pass in a year, return true (1) if it's a leap year, false (0) otherwise
static int leap_year( int year ){

    //We default to the year being a non-leap year
    int value = 0;

    //If the year is divisible by 4, then set it to true (1)
    if ( !( year % 4 ) )
        value = 1;

    //If the year is divisible by 100, then set to false (0)
    if ( !( year % 100 ) )
        value = 0;

    //If the year is then also divisible by 400, set to true (1)
    if ( !( year % 400 ) )
        value = 1;

    /* Goes through all three if statements, if passes third, passes 2 before
    If passes second, passes 1 before, always returns correct boolean/int */
    return value;
}

//Returns how many days there are in a month
static int month_length( int month, int leap ){

    //Int arrays that hold the month values with their specified amount of days
    int ThirtyOne[ 7 ] = { 1, 3, 5, 7, 8, 10, 12 };
    int Thirty[ 4 ] = { 4, 6, 9, 11 };

    //Iterate through ThirtyOne, if the month value passed in corresponds to a
    //value in the array, we return 31
    for ( int i = 0; i < 7; i++ )
        if ( ThirtyOne[ i ] == month )
            return 31;

    //Iterate through Thirty, if the month value passed in corresponds to a
    //value in the array, we return 30
    for ( int i = 0; i < 4; i++ )
        if ( Thirty[ i ] == month )
            return 30;

    //If the function gets here, it must be February, if it is not a leap year
    //we return 28
    if ( !leap )
        return 28;

    //If it is a leap year we return 29
    if ( leap )
        return 29;
}

//Increments a DATE_T's day field, changing the month and year if necessary
void next_day( DATE_T *date ){

    //Check if the day is the last day of the given month
    if ( date->day == month_length( date->month, leap_year( date->year ) ) ){

        //If so, set day to 1
        date->day = 1;

        //If it is December, set month to January and increment year
        if ( date->month == 12 ){
            date->month = 1;
            date->year++;
        }

        //If it is any other month, increment month
        else
            date->month++;
    }

    //If it is not the last day of the month, increment the day
    else
        date->day++;
}
