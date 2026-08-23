class Solution {
  public:
    bool isPalindrome(int x) {
        string y = to_string(x);
        // using string reverse function
        string z = y;

        reverse(z.begin(), z.end());

        if (y == z) {
            return true;
        } else {
            return false;
        }
    }

    // manual two pointer approach
    /*
    int l = 0, r = y.size() - 1;
    while (l <= r) {
        if (y[l] != y[r]) {
            return false;
        }
        l++;
        r--;
    }
    return true;
    */
};
