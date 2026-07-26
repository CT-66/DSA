class Solution:
    def firstUniqChar(self, s: str) -> int:
        # unique=s[0]
        # for i in range(1, len(s)):
        #     if s[i] != unique:
        #         for j in range(i+1, len(s)):
        #             if j==i:
        #                 break
        #         unique = s[i]
        #         return unique
        # return -1
        for i in range(len(s)):
            if s.count(s[i]) == 1:
                return i
        return -1