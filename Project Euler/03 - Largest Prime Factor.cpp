#include <cmath>
#include <iostream>
#include <vector>
using namespace std;

// test
int main() {
  int a = 13195;
  //   cout << sqrt(a);
  vector<int> facs;
  for (int i = 1; i < sqrt(a); i++) {
    if (a % i == 0) {
      facs.push_back(i);
    }
  }
  for (int i = 0; i < facs.size(); i++) {
    cout << facs[i] << endl;
  }
}
