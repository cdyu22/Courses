#include <stdio.h>

int x;

void div_x(int div){
  x = x / div;
}

void print_x(){
  printf("x is: %d", x);
  printf("\n");
}

void third(){
  int x = 17;
  div_x(4);
  print_x();
}

void first(){
  x = 47;
  print_x();
  div_x(2);
}

void second(){
  int x = 39;
  div_x(3);
  print_x();
  third();
  print_x();
}

void main(){
  first();
  print_x();
  second();
  print_x();
}
