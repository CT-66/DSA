class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for i in operations:
            if i == "--X" or i== "X--":
                x-=1
                print(x)
            elif i == "++X" or i == "X++":
                x+=1
                print(x)
            else:
                print("Else", i)
        return x