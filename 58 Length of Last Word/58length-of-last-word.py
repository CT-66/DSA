class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lastWord = s.strip().split(" ")[-1]
        return len(lastWord)