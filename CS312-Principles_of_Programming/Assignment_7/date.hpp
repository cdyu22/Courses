#ifndef DATE_HPP
#define DATE_HPP

#include <string>
/*
by Connor Yu
11/13/2020
Designing the date, with fields for day, month, and year.
*/
class Date{
    private:
        int day;
        int month;
        int year;
        std::string monthStr( void );
        bool leapYear( void );
        int monthLength( void );

    public:
        Date( void );
        Date( int day, int month, int year );
        void set( int day, int month, int year );
        bool equals( Date date );
        bool operator==( Date date );
        bool lessThan( Date date );
        bool operator<( Date date );
        bool operator>( Date date );
        void format( std::string &str );
        void nextDay( void );
        void operator++( void );
        void operator++( int dummy );
};

#endif
