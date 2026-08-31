class Solution {
  public:
    int largestPerimeter(vector<int> &nums) {
        if (nums.size() < 3) {
            return 0;
        }

        sort(nums.begin(), nums.end(), std::greater<>());

        /*
        int s1 = nums[0];
        int s2 = nums[1];
        int s3 = nums[2];
        if (s1 + s2 > s3 && s1 + s3 > s2 && s2 + s3 > s1) {
            return s1 + s2 + s3;
        }
        return 0;
        }
        */

        // brute force with 3 loops (O(n^3))
        /*
            for (int i = 0; i < nums.size(); i++) {
            for (int j = i + 1; j < nums.size(); j++) {
                for (int k = j + 1; k < nums.size(); k++) {
                    if (nums[i] + nums[j] > nums[k] && nums[i] + nums[k] >
        nums[j] && nums[j] + nums[k] > nums[i]) { return
        nums[i]+nums[j]+nums[k];
                }
            }
        }
        */

        // better solution with just one loop (O(n logn))
        for (int i = 0; i + 2 < nums.size(); i++) {
            if (nums[i + 1] + nums[i + 2] > nums[i]) {
                return nums[i] + nums[i + 1] + nums[i + 2];
            }
        }

        return 0;
    }
};
