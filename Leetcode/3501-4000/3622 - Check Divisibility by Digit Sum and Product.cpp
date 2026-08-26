class Solution {
  public:
    bool checkDivisibility(int n) {
        int dSum = 0;
        int dProd = 1;
        int nn = n;

        while (n > 0) {
            dSum += (n % 10);
            dProd *= (n % 10);
            n /= 10;
        }

        if (nn % (dSum + dProd) == 0) {
            return true;
        } else {
            return false;
        }
    }
};
