uses sysutils;

{Connor Yu}
{10/14/2020}
{This program allows us to create objects that represent dates compare the}
{dates, print them out, and increment them (go to the next day)}

{*********************************type/const***********************************}
type
    {The possible values a day can have}
    day_range = 1..31;

    {The range of months, going from 1 (January) to 12 (December)}
    month_range = 1..12;

    {The record that we will use to represent a date}
    date_t = record
        {Contains a day, month, and year}
        day : day_range;
        month : month_range;
        year : integer;
    end;

{The array of all months we use for the month_str function}
{Returns the correct string corresponding to the month integer passed in}
const
    months : array[ 1..12 ] of string = ( 'January', 'February', 'March',
                                          'April', 'May', 'June', 'July',
                                          'August', 'September', 'October',
                                          'November', 'December' );

{*****************************Date Initializations*****************************}
{The first init type, we can pass in our own specific day, month and year}
procedure init_date ( var dt : date_t; day : day_range;
                      month : month_range; year : integer );
begin
    {Simply goes through dt and sets its fields}
    dt.day := day;
    dt.month := month;
    dt.year := year;
end;

{The second init type, just pass in a date_t, sets it equal to current date}
procedure init_date1 ( var dt : date_t );
var
    {Variables to hold current date values}
    year, month, day : word;
