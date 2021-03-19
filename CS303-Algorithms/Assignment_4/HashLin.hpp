#ifndef HASHLIN_HPP
#define HASHLIN_HPP

#include <iostream>
#include <string>
#include <vector>

class HashLin{

  private:
    std::vector<std::string> hashTable;
    unsigned long hashlinear( const std::string );
    void init( void );

  public:
    HashLin ( int );
    bool insert( const std::string );
    void print( int indent = 0 );

};
#endif
