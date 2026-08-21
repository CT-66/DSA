class Solution:
    def maxProduct(self, n: int) -> int:
        n = sorted(list(str(n)), reverse=True)
        return int(n[0]) * int(n[1])
