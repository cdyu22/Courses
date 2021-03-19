#include <iostream>
double q( int a, int b, int c ){
    double q;
    c = a + b + c;
    a = 2 * c;
    b = b * 4;
    q = (double)a / (double)b;
    std::cout << a <<" " << b << " "<< c <<" " << q << "\n";
    return q;
}

int main(){
    int x, y, z;
    double i;
    printf("Enter three integers: ");
    x = 3;
    y = 4;
    z = 5;
    i = q(x, y, z);
    std::cout << "result: " << x <<" " << y << " " << z <<" " << i;
}
