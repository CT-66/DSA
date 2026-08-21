class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        new = n
        mul = 1
        add = 0
    
        while new != 0:
            mul *= (new % 10) 
            add +=  (new % 10)
            new //= 10

        return mul - add