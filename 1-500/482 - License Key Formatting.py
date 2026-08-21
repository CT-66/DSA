class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()

        result = []
        count = 0

        for i in range(len(s) - 1, -1, -1):
            result.append(s[i])
            count += 1

            if count == k:
                result.append("-")
                count = 0

        result.reverse()

        ans = "".join(result)

        # Remove extra dash at the beginning
        if ans.startswith("-"):
            ans = ans[1:]

        return ans