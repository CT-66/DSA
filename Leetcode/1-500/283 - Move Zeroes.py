class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l +=1
        return nums

        #####

        # brute force
        """
        # if len(nums) == 1:
        #     return nums
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if i == 0 and j != 0:
        #             temp = nums[j]
        #             nums[j] = nums[i]
        #             nums[i] = temp
        # return nums
        num0 = 0
        numss = []
        # nums.clear()
        for i in nums:
            if i != 0:
                numss.append(i)
            if i == 0:
                num0 += 1

        for _ in range(num0):
            numss.append(0)
        nums[:] = numss
        return nums
        """
