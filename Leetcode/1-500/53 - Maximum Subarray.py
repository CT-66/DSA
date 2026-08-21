class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # left = 0
        # right = 1
        # res = 0
        # if len(nums) == 0:
        #     return 0
        # while right < len(nums):
        #     sum = nums[left] + nums[right]
        #     res = max(res, sum)
        #     right +=1 
        #     if res < sum:
        #         left = right
        # return res
        maxSub = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub
