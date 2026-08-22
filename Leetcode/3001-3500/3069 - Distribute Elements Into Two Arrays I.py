class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        # a1, a2 = [], []
        # for i in range(len(nums)):
        #     if i % 2 != 0:
        #         a1.append(nums[i])
        #     else:
        #         a2.append(nums[i])
        ####
        # for i in range(3):
        #     if i % 2 != 0:
        #         a1.append(nums[i])
        #     else:
        #         a2.append(nums[i])
        # if len(nums) > 3:
        #     for i in range(3, len(nums)):
        #         if a1[-1] > a2[-1]:
        #             # if i % 2 != 0:
        #             a1.append(nums[i])
        #         else:
        #             a2.append(nums[i])


        # print(a1, a2)
        # res = []
        # for _ in a2:
        #     res.append(_)
        # for _ in a1:
        #     res.append(_)

        # return res
        a1 = [nums[0]]
        a2 = [nums[1]]

        for i in range(2, len(nums)):
            if a1[-1] > a2[-1]:
                a1.append(nums[i])
            else:
                a2.append(nums[i])

        return a1 + a2
