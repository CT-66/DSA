class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        # """
        # for i in nums2:
        #     nums1.append(i)
        # nums1[:] = sorted(nums1)
        # print(nums1)
        # nums1[:] = nums1[3:]
        # return nums1

        first_array = nums1[:m]  # only valid elements
        merged_array = first_array + nums2
        merged_array.sort()
        
        nums1[:] = merged_array