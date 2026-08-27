/*
class Solution {
public:
    string removeOuterParentheses(string S) {
        string res;
        int opened = 0;
        for (char c : S) {
            if (c == '(' && opened++ > 0) res += c;
            if (c == ')' && opened-- > 1) res += c;
        }
        return res;
    }
};
*/
// more verbose
class Solution {
  public:
    string removeOuterParentheses(string S) {
        string res;
        int depth = 0;

        for (char c : S) {
            if (c == '(') {
                if (depth > 0)
                    res += c;

                depth++;
            } else {
                depth--;

                if (depth > 0)
                    res += c;
            }
        }

        return res;
    }
};
