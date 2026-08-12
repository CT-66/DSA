class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        memo = {}
        def maxDiff(l, r):
            if l == r:
                return nums[l]
            if (l, r) in memo:
                return memo[(l, r)]
            
            pickLeft = nums[l] - maxDiff(l+1, r)
            pickRight = nums[r] - maxDiff(l, r-1)

            memo[(l, r)] = max(pickLeft, pickRight)
            return memo[(l, r)]

        return maxDiff(0, len(nums) - 1) >= 0