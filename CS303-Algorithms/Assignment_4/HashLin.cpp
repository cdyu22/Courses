#include <iostream>
#include <string>
#include <vector>
#include "HashLin.hpp"

//PUBLIC
HashLin::HashLin ( int size )
{
  hashTable.resize( size );
  init();
}

//******************************************************************************

//PRIVATE
void HashLin::init( void )
{
  for ( int value = 0; value < hashTable.size(); ++value )
    hashTable[ value ] = "";
}

//******************************************************************************

//PUBLIC
bool HashLin::insert( const std::string insertion )
{
  bool completion = true;
  int ins_point = hashlinear( insertion );

  //Won't insert in occupied cell, starts probe
  if ( hashTable[ ins_point ] != "" )
    for ( int i = 1; i < hashTable.size(); ++i )
    {
      if ( hashTable[ ( ins_point + i ) % hashTable.size() ] == "")
      {
        //Found insertion point, break
        ins_point = ( ins_point + i ) % hashTable.size();
        break;
      }

      //Checked all spaces, open one found, insertion failed
      if ( i == ( hashTable.size() - 1 ))
        completion = false;
    }

  //Inserts value; but only if open space found
  if ( completion == true )
    hashTable[ ins_point ] = insertion;

  if ( completion == false )
    std::cout << "Could not insert: " << insertion << "\n";

  return completion;
}

//******************************************************************************

//PRIVATE
//This will find the insertion point for the input before probing.
unsigned long HashLin::hashlinear( const std::string str )
{
  unsigned long hashVal = 0;
  for ( int k = 0; k < str.size(); ++k )
  {
    unsigned char value = str[ k ];
    hashVal = ( 37 * hashVal + value ) % hashTable.size();
  }
  return hashVal;
}

//******************************************************************************

//PUBLIC
void HashLin::print( int indent )
{
  //To create indentation
  std::string place = "  ";
  for ( int space = 0; space < indent ; ++space )
    place = place + place;

  for ( int n = 0; n < hashTable.size(); n++ )
    std::cout << place << n << ": " << hashTable[ n ] << "\n";
}
