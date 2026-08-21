
#include <iostream>
using namespace std;

// regular fibonacci
/*
int main() {
  int a = 0;
  int b = 1;
  cout << a << endl << b << endl;
  for (int i = 0; i <= 11; i++) {
    int c = a + b;
    a = b;
    b = c;
    cout << c << endl;
  }
}
*/

// brute force
/*
int main() {
  long long a = 1;
  long long b = 2;
  long long sum = 0;
  while (b < 4000000) {
    if (b % 2 == 0) {
      sum += b;
    }
    long long c = a + b;
    a = b;
    b = c;
  }
  cout << sum;
}
*/

// math approach: every third number in fib sequence is even
int main() {
  long long a = 2;
  long long b = 8;
  long long sum = 0;

  while (a <= 4000000) {
    sum += a;

    long long next = 4 * b + a;
    a = b;
    b = next;
  }

  cout << sum;

  return 0;
}
