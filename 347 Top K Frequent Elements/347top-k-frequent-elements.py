class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1 

        # sorted_items = sorted(d.items(), key=lambda x: x[1], reverse=True)
        sorted_items = sorted(
            d.items(),          # produces a view of the key-value pairs, in tuples
            key=lambda x: x[1], # sort by frequency; and only compare the second pair instead of first pair

            #Example: 
            #    (1, 3) -> compare using 3
            #    (2, 2) -> compare using 2
            #    (3, 1) -> compare using 1
            #Instead of:
            #    (1, 3) -> compare using 1
            #    (2, 2) -> compare using 2
            #    (3, 1) -> compare using 3
            
            reverse=True
        )

        # return [num for num, freq in sorted_items[:k]]
        result = []

        for item in sorted_items[:k]: # 0-k elements
            num = item[0] # 0 is tuple's index
            result.append(num)

        return result