class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:

        # not optimal solution, should probably use sets

        res = 0
        i = 0

        # print(len(nums))
        # print(len(set(nums)))

        # if len(nums) == 1:
        #     return 1
        # if len(nums) == len(set(nums)):
        #     return len(nums)
        # for j in range(1, len(nums)):
        #     if nums[i] == nums[j]:
        #         res+=1
        #     i+=1
        # return res
        for i in range(len(nums)):
            if nums[i] in nums[:i]:
                continue
            f = i
            l = i

            for j in range(i + 1, len(nums)):
                if nums[j] == nums[i]:
                    l = j
            found = True

            for k in range(f, l + 1):
                if nums[k] != nums[i]:
                    found = False
                    break
            if found:
                res += 1
        return res
