class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n

        while left <= right:
            mid = (left + right) // 2
            coins = mid * (mid + 1) // 2

            if coins == n:
                return mid
            elif coins < n:
                left = mid + 1
            else:
                right = mid - 1

        return right

        #####

        # brute force
        """
        rows = 0
        i = 1

        while n >= i:
            n -= i
            rows += 1
            i += 1

        return rows
        """

