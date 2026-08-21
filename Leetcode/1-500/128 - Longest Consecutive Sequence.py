class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new = set(nums)
        longest = 0

        for i in new:
            # i - 1 -> check if i is the start of a sequence
            if (i - 1) not in new:
                length = 0
                while (i + length) in new:
                    length += 1
                longest = max(length, longest)
        return longest

        #####

        # brute force
        """
        class Solution:
        def longestConsecutive(self, nums: List[int]) -> int:
            nums[:] = sorted(nums)

            res = 1
            best = 1


            if len(nums) == 0:
                return 0

            for i in range(len(nums)-1):
                if nums[i+1] == nums[i] + 1:
                    res += 1
                elif nums[i+1] == nums[i]:
                    continue # for duplicate elements
                else:
                    res = 1

                best = max(best, res)

            return best

        """
