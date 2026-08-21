class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        total = 0

        for i in range(n):
            # sum of main diagonal
            total += mat[i][i]
            # sum of other diagonal
            total += mat[i][n - 1 - i]
            
        # Subtract the center once if n is odd
        if n % 2 == 1:
            total -= mat[n // 2][n // 2]

        return total
