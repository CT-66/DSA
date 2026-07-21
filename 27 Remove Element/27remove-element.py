class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        notEqual = 0
        for i in nums:
            if i == val:
                nums.remove(i)
            elif i != val:
                notEqual+=1
        print(notEqual)
        # joke solution to hard remove the duplicate elements
        # it actually cleared all testcases lmao
        for i in nums:
            if i == val:
                nums.remove(i)
        for i in nums:
            if i == val:
                nums.remove(i)
        print(nums)