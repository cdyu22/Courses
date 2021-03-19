//gcc 7.4.0

#include  <stdio.h>

void main(void)
{

    // int a[3] = {7, 11,13};
    // int *p = &a[2];
    // int *q = a;
    //
    // printf("%d %d %d\n",&p, p, *p);
    // printf("%d %d %d\n",&q, q, *q);
    //
    //
    //
    // p = &a[1];
    //
    // printf("%d %d %d\n",&p, p, *p);
    // printf("%d %d %d\n",&q, q, *q);
    //
    // *p -= *q;
    // q++;
    // q += 1;
    // *q -= *a;
    // p[-1]--;
    //
    // printf("%d %d %d\n",&p, p, *p);
    // printf("%d %d %d\n",&q, q, *q);

    // float x = -1;
    // printf("%f",x);

    //gcc 7.4.0



    int a[] = {1,6};
    int b = 10;
    int c = 7;

    int *p = a;
    int *q = &b;

    printf("%d %d\n", &a, a);
    printf("%d %d %d\n", &p, p, *p);
    printf("%d %d %d\n", &q, q, *q);

    p = q--;
    *q = 3;

    printf("%d %d %d %d",a[0], a[1], b, c);
    p[1] = 5;

    printf("%d %d %d\n", &p, p, *p);
    printf("%d %d %d\n", &q, q, *q);
}
