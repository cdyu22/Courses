#include <stdio.h>

int a, b, c;

void main(){
  a = 0;
  b = 4;
  c = a != 0 && b/a ? b++ * ++a : --b * 3;
  printf("a is: %d, b is: %d, and c is: %d", a, b, c);
  a = 7;
  b = 4;
  c = a / b;
  printf("c is: %d", c);
}
