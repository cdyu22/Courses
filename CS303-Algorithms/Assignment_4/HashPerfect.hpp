#ifndef HASHPERFECT_HPP
#define HASHPERFECT_HPP

#include <iostream>
#include <string>
#include <vector>
#include "HashLin.hpp"

class HashPerfect{

  private:
    unsigned size;
    HashLin * hashPerfectTable[ 10 ];
    void init( void );
    unsigned long hashPerfect( const std::string );

  public:
    HashPerfect ( void );
    ~HashPerfect ( void );
    void print( void );
    bool insert( const std::vector< std::string > );

};
#endif