begin
    {Decode them, which sets their values to the current date}
    DecodeDate( Date, year, month, day );

    {Then set dt's fields}
    dt.day := day;
    dt.month := month;
    dt.year := year;
end;

{*****************************Comparison Functions*****************************}
{Check if two date_t objects are representing the same date, true if equal}
function date_equal ( date1 : date_t; date2 : date_t ) : boolean;
begin
    {If they have the same year, month and day then return true}
    if ( date1.year = date2.year ) and ( date1.month = date2.month ) and
       ( date1.day = date2.day ) then
        date_equal := true
    else
        {If they have a different field then return false}
        date_equal := false;
end;

{Check if date1 is before date2, true if it is}
function date_less_than ( date1 : date_t; date2 : date_t ) : boolean;
begin
    {If the year of date1 is after that of date2, then return false}
    if date1.year > date2.year then
        date_less_than := false;

    {If the year of date1 is before that of date2, return true}
    if date1.year < date2.year then
        date_less_than := true;

    {If the year of date1 and date2 are equal, similarly check the months}
    if date1.year = date2.year then

        {Equal Years}
        begin
        if date1.month > date2.month then
            date_less_than := false;

        if date1.month < date2.month then
            date_less_than := true;

        {If the months are the same, check the days}
        if date1.month = date2.month then

            {Equal Months}
            begin
            {If the day is before date2, then return true}
            if date1.day < date2.day then
                date_less_than := true
            else
                {If it's greater or equal to the day of date2, return false}
                date_less_than := false;

            {Equal Months}
            end;

        {Equal Years}
        end;
end;

{********************************Output String*********************************}
{Returns a string corresponding to the integer of the month}
function month_str( month : month_range ) : string;
begin
    {Checks array months, using the integer passed in as the index}
    month_str := months[ month ];
end;

{Formats the fields of dt to a string}
procedure format_date( dt : date_t; var ret_str : string );
var
    tmp_day, tmp_year : string;
begin
    {Change the day/year integers to strings temporarily}
    str( dt.day, tmp_day );
    str( dt.year, tmp_year );

    {Then concatenate it and put it in one string}
    ret_str := month_str( dt.month ) + ' ' + tmp_day + ', ' + tmp_year;
end;

{********************************Increment Day*********************************}
{Increments a date_t's day field, changing the month and year if necessary}
procedure next_day( var dt : date_t );

    {Nested Function: Returns true if the year is a leap year}
    function leap_year( year : integer ) : boolean;
    begin
        {Defaults to false}
        leap_year := false;

        {If the year is divisible by 4, then set it to true}
        if year mod 4 = 0 then
            leap_year := true;

        {If the year is divisible by 100, then set to false}
        if year mod 100 = 0 then
            leap_year := false;

        {If the year is then also divisible by 400, set to true}
        if year mod 400 = 0 then
            leap_year := true;

        {Goes through all three if statements, if passes third, passes 2 before}
        {If passes second, passes 1 before, always returns correct boolean}
    end;

    {Nested Function: Returns the last day of a givn month}
    function month_length( month : month_range; leap : boolean ) : day_range;
    begin
        {If the month is in the set below, the length of the month is 31}
        if month in [ 1, 3, 5, 7, 8, 10, 12 ] then
            month_length := 31;

        if month in [ 4, 6, 9, 11 ] then
            month_length := 30;

        {If the month is February and it is a leap year, the length is 29}
        if ( month = 2 ) and leap then
            month_length := 29;

        {If the month is February and it it not a leap year, the length is 28}
        if ( month = 2 ) and not leap then
            month_length := 28;
    end;

{Begin next_day Method}
begin
{Check if the day is the last day of the given month}
if ( dt.day = month_length( dt.month, leap_year( dt.year ) ) ) then
    {Last Day of Month}
    begin
    {If so, set day to 1}
    dt.day := 1;

    {If it is the last day of December, set month to January and increment year}
    if dt.month = 12 then
        begin
        dt.month := 1;
        dt.year := dt.year + 1;
        end

    {If it is any other month, increment month}
    else
        dt.month := dt.month + 1;
    end

{If it is not the last day of the month, increment the day}
else
    dt.day := dt.day + 1;
end;

{********************************Main Function*********************************}
{Variables for main, three dates and a string to print out}
var
    d1, d2, d3 : date_t;
    format_str : string;

begin
    {First Initializations}
    init_date1( d1 );
    init_date( d2, 30, 12, 1999 );
    init_date( d3, 1, 1, 2000 );

    writeln( );
    {Formatting all of the dates to format_str and printing them out}
    format_date( d1, format_str );
    writeln( 'd1: ' + format_str );
    format_date( d2, format_str );
    writeln( 'd2: ' + format_str );
    format_date( d3, format_str );
    writeln( 'd3: ' + format_str );

    writeln( );
    {Comparing the dates}
    writeln( 'd1 < d2? ', date_less_than( d1, d2 ) );
    writeln( 'd2 < d3? ',  date_less_than( d2, d3 ) );

    writeln( );
    {Incrementing d2 and then comparing the dates}
    next_day( d2 );
    format_date( d2, format_str );
    writeln( 'next day d2: ' + format_str );
    writeln( 'd2 < d3? ', date_less_than( d2, d3 ) );
    writeln( 'd2 = d3? ', date_equal( d1, d2 ) );
    writeln( 'd2 > d3? ', date_less_than( d3, d2 ) );

    writeln( );
    {Incrementing d2 again and comparing the dates (should equal d3)}
    next_day( d2 );
    format_date( d2, format_str );
    writeln( 'next day d2: ' + format_str );
    writeln( 'd2 = d3? ', date_equal( d2, d3 ) );

    writeln( );
    {Checking to see if next_day correctly calculates leap_year for 1529}
    init_date( d1, 28, 2, 1529 );
    format_date( d1, format_str );
    writeln( 'initialized d1 to ' + format_str );
    next_day( d1 );
    format_date( d1, format_str );
    writeln( 'next day d1: ' + format_str );

    writeln( );
    {Checking to see if next_day correctly calculates leap_year for 1460}
    init_date( d1, 28, 2, 1460 );
    format_date( d1, format_str );
    writeln( 'initialized d1 to ' + format_str );
    next_day( d1 );
    format_date( d1, format_str );
    writeln( 'next day d1: ' + format_str );

    writeln( );
    {Checking to see if next_day correctly calculates leap_year for 1700}
    init_date( d1, 28, 2, 1700 );
    format_date( d1, format_str );
    writeln( 'initialized d1 to ' + format_str );
    next_day( d1 );
    format_date( d1, format_str );
    writeln( 'next day d1: ' + format_str );

    writeln( );
    {Checking to see if next_day correctly calculates leap_year for 1600}
    init_date( d1, 28, 2, 1600 );
    format_date( d1, format_str );
    writeln( 'initialized d1 to ' + format_str );
    next_day( d1 );
    format_date( d1, format_str );
    writeln( 'next day d1: ' + format_str );

    writeln( );
end.
