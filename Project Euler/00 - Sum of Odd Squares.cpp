#include <iostream>
using namespace std;

// Brute force

/*
int main() {
    long long count = 0;
    for (long long i=0; i <= 972000; i++) {
        if (i % 2 != 0) {
            count += 1LL * i*i;
        }
    }
    cout << count;
}
*/

// Optimal, mathy solution

int main() {
    long long n = 972000;

    // Sum of all squares: 1^2 + 2^2 + ... + n^2
    long long allSquares = (n / 6) * (n + 1) * (2 * n + 1);

    // Sum of even squares:
    // 2^2 + 4^2 + ... + (972000)^2
    long long m = n / 2;
    long long evenSquares = 4 * (m / 6) * (m + 1) * (2 * m + 1);

    long long answer = allSquares - evenSquares;

    cout << answer << endl;

    return 0;
}
