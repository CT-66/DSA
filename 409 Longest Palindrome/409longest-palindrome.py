class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0

        for count in Counter(s).values():
            ans += count // 2 * 2

        if ans < len(s):
            ans += 1

        return ans