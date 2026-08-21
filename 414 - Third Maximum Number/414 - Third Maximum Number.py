class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums=sorted(set(nums), reverse=True)
        # print(len(nums))
        if (len(nums) >= 3):
            print(nums)
            return nums[2]
        else:
            return max(nums)
