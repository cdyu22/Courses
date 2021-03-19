#include <stdio.h>

void assign (char *n) {
    char answer[1];
    printf ("enter Y or N: ");
    scanf ("%c", answer);
    if (*answer == 'Y')
        *n = *answer;
    else
        *n = 'N';
}

int main()
{
    char x[2];
    assign (x);
}
