# class Solution:
#     def validMountainArray(self, arr: List[int]) -> bool:
#         if len(arr) < 3:
#             return False
#         max_element = arr.index(max(arr))
#         # print(max_element)
#         valid = True
#         for i in range(0, max_element+1):
#             for j in range(i+1, max_element+1):
#                 if arr[i] > arr[j]:
#                     valid = False
#                     break
#                 else:
#                     valid = True

#         if valid:
#             for i in range(max_element, len(arr)):
#                 for j in range(i+1, len(arr)):
#                     if arr[j] > arr[i]:
#                         valid = False
#                     else:
#                         valid = True
#         if valid:
#             return True
#         else:
#            return False

######

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        peak = arr.index(max(arr))

        # Peak cannot be first or last
        if peak == 0 or peak == len(arr) - 1:
            return False

        # Increasing before peak
        for i in range(peak):
            if arr[i] >= arr[i + 1]:
                return False

        # Decreasing after peak
        for i in range(peak, len(arr) - 1):
            if arr[i] <= arr[i + 1]:
                return False

        return True