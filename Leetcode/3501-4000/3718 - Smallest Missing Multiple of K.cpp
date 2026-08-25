
/*
#include <algorithm>
#include <bits/stdc++.h>
#include <vector>

using namespace std;
int main() {
    vector<int> nums = {76, 12, 14};
    vector<int> neww = {};
    int k = 6;

    if (nums.size() < 2) {
        return k;
    }

    sort(nums.begin(), nums.end());
    for (int i = 0; i <= nums.size() - 1; i++) {
        // cout << nums[i] << endl;
        if (nums[i] % k == 0) {
            neww.push_back(nums[i]);
        }
    }
    // cout << neww[0];
    int maxE = neww.back();
    int res;
    for (int i = k; i <= maxE + k; i += k) {
        // cout << i << endl;
        // check if i is NOT in neww
        if (find(neww.begin(), neww.end(), i) == neww.end()) {
            // cout << i << endl;
            res = i;
            break;
        }
    }
    cout << res;
    return res;
}
*/

class Solution {
  public:
    int missingMultiple(vector<int> &nums, int k) {
        unordered_set<int> s(nums.begin(), nums.end());

        for (int x = k;;
             x += k) { // ;; -> no condition (infinite), basically a while loop
            if (s.find(x) == s.end()) {
                return x;
            }
        }
    }
};
