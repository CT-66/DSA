class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # for i in range(len(nums)):
            # for j in range(len(nums)):
                # print(nums[i])
                # print(nums[j])
        # print(list(set(nums)))
        # nums = sorted(nums)
        # new = sorted(set(nums))

        # if list(new) == nums:
        #     return False
        # else:
        #     return True

        """
        new = set(nums)

        if len(new) == len(nums):
            return False
        else:
            return True
        """

        n = set()
        for i in nums:
            if i in n:
                return True
            n.add(i)
        return False