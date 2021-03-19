#include <stdio.h>
double q( int *a, int b, int *c ){
    double q;
    *c = *a + b + *c;
    *a = 2 * (*c);
    b = b * 4;
    q = (double)*a / (double)b;
    printf("result: %d, %d, %d, %f\n",a, b, c, q);
    return q;
}

int main(){
    int x, y, z;
    double i;
    printf("Enter three integers: ");
    x = 3;
    y = 4;
    z = 5;
    i = q(&x, y, &z);
    printf("result: %d, %d, %d, %f",x, y, z, i);
}
