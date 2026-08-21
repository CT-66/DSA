class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.strip().replace(" ", "")
        s = ''.join(char for char in s if char.isalnum())
        s=s.lower()

        # two pointers
        for i in range(len(s)):
            if s[i] != s[len(s)-1-i]:
                return False

        return True

        #####

        # slicing
        """
        if s == s[::-1]:
            return True
        else:
            return False
        """
