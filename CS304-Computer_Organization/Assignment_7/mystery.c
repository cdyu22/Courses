#include <stdio.h>

void mystery (int *a, int *b){
    int i, flag;

    while (*a <= *b){
        flag = 0;

        for (i = 2; i * i <= *a; ++i){
            if (*a % i == 0){
                flag = 1;
                break;
            }
        }

        if (flag == 0)
            printf("%d ", *a);

        ++*a;
    }
}

int main(){
  int i, sum = 0;
  for ( i = 1; i < 65; i+=2)
      sum += i;
  printf("%d",sum);
}
