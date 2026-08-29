class Solution {
  public:
    // not actual solution
    int peakIndexInMountainArray(vector<int> &arr) {
        int maxV = *max_element(arr.begin(), arr.end());
        for (int i = 0; i < arr.size(); i++) {
            if (arr[i] == maxV) {
                return i;
            }
        }
        return 0;
    }
};
