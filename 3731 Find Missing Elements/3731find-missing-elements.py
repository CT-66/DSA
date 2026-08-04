class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        low = nums[0]
        high = nums[-1]+1
        full = []
        missing = []
        if len(nums) == 0:
            return []
        for i in range(low, high):
            full.append(i)
        print(nums)
        print(full)
        
        for i in full:
            if i not in nums:
                missing.append(i)

        return missing
        
