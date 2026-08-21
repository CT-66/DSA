# class Solution:
#     def pivotIndex(self, nums: List[int]) -> int:
#         p = 0
#         tSum = sum(nums)
#         lSum, rSum = [], []
#         for p in range(len(nums)):
#             for x in range(p):
#                 lSum.append(nums[x])
#             for y in range(p+1, len(nums)):
#                 rSum.append(nums[y])
#             ll = sum(lSum)
#             rr = sum(rSum)
#             # print(ll, rr)
#             if ll == rr:
#                 return p
#                 break
#             lSum.clear()
#             rSum.clear()
#         return -1

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0

        for i in range(len(nums)):
            right = total - left - nums[i]

            if left == right:
                return i

            left += nums[i]

        return -1