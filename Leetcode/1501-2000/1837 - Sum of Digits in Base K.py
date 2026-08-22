class Solution:
    def sumBase(self, n: int, k: int) -> int:
        def digitSum(num):
            res = 0
            while num != 0:
                res += num % 10
                num //= 10
            return res

        res = ""
        while n > 0:
            res += str(n % k)
            n //= k
        return digitSum(int(res))
