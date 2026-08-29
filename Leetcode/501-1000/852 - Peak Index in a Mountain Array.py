class Solution:
    # not actual solution
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        x = max(arr)
        for i in range(len(arr)):
            if arr[i] == x:
                return i
