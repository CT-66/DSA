class Solution:
    def sumDecoded(self, nums: list[int]) -> int:
        import math

        sum = 0
        for i in range(len(nums)):
            w = nums[i] % 10
            d = math.floor(nums[i] / 10)
            ds = str(d)
            x = int(ds[:w])
            y = int(ds[w:])
            # x=x.replace('b', '')
            # y=y.replace('b', '')
            # dec=pow(int(x),int(y))
            sum = (sum + pow(x, y, 1000000007)) % 1000000007
        return sum
