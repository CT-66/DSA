class Solution {
public:
    long long coloredCells(int n) {
        long long tiles = 0;
        long long i = 1;

        while (i <= n) {
            long long inc = 0;
            if (i == 1) {
                inc++;
                tiles += inc;
            }
            else {
                inc += (4 * (i-1));
                tiles += inc;
            }
            i++;
        }
        return tiles;
    }
};

