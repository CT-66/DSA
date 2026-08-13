class Solution:
    def reverse(self, x: int) -> int:
        new = 0
        isNegative = False

        if x < 0:
            x = abs(x)
            isNegative = True

        while x > 0:
            new = new * 10 + x % 10
            x = x // 10

        
        if new < -2**31 or new > 2**31 - 1:
            return 0
        if isNegative:
            return -new
        return new