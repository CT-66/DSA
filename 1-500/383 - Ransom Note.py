class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counts = {}

        # Count letters in magazine
        for ch in magazine:
            counts[ch] = counts.get(ch, 0) + 1

        # Use letters for ransom note
        for ch in ransomNote:
            if counts.get(ch, 0) == 0:
                return False
            counts[ch] -= 1

        return True