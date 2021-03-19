#include <iostream>
#include <time.h>
#include <iomanip>

//Prototypes
double maxSubSum1( int array[] ,  int length );
double maxSubSum2( int array[] ,  int length );
double maxSubSum4( int array[] ,  int length );
double maxSubSum3( int array[] ,  int length );
int max3( int a, int b, int c );
int maxSumRec( int array[], int length, int left, int right );

int main()
{
  std::cout << "Please enter sequence integers: \n\n";
  long index = 0;
  int MaxSumCalc[ 2500 ];
  double runtime_1, runtime_2, runtime_3, runtime_4;


  std::cout << "CLOCKS_PER_SEC is: " << CLOCKS_PER_SEC << "\n";
  std::cout << "Index is: " << index << "\n"<<"It's contents are: " << "[";
  for ( int i = 0; i < (index+1); i++)
  {
    std::cout << MaxSumCalc[i] << ' ';
  }
  std::cout << "]" << "\n" ;
  //Declaration of variables

  //Reading in integers to array
  while ( std::cin >> MaxSumCalc[ index ] )
    index++;

  //Running algorithms and storing their runtimes
  runtime_1 = maxSubSum1( MaxSumCalc, index );
  runtime_2 = maxSubSum2( MaxSumCalc, index );
  runtime_3 = maxSubSum3( MaxSumCalc, index );
  runtime_4 = maxSubSum4( MaxSumCalc, index );

  //Displaying final results of runtime
  std::cout << "Final Results\n" << std::setprecision(0) <<  std::fixed
            << "  Algorithm 1 O(n^3)      : " << runtime_1 << " ms\n"
            << "  Algorithm 2 O(n^2)      : " << runtime_2 << " ms\n"
            << "  Algorithm 3 O(n lg n)   : " << runtime_3 << " ms\n"
            << "  Algorithm 4 O(n)        : " << runtime_4 << " ms\n";

  return 0;
}

//******************************************************************************

double maxSubSum1( int array[], int length )
{
  //Declaration of Variables
  int maxSum = 0;
  double time_recorded_1;
  time_t time_recorded_1Start, time_recorded_1End;

  time_recorded_1Start = clock(); //Clock starttime

  //Algorithm_1
  for( int i = 0; i < length; ++i )
    for( int j = i; j < length; ++j )
    {
      int thisSum = 0;

      for( int k = i; k <= j; ++k )
        thisSum += array[ k ];

      if( thisSum > maxSum )
        maxSum = thisSum;
    }

  //Clock endtime and runtime computation
  time_recorded_1End = clock();
  time_recorded_1 = double ( time_recorded_1End - time_recorded_1Start )
                           / CLOCKS_PER_SEC * 1000000;

  //Outputting the calculated maxSum
  std::cout << "Recorded_1: " << time_recorded_1 << "\n";
  std::cout << "Alg_1 Beginning: " << time_recorded_1Start << "\n";
  std::cout << "Alg_1 Ending: " << time_recorded_1End << "\n\n";
  std::cout << "Algorithm 1: " << maxSum << "\n";

  return time_recorded_1;
}

//******************************************************************************

double maxSubSum2( int array[], int length )
{
  //Declaration of variables
  int maxSum = 0;
  double time_recorded_2;
  time_t time_recorded_2Start, time_recorded_2End;

  time_recorded_2Start = clock();//Clock starttime

  //Algorithm_2
  for( int i = 0; i < length; ++i )
  {
    int thisSum = 0;
    for( int j = i; j < length; ++j )
    {
      thisSum += array[ j ];

      if( thisSum > maxSum )
        maxSum = thisSum;
    }
  }

  //Clock endtime and runtime computation
  time_recorded_2End = clock();
  time_recorded_2 = double ( time_recorded_2End - time_recorded_2Start )
                           / CLOCKS_PER_SEC * 1000000;

  //Outputting the calculated maxSum
  std::cout << "Recorded_2: " << time_recorded_2 << "\n";
  std::cout << "Alg_2 Beginning: " << time_recorded_2Start << "\n";
  std::cout << "Alg_2 Ending: " << time_recorded_2End << "\n\n";
  std::cout << "Algorithm 2: "<< maxSum << "\n";

  return time_recorded_2;
}

//******************************************************************************
double maxSubSum3( int array[], int length )
{
  //Declaration of variables
  int maxSum = 0;
  double time_recorded_3;
  time_t time_recorded_3Start, time_recorded_3End;

  time_recorded_3Start = clock();//Clock starttime

  //Call to recursive function, declaration of maxSum, which will be returned
  maxSum = maxSumRec( array, length, 0, length - 1 );

  //Clock endtime and runtime computation
  time_recorded_3End = clock();
  time_recorded_3 = double ( time_recorded_3End - time_recorded_3Start )
                           / CLOCKS_PER_SEC * 1000000;

  //Outputting the calculated maxSum
  std::cout << "Recorded_3: " << time_recorded_3 << "\n";
  std::cout << "Alg_3 Beginning: " << time_recorded_3Start << "\n";
  std::cout << "Alg_3 Ending: " << time_recorded_3End << "\n\n";
  std::cout << "Algorithm 3: " << maxSum << "\n";

  return time_recorded_3;
}

int maxSumRec( int array[], int length, int left, int right )
{
  if( left == right )
    if( array[ left ] > 0 )
      return array[ left ];
    else
      return 0;

  int center = ( left + right ) / 2;
  int maxLeftSum = maxSumRec( array, length,  left, center );
  int maxRightSum = maxSumRec( array, length, center + 1, right );

  int maxLeftBorderSum = 0, leftBorderSum = 0;
  for( int i = center; i >= left; --i)
  {
    leftBorderSum += array[ i ];
    if( leftBorderSum > maxLeftBorderSum )
      maxLeftBorderSum = leftBorderSum;
  }
  int maxRightBorderSum = 0, rightBorderSum = 0;
  for( int j = center + 1; j <= right; ++j)
  {
    rightBorderSum += array[ j ];
    if( rightBorderSum > maxRightBorderSum )
      maxRightBorderSum = rightBorderSum;
  }

  return max3( maxLeftSum, maxRightSum, maxLeftBorderSum + maxRightBorderSum );
}

//Function to return the maximum of the 3 variables inputted
int max3( int a, int b, int c)
{
  if( b > a )
    a = b;
  if( c > a )
    a = c;
  return a;
}
//******************************************************************************
double maxSubSum4( int array[], int length )
{
  //Declaration of variables
  int maxSum = 0, thisSum = 0;
  double time_recorded_4;
  time_t time_recorded_4Start, time_recorded_4End;

  time_recorded_4Start = clock();//Clock starttime

  for( int j = 0; j < length; ++j )
  {
    thisSum += array[ j ];

    if( thisSum > maxSum )
      maxSum = thisSum;
    else if( thisSum < 0 )
      thisSum = 0;
  }

  //Clock endtime and runtime computation
  time_recorded_4End = clock();
  time_recorded_4 = double ( time_recorded_4End - time_recorded_4Start )
                           / CLOCKS_PER_SEC * 1000000;

  //Outputting the calculated maxSum
  std::cout << "Algorithm 4: " << maxSum << "\n";

  std::cout << "Recorded_4: " << time_recorded_4 << "\n";
  std::cout << "Alg_4 Beginning: " << time_recorded_4Start << "\n";
  std::cout << "Alg_4 Ending: " << time_recorded_4End << "\n\n";
  return time_recorded_4;
}
