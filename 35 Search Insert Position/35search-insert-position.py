class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # for i in range(len(nums)):
        #     res = 0
        #     if nums[i] == target:
        #         # res = nums.index(i)
        #         res = i
            
        #     return res
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)