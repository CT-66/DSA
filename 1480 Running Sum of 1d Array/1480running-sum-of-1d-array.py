class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            a = nums[:]
            del a[i+1:]
            res.append(sum(a))
        return res