class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}

        for i in s:
            d[i] = d.get(i, 0) + 1
        
        d_sorted = sorted(d.items(), key=lambda x: x[1], reverse=True)
        print(d_sorted)

        res = ""

        for letter, freq in d_sorted:
            res+=(letter * freq)

        return res
        
