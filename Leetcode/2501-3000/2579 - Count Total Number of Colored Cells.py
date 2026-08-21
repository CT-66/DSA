class Solution:
    def coloredCells(self, n: int) -> int:
        tiles = 0
        i = 1

        while i <= n:
            inc = 0
            if (i == 1):
                inc += 1
                tiles += inc
            else:
                inc += 4 * (i-1)
                tiles += inc
            i += 1
        return tiles
