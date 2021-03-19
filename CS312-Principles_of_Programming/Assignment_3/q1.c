#include <stdio.h>

int a = 2;
int f(int y){
  static int z = -2;
  printf("A: a is %d , y is %d , z is %d ", a,y,z);
  printf("\n");
  if (!y){
    y++;
    a = f(y + 1);
  }
  z += 1;
  printf("B: a is %d , y is %d , z is %d", a,y,z);
  printf("\n");
  return z;
}

void main(){
  int x = 5;
  int y = 7;
  int z = 0;
  printf("C: a is %d , x is %d , y is %d , z is %d", a,x,y,z);
  printf("\n");
  x = f(z);
  printf("D: a is %d , x is %d , y is %d , z is %d", a,x,y,z);
  printf("\n");
  y = f(a);
  printf("E: a is %d , x is %d , y is %d , z is %d", a,x,y,z);
  printf("\n");
}
