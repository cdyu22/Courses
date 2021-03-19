#include <iostream>

void swap(int &a,int &b)
{
  int c = a;
  a = b;
  b = c;
  std::cout << "Baz is: " << a << "\nFoo is: " << b << "\n";
}

int main()
{
  /*

baz = 10;
foo = *baz;
std::cout << baz << " Hello " << foo;
*/
int baz = 0;
int foo = 1;
swap(baz,foo);

std::cout << "Baz is: " << baz << " Foo is: "<< foo;
return 0;

}
