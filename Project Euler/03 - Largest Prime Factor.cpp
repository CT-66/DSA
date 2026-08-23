#include <cmath>
#include <iostream>
#include <vector>
using namespace std;

// brute force
bool isPrime(int num) {
  bool is_prime = true;
  if (num < 2) {
    is_prime = false;
  } else if (num == 2) {
    is_prime = true;
  }
  for (int i = 2; i <= sqrt(num); i++) {

    if (num % i == 0) {
      is_prime = false;
    }
  }

  return is_prime;
}

int main() {
  // int a = 13195;
  long long a = 600851475143;
  vector<int> facs;
  for (int i = 1; i < sqrt(a); i++) {
    if (a % i == 0) {
      facs.push_back(i);
    }
  }
  for (int i = 0; i < facs.size(); i++) {
    // cout << facs[i] << endl;
    if (isPrime(facs[i])) {
      cout << facs[i] << endl;
    }
  }
}
