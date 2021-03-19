#include <iostream>
#include <string>
#include <ctime>
#include "date.hpp"

/*
by Connor Yu
11/13/2020
This program allows us to create objects that represent dates compare the
dates, print them out, and increment them (go to the next day)
*/
//*****************************Date Initializations*****************************
//If no date specifications, set the Date to today's date
Date::Date( void ){
    time_t current_time = time( NULL );
    tm *storage = localtime( &current_time );

    //Setting fields
    day = storage->tm_mday;
    month = storage->tm_mon + 1;
    year = storage->tm_year + 1900;
}

//If there are specifications, call set
Date::Date( int day, int month, int year ){
    set( day, month, year );
}

//Sets the date's various fields, corresponding to the values passed in
void Date::set( int day, int month, int year ){
    this->day = day;
    this->month = month;
    this->year = year;
}

//*****************************Comparison Functions*****************************
//Returns true if day, month and year are identical, false otherwise
bool Date::equals( Date date ){
    if ( ( day == date.day ) && ( month == date.month ) &&
         ( year == date.year ) )
        return true;
    return false;
}

//Overrides the == operator, calling equals
bool Date::operator==( Date date ){
    if ( equals( date ) )
        return true;
    return false;
}

//Check if passed in date object comes before passed in date
bool Date::lessThan( Date date ){
    if ( year > date.year )
        return false;
    if ( year < date.year )
        return true;

    //If the years are equal, check the months
    if ( year == date.year ){
        if ( month > date.month )
            return false;
        if ( month < date.month )
            return true;

        //If the months are equal, check the days
        if ( month == date.month ){

              //If the day is before date's day then return true
              if ( day < date.day )
                  return true;
              if ( day >= date.day )
                  return false;
        }
    }

    //Put this as compiler likes a default return value
    return false;
}

//Overriding the < operator, making it call lessThan
bool Date::operator<( Date date ){
    if ( lessThan( date ) )
        return true;
    return false;
}

//Similarly overriding the > operator, making it call lessThan (negated)
bool Date::operator>( Date date ){
    if ( !lessThan( date ) )
        return true;
    return false;
}

//********************************Output String*********************************
//Returns a std::string corresponding to the integer of the month
std::string Date::monthStr( void ){
    switch( month ){
        case 1: return "January";
        case 2: return "February";
        case 3: return "March";
        case 4: return "April";
        case 5: return "May";
        case 6: return "June";
        case 7: return "July";
        case 8: return "August";
        case 9: return "September";
        case 10: return "October";
        case 11: return "November";
        case 12: return "December";
        default: return "unknown";
    }
}

//Formats the fields of date into the std::string passed in by reference
void Date::format( std::string &str ){
    str = monthStr() + " " + std::to_string( day ) + ", "
                     + std::to_string( year );
}

//********************************Increment Day*********************************
//Pass in a year, return true if it's a leap year, false otherwise
bool Date::leapYear( void ){
    //We default to the year being a non-leap year
    bool value = false;

    //If the year is divisible by 4, then set it to true
    if ( !( year % 4 ) )
        value = true;

    //If the year is divisible by 100, then set to false
    if ( !( year % 100 ) )
        value = false;

    //If the year is then also divisible by 400, set to true
    if ( !( year % 400 ) )
        value = true;

    /* Goes through all three if statements, if passes third, passes 2 before
    If passes second, passes 1 before, always returns correct boolean/int */
    return value;
}

//Returns how many days there are in a given month
int Date::monthLength( void ){

    //Switch case, checking the integer of the month
    switch( month ){
        //If it is April, June, October or November we return 30 days
        case 4:
        case 6:
        case 9:
        case 11:
            return 30;

        //If it's 2 we check the leap year, if it is we return 29, if not, 28
        case 2:
            if (leapYear())
                return 29;
            return 28;

        //Then we finally default to 31 days, as the rest of the months have 31
        default:
            return 31;
    }
}

//Increments the day, changing the month and year if necessary
void Date::nextDay( void ){
    //Check if the day is the last day of the given month
    if ( day == monthLength() ){

        //If so, set day to 1
        day = 1;

        //If it is December, set month to January and increment year
        if ( month == 12 ){
            month = 1;
            year++;
        }

        //If it is any other month, just increment month
        else
            month++;
    }

    //If it is not the last day of the month, increment the day
    else
        day++;
}

//Overriding the prefix ++ operator to make it call nextDay
void Date::operator++ (void){
    nextDay();
}

//Similarly overriding the postfix ++ operator to make it call nextDay
//(dummy is used to differentiate between this and the prefix ++)
void Date::operator++ (int dummy){
    nextDay();
}
