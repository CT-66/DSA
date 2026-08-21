#include <iostream>

using namespace std;

// Brute force
/*
int main() {
    int c = 0;
    for (int i = 0; i < 1000; i++) {
        if (i % 3 == 0 || i % 5 == 0) {
            c += i;
        }
    }
    cout << c;
}
*/

// Optimal
int main() {
    // Number of multiples of 3, 5, and 15 below 1000
    // n * (1 + 2 + ... + k) = n * k * (k + 1) / 2
    int sum3 = 3 * (999 / 3) * ((999 / 3) + 1) / 2;
    int sum5 = 5 * (999 / 5) * ((999 / 5) + 1) / 2;
    int sum15 = 15 * (999 / 15) * ((999 / 15) + 1) / 2;

    cout << (sum3 + sum5) - sum15;
}
