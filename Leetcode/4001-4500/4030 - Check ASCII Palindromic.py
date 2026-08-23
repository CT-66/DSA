class Solution:
    def isPalindromic(self, s: str) -> bool:
        res = ""
        for i in s:
            res += bin(ord(i))
        res = res.replace('b', '')
        # print(res)
        if res == res[::-1]:
            return True
        return False
