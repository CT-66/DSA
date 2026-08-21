class Solution:
    def isValid(self, s: str) -> bool:
        """
        d = {
            "]": "[",
            ")": "(",
            "}": "{",
            "[": "]",
            "(": ")",
            "{": "}"
        }
        if len(s)%2 == 0:
            arr = []
            for i in s:
                arr.append(i)
            print(arr)

            s1 = arr[:len(arr)//2]
            s2 = arr[len(arr)//2:]
            s2 = s2[::-1]
            print(s2)

            for x in s2:
                print(x)
                # print(d[str(x)])
                s2[s2.index(x)] = d[x]

            res = ""
            for i in s2:
                res+=i

            return res 
            """

        stack = []
        matches = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for i in s:
            if i in matches: # if closing bracket
                if stack and stack[-1] == matches[i]: # check if stack isn't empty
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False