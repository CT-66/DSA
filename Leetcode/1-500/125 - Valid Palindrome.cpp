#include <cctype>
#include <string>
using namespace std;

// inefficient solution
/*
class Solution {
public:
  bool isPalindrome(string s) {
    string n = "";
    for (char i : s) {
      if (std::isalnum(i)) {
        //   cout << i;
        n += i;
      }
    }

    for (char &c : n) {
      c = std::tolower(c);
    }

    int l = 0;
    int r = n.size() - 1;

    while (l <= r) {
      if (n[l] != n[r]) {
        return false;
      }
      l++;
      r--;
    }
    return true;
  }
};
*/

// without creating new string
class Solution {
public:
  bool isPalindrome(string s) {
    int l = 0;
    int r = s.size() - 1;

    while (l < r) {
      while (l < r && !isalnum(s[l])) {
        l++;
      }

      while (l < r && !isalnum(s[r])) {
        r--;
      }

      if (tolower(s[l]) != tolower(s[r])) {
        return false;
      }

      l++;
      r--;
    }

    return true;
  }
};
