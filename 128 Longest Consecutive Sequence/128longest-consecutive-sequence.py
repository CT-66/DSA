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