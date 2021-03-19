#include <iostream>
#include <vector>
#include <string>
#include <cmath>

#include "HashLin.hpp"
#include "HashPerfect.hpp"

main()
{
  //**********************************HashLin***********************************
  std::vector< std::string > string_storage;
  std::string input;
  bool prime = false;
  int size;

  std::cout << "\nPlease enter strings to insert "
            << "(one per line; end lists with '!'):\n\n";

  //Reading in strings
  while ( std::cin >> input )
  {
    //Stops reading in if "!" is detected
    if ( input == "!" )
      break;

    string_storage.push_back( input );
  }

  //Finding prime number greater or equal to string_storage size
  size = string_storage.size();

  if ( ( size == 1 ) || ( size == 2 ) || ( size == 3 ) )
    prime = true;

  while ( prime == false )
  {
    for ( int i = 2; i <= ceil( sqrt( size ) ); ++i )//**
    {
      if ( (size % i) == 0 )
        break;//A factor is found, break and check next integer

      else if ( i == ( ceil( sqrt( size ) ) ) ) //Scanned all possible factors
        prime = true; //Number is found to be prime
    }

    //Number isn't prime, check next one
    if ( prime == false )
      ++size;//
  }

  //Initializing HashLin
  HashLin HashLinearClass(size);

  //Inserting input strings
  for ( int c = 0; c < string_storage.size(); ++c )
    HashLinearClass.insert( string_storage[ c ] );

  std::cout << "\n\n\nHash Table with Linear Probing (size = "
            << size << "):" << "\n\n";

  HashLinearClass.print();

  //********************************HashPerfect*********************************
  HashPerfect HashPerfectClass;
  HashPerfectClass.insert( string_storage );

  std::cout <<"\n\n\nPerfect Hash Table:\n";

  HashPerfectClass.print();
}
