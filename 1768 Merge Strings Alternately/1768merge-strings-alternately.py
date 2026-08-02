class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        p1 = p2 = 0

        # main logic
        while p1 < len(word1) and p2 < len(word2):
            merged += word1[p1]
            merged += word2[p2]
            p1 += 1
            p2 += 1

        # if word1 has excess chars
        while p1 < len(word1):
            merged += word1[p1]
            p1 += 1

        # if word2 has excess chars
        while p2 < len(word2):
            merged += word2[p2]
            p2 += 1

        return merged