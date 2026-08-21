class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d = dict(zip(heights, names))
        d_sorted = sorted(d.items(), reverse=True)

        result = []

        for height, name in d_sorted:
            result.append(name)

        return result