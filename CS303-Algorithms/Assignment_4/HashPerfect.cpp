#include <iostream>
#include <string>
#include <vector>
#include "HashLin.hpp"
#include "HashPerfect.hpp"

//PUBLIC
HashPerfect::HashPerfect()
{
  size = 10;
  init();
}

//******************************************************************************

//PRIVATE
void HashPerfect::init()
{
  for ( int cell_ptr = 0; cell_ptr < size; ++cell_ptr )
    hashPerfectTable[ cell_ptr ] = NULL;
}

//******************************************************************************

//PUBLIC
bool HashPerfect::insert( const std::vector< std::string > passed_in )
{
  bool check = true;

  //Will initialize all 10 values to zero.
  std::vector<int> sizeKeeper( size );

  //Filling up sizeKeeper to track amount of hashes to each HashLin
  for ( int fill = 0; fill < passed_in.size(); ++fill )
  {
    unsigned long foo = hashPerfect( passed_in[ fill ] );
    sizeKeeper[ foo ] = sizeKeeper[ foo ] + 1;
  }

  //Creation of the HashLin for each non-zero cell
  for ( int x = 0; x < size; ++x )
    if ( sizeKeeper[ x ] != 0 )
      hashPerfectTable[ x ] = new HashLin( sizeKeeper[ x ] * sizeKeeper[ x ] );

  //Hashing the values and inserting them into the table.
  for ( int k = 0; k < passed_in.size(); ++k )
  {
    unsigned long location = hashPerfect( passed_in[ k ] );
    if (hashPerfectTable[ location ]->insert( passed_in[ k ] ) == false)
    {
      std::cout << "Could not insert: " << passed_in[ k ] << "\n";
      check = false;
    }
  }

  return check;
}

//******************************************************************************

//PRIVATE
unsigned long HashPerfect::hashPerfect( const std::string find_val )
{
  unsigned long hashVal = 0;
  for ( int k = 0; k < find_val.size(); ++k )
  {
    unsigned char w = find_val[ k ];
    hashVal = ( 37 * hashVal + w ) % size;
  }
  return hashVal;
}

//******************************************************************************

//PUBLIC
void HashPerfect::print()
{
  for( int i = 0; i < size; ++i )
  {
    std::cout << i << ": - - > " << "\n";
    if ( hashPerfectTable[ i ] != NULL ) //Doesn't print if still NULL
    {
      hashPerfectTable[ i ]->print(2);
    }
  }
}

//******************************************************************************

//PUBLIC
HashPerfect::~HashPerfect( void )
{
  for ( int destroy = 0; destroy < size; ++destroy )
    if ( hashPerfectTable[ destroy ] != NULL )
      delete hashPerfectTable[ destroy ];
}
