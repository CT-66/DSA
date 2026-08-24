class Solution {
  public:
    double myPow(double x, int n) {
        long double res = 1;
        for (long double i = 1; i <= abs(n); i++) {
            res *= x;
        }
        if (n < 0) {
            return (1 / res);
        }
        return res;
    }
};
