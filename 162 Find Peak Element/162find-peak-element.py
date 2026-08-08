class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
       l = 0
       r = len(nums) - 1

       while l <= r:
        m = (l + r) // 2

        # check if left neighbor is greater
        if m > 0 and nums[m] < nums[m-1]:
            r = m - 1
        # check if right neighbor is greater
        elif m < len(nums) - 1 and nums[m] < nums[m+1]:
            l = m + 1
        else:
            return m