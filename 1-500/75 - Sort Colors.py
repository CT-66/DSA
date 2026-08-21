class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums.sort()
        num0, num1, num2 = 0,0,0
        for i in nums:
            if i == 0:
                num0+=1
            elif i == 1:
                num1+=1
            elif i == 2:
                num2+=1
        
        # nums = []
        nums.clear()

        print(num0, num1, num2)

        for i in range(num0):
            nums.append(0)
        for i in range(num1):
            nums.append(1)
        for i in range(num2):
            nums.append(2)
        # nums[:] = [0] * num0 + [1] * num1 + [2] * num2

            

        