#include <stdio.h>

// create an array and fill it with first 20 multiples of 3
// add up all of the odd values in the array


void main ()

{
   int arr[20];
   int i;
   int sum;


   // fill array with multiples of 3
   i = 0;
   while (i < 20) {

      arr[i] = i * 3;
      i++;
   }

   // add up only odd entries
   sum = 0;
   i = 0;
   while (i < 20) {

      if (arr[i] & 1)

         sum += arr[i];

      i++;
   }

   printf ("sum: %d\n", sum);
}
