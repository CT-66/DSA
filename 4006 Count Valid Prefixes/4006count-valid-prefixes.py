class Solution:
    def countValidPrefixes(self, s: str) -> int:
        # arr=[]
        # if len(s) == 1:
        #     return 1
        # if len(s) == 2:
        #     if s[0] == s[1]:
        #         return 1
        #     return 2
        # arr.append(s[0])
        # arr.append(s[1])
        # arr.append(s[2])

        # num0 = 0 
        # num1 = 0

        # for i in arr:
        #     if i == "0":
        #         num0+=1
        #     if i == "1":
        #         num1+=1
        # if s[0] == s[1] or s[1] == s[2]:
        #     return 2
        # if num0 == 2 or num1 == 2:
        #     return 3
        
        # else:
        #     return 0
        count0 = 0
        count1 = 0
        answer = 0

        for c in s:
            if c == '0':
                count0 += 1
            else:
                count1 += 1

            if abs(count0 - count1) <= 1:
                answer += 1

        return answer

