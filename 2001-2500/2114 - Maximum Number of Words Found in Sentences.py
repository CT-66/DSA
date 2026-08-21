class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max = 0
        for i in sentences:
            i = i.split(" ")
            if len(i) > max:
                max = len(i)
        return max