class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1 # not index 0 because that's guarenteed  to be unique

        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]: # check with prev value
                nums[l] = nums[r]
                l+=1
        return l
