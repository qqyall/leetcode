class Solution:
    def reverseString(self, s: list[str]) -> None:
        for i in range(len(s) // 2 + len(s) % 2):
            s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i] 
        


s = ["h","e","l","l","o","1"]
sol = Solution()
sol.reverseString(s)
print(s)
