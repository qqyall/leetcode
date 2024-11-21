class Solution:
    def myAtoi(self, s: str) -> int:
        i1 = 0
        while i1 < len(s):
            if s[i1] == ' ':
                i1 += 1
            elif s[i1] in ['-', '+'] or s[i1].isdigit():
              break
            else:
                return 0
        i2 = i1 + 1
        while i2 < len(s) and s[i2].isdigit():
            i2 += 1
        if s[i1:i2] in ['-', '+', '']:
            return 0
        num = int(s[i1:i2])
        if (num < -1 * (2**31)):
            return -1 * (2**31)
        elif (num > (2**31) - 1):
            return (2**31) - 1
        else:
            return num


s = ""
sol = Solution()
print(sol.myAtoi(s))
#print("hgfh".isalpha())
