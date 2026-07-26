class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse=True)
        a = nums[0] * nums[1] * nums[2]
        b = nums[-1] * nums[-2] * nums[0] 
        if a>b: 
            return a
        else:
            return b