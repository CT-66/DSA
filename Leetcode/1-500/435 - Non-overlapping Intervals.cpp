
class Solution {
  public:
    int eraseOverlapIntervals(vector<vector<int>> &intervals) {
        int n = intervals.size();
        sort(intervals.begin(), intervals.end(),
             [](const vector<int> &x, const vector<int> &y) {
                 return x[1] < y[1];
             });
        int c = 1;
        int k = 0;
        for (int j = 1; j < n; j++) {
            if (intervals[j][0] >= intervals[k][1]) {
                c++;
                k = j;
            }
        }
        return n - c;
    }
};
