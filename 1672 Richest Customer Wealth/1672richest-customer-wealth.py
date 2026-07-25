class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max=0
        for i in accounts:
                w=0
                for j in i:
                    w+=j
                if w>max:
                    max=w
        return max    