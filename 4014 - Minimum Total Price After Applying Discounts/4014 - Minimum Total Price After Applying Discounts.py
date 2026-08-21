class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        p = sorted(prices, reverse = True)
        d = sorted(discounts, reverse = True)

        new = sum(p)

        for i in range(min(len(p), len(d))):
            new -= p[i] * d[i] / 100

        return new