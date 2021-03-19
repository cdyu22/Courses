#include <stdio.h>

int a = 5;
int Recursive (int n, int sum) {
  printf ("%d\n", n);
  if (n == 0) return 3;
  if (n == 1) return 1;

  printf("So Sum is: %d\n",sum);
  if (n % 2)
    return sum + Recursive (n - 1, sum);
  else
      return sum + 2*Recursive (n - 2, sum);

}

void main() {
  int sum = 0;
  printf ("%d\n", Recursive (a, sum));
}
