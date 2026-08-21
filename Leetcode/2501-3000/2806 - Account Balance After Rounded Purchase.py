class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        import math
        # # return 100 - math.ceil(purchaseAmount)
        # if purchaseAmount > 6:
        #     purchaseAmount = 10
        # return 100 - purchaseAmount
        return 100 - (math.floor((purchaseAmount + 5) / 10) * 10)
        