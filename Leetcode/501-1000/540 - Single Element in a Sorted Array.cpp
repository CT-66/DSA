class Solution {
  public:
    int singleNonDuplicate(vector<int> &nums) {
        //     int l = 0;
        //     int r = nums.size()-1;

        //     while (l!=r) {
        //         int m = l + (r-l) / 2;

        //         if (nums[l] != nums[r]) {
        //             return nums[l];
        //         }
        //         else {
        //             l++;
        //             // r--;
        //         }
        //     }
        //     return 0;
        // }
        int l = 0;
        for (int r = 1; r < nums.size(); r += 2) {
            if (nums[l] != nums[r]) {
                return nums[l];
            }
            l += 2;
        }
        return nums.back();
    }
};
